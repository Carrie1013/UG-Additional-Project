import numpy as np


class ValueIterationSolver(object):
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
            iterations: int,
            discount: float = None,
            initial_value: np.ndarray = None
    ):
        if discount is None:
            discount = self._gamma
        utility_grids, policy_grids = self._init_utility_policy_storage(iterations)

        if initial_value is not None:
            v_table = initial_value
        else:
            v_table = np.zeros(self._num_state, dtype=utility_grids.dtype)
        utility_grids[..., 0] = v_table
        policy_grids[..., 0] = self._get_best_policy(v_table, discount=discount)

        for i in range(1, iterations):
            v_table = self._value_iteration(utility_grid=v_table, discount=discount)
            policy_grids[..., i] = self._get_best_policy(v_table, discount=discount)
            utility_grids[..., i] = v_table
        policy_grids = policy_grids.transpose([1, 0])
        utility_grids = utility_grids.transpose([1, 0])

        result = {
            "t": np.arange(len(utility_grids)),
            "utility": utility_grids,
            "policy": policy_grids
        }

        return result

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
        policy_grids = np.zeros((self._num_state, depth), dtype=np.int32)
        return utility_grids, policy_grids
