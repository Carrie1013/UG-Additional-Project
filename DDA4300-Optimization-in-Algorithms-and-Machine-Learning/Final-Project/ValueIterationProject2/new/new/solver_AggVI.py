import numpy as np
import matplotlib.pyplot as plt


def _draw_l2norm_cvg(utility_grids, plot):
    value_opt = utility_grids[-1, ...]
    l2_norm_vector = np.linalg.norm(utility_grids - value_opt, ord=2, axis=1)

    iter_cvg = np.argmin(abs(l2_norm_vector - 1e-6))
    if plot:
        plt.plot(np.arange(len(utility_grids), step=1), l2_norm_vector)
        plt.xlabel('Number of Iterations')
        plt.ylabel('Error')
        plt.show()

    return l2_norm_vector

def _alpha_t(t_sa):
    return 1 / np.sqrt(t_sa)

def _value_based_aggregation(utility_grids, epsilon=0.5):
    b1, b2 = utility_grids.min(), utility_grids.max()

    delta = (b2 - b1) / epsilon
    K = np.ceil(delta).astype(int)
    w_table = list()
    mega = list()
    if K == 0:
        mega.append(np.arange(utility_grids.size).astype(int))
        w_table = [b1 + 0.5 * epsilon]
    else:
        for i in range(1, K + 1):
            pos_min =  b1 + (i - 1) * epsilon <= utility_grids
            pos_max = utility_grids < b1 + i * epsilon
            S_i = np.where(pos_min & pos_max == True)[0]
            if S_i.size != 0:
                mega.append(S_i)
                w_table.append(b1 + (i - 0.5) * epsilon)

    return mega, np.array(w_table)

def _value_mapping(w_table, v_table, mega):
    value_out = np.zeros_like(v_table)
    for i in range(len(mega)):
        value_out[mega[i]] = w_table[i]

    return value_out

def _time_divide(iterations, size_B, size_A):
    T = np.ceil(iterations / (size_B + size_A)).astype(int)
    division = list(('B' * size_B + 'A' * size_A) * T)

    return division[:iterations]

def _sampling(mega):
    index = np.random.choice(mega)

    return index

class AggVISolver(object):
    """Value Iteration Solver."""
    def __init__(
            self,
            cost_matrix: np.ndarray,
            transition_matrix: np.ndarray,
            gamma: float,
            dtype: np.dtype = np.float32
    ):
        self._cost_matrix = cost_matrix
        self._transition_matrix = transition_matrix

        num_state, num_action = self._transition_matrix.shape[:2]
        self._num_state = num_state
        self._num_action = num_action
        self._gamma = gamma
        self._dtype = dtype

    def run(
            self,
            plot: bool,
            iterations: int,
            discount: float = None,
            initial_value: np.ndarray = None,
            size_B: int = 2,
            size_A: int = 5
    ):
        division = _time_divide(iterations, size_B=size_B, size_A=size_A)

        if discount is None:
            discount = self._gamma
        utility_grids, policy_grid = self._init_utility_policy_storage(iterations)

        if initial_value is not None:
            v_table = initial_value
        else:
            v_table = np.zeros(self._num_state, dtype=utility_grids.dtype)
        utility_grids[..., 0] = v_table

        w_table = np.zeros(self._num_state)
        mega = [[i] for i in range(self._num_state)]
        t_sa = 1

        # permutation = np.arange(self._num_state)
        for i in range(1, iterations):
            if division[i] == 'B':
                # global update Bt
                if division[i - 1] == 'A':
                    v_table = _value_mapping(w_table, v_table, mega) ## initialization
                v_table = self._value_iteration(utility_grid=v_table, discount=discount)
                # v_table = self._rpc_value_iteration(utility_grid=v_table, permutation=permutation, discount=discount)
                utility_grids[..., i] = v_table

            elif division[i] == 'A':
                # state aggregation At
                if division[i - 1] == 'B':
                    mega, w_table = _value_based_aggregation(utility_grids=v_table, epsilon=0.2)
                v_tilde = _value_mapping(w_table, v_table, mega)
                for j in range(len(mega)):
                    state = _sampling(mega[j])
                    w_table[j] = (1 - _alpha_t(t_sa)) * w_table[j] + _alpha_t(t_sa) * self._calculate_utility(state, discount, v_tilde)
                v_table = _value_mapping(w_table, v_table, mega)
                utility_grids[..., i] = v_table
                t_sa += 1

        policy_grid = self._get_best_policy(v_table, discount=discount)
        utility_grids = utility_grids.transpose([1, 0])

        record = _draw_l2norm_cvg(utility_grids=utility_grids, plot=plot)

        result = {
            "t": np.arange(len(utility_grids)),
            "utility": utility_grids,
            "policy": policy_grid
        }

        return result, record

    def _rpc_value_iteration(self, utility_grid, permutation, discount=1.0):
        value_out = utility_grid.copy()
        np.random.shuffle(permutation)
        for i in permutation:
            value_out[i] = self._calculate_utility(i, discount, value_out)

        return value_out

    def _value_iteration(self, utility_grid, discount=1.0):
        value_out = np.zeros_like(utility_grid)
        for i in range(self._num_state):
            value_out[i] = self._calculate_utility(i, discount, utility_grid)

        return value_out

    def _calculate_utility(self, index, discount, utility_grid):
        assert utility_grid.shape == (self._num_state,)

        best_utility = np.min(
            self._cost_matrix[index] + discount * self._transition_matrix[index, :, :] @ utility_grid,
        )
        return best_utility

    def _get_best_policy(self, utility_grid, discount):
        # R(s, a) + \gamma * P(s, a, s') * V(s')
        out = np.argmin(np.round(
            self._cost_matrix + discount * (
                    utility_grid.reshape((1, 1, self._num_state)) * self._transition_matrix
            ).sum(axis=-1), decimals=8), axis=-1)
        return out

    def _init_utility_policy_storage(self, depth, q_table=False):
        """
        Initialize value function and policy strcture.
        :param depth: number of iterations (int).
        :param q_table: initialize q or v (bool)? If q_table = True, initialize Q[state, action, depth];
            otherwise, initialize V[state, depth].
        :return: value function (np.ndarray) and policy (np.ndarray).
        """
        if q_table:
            utility_grids = np.zeros((self._num_state, self._num_action, depth)).astype(self._dtype)
        else:
            utility_grids = np.zeros((self._num_state, depth)).astype(self._dtype)
        policy_grid = np.zeros(self._num_state, dtype=np.int32)
        return utility_grids, policy_grid
