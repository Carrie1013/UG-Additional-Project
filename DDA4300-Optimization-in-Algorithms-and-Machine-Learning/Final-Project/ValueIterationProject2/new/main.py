from environment import Maze, Render, Action
from new.random_policy import RandomModel

import numpy as np
import logging

import matplotlib.pyplot as plt

logging.basicConfig(format="%(levelname)-8s: %(asctime)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    level=logging.INFO)  # Only show messages *equal to or above* this level

maze = np.array([
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0]
])  # 0 = free, 1 = occupied


def compute_transition_function(maze):
    num_state = maze.size
    num_action = 4
    P = np.zeros([num_state, num_action, num_state], dtype=np.float32)
    for i in range(num_state):
        for j in range(num_action):
            row, col = np.unravel_index(i, maze.shape)
            if j == 0:  # "left"
                next_row = row
                if col == 0:
                    next_col = 0
                else:
                    next_col = col - 1
            elif j == 1:  # "right"
                next_row = row
                if col == maze.shape[1] - 1:
                    next_col = col
                else:
                    next_col = col + 1
            elif j == 2:  # "up"
                next_col = col
                if row == 0:
                    next_row = row
                else:
                    next_row = row - 1
            elif j == 3:  # down
                next_col = col
                if row == maze.shape[0] - 1:
                    next_row = row
                else:
                    next_row = row + 1
            else:
                raise ValueError(j)

            if row == maze.shape[0] - 1 and col == maze.shape[1] - 1:    # terminal state
                next_row, next_col = row, col
            if maze[next_row, next_col] == 1 or maze[row, col] == 1:   # wall
                next_row, next_col = row, col
            k = np.ravel_multi_index((next_row, next_col), maze.shape)
            P[i, j, k] = 1.

            # action_meaning = {
            #     0: "left",
            #     1: "right",
            #     2: "up",
            #     3: "down"
            # }
            # print(f"({row, col} by {action_meaning[j]} to {next_row, next_col})")
    np.testing.assert_allclose(np.sum(P, axis=-1), 1.)
    return P


def compute_cost_function(maze):
    num_state = maze.size
    num_action = 4
    C = np.zeros([num_state, num_action], dtype=np.float32)
    for i in range(num_state):
        for j in range(num_action):
            row, col = np.unravel_index(i, maze.shape)
            if j == 0:  # "left"
                next_row = row
                if col == 0:
                    next_col = 0
                else:
                    next_col = col - 1
            elif j == 1:  # "right"
                next_row = row
                if col == maze.shape[1] - 1:
                    next_col = col
                else:
                    next_col = col + 1
            elif j == 2:  # "up"
                next_col = col
                if row == 0:
                    next_row = row
                else:
                    next_row = row - 1
            elif j == 3:  # down
                next_col = col
                if row == maze.shape[0] - 1:
                    next_row = row
                else:
                    next_row = row + 1
            else:
                raise ValueError(j)
            if row == maze.shape[0] - 1 and col == maze.shape[1] - 1:    # terminal state
                next_row, next_col = row, col
            if maze[next_row, next_col] == 1 or maze[row, col] == 1:   # wall
                next_row, next_col = row, col

            if next_row == maze.shape[0] - 1 and next_col == maze.shape[1] - 1:
                cost = 0
            else:
                cost = 1.
            C[i, j] = cost

            # action_meaning = {
            #     0: "left",
            #     1: "right",
            #     2: "up",
            #     3: "down"
            # }
            # print(f"({row, col} by {action_meaning[j]} cost: {cost}")
    return C


if __name__ == "__main__":
    from solver_RPCVI import RPCVISolver

    game = Maze(maze)
    cost_matrix = compute_cost_function(maze)
    transition_matrix = compute_transition_function(maze)

    vi = RPCVISolver(cost_matrix, transition_matrix, 0.99)
    results = vi.run(4000)
    policy = results["policy"][-1]    # the last policy iterate
    value = results["utility"][-1]    # the last value iterate
    print(value)
    # assert 0

    class VIModel:
        def predict(self, state):
            # We take the row first, while the game is column first
            col, row = state[0]
            index = np.ravel_multi_index((row, col), maze.shape)
            action = policy[index]
            return action

    model = VIModel()
    game.render(Render.MOVES)
    game.play(model)
    plt.show()
