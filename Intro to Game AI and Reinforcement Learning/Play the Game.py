# ================================================================
#  Kaggle - Intro to Game AI and Reinforcement Learning: Play the Game
# ================================================================

# Q1
import numpy as np
import random

# Gets board at next step if agent drops piece in selected column
def drop_piece(grid, col, piece, config):
    next_grid = grid.copy()
    for row in range(config.rows-1, -1, -1):
        if next_grid[row][col] == 0:
            row_to_drop = row
            break
    next_grid[row_to_drop][col] = piece
    return next_grid

# Returns True if dropping piece in column results in game win
def check_winning_move(obs, config, col, piece):
    # Convert the board to a 2D grid
    grid = np.asarray(obs.board).reshape(config.rows, config.columns)
    next_grid = drop_piece(grid, col, piece, config)
    # horizontal
    for row in range(config.rows):
        for col_idx in range(config.columns-(config.inarow-1)):
            window = list(next_grid[row,col_idx:col_idx+config.inarow])
            if window.count(piece) == config.inarow:
                return True
    # vertical
    for row in range(config.rows-(config.inarow-1)):
        for col_idx in range(config.columns):
            window = list(next_grid[row:row+config.inarow,col_idx])
            if window.count(piece) == config.inarow:
                return True
    # positive diagonal
    for row in range(config.rows-(config.inarow-1)):
        for col_idx in range(config.columns-(config.inarow-1)):
            window = list(next_grid[range(row, row+config.inarow), range(col_idx, col_idx+config.inarow)])
            if window.count(piece) == config.inarow:
                return True
    # negative diagonal
    for row in range(config.inarow-1, config.rows):
        for col_idx in range(config.columns-(config.inarow-1)):
            window = list(next_grid[range(row, row-config.inarow, -1), range(col_idx, col_idx+config.inarow)])
            if window.count(piece) == config.inarow:
                return True
    return False

def agent_q1(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    for col in valid_moves:
        if check_winning_move(obs, config, col, obs.mark):
            return col
    return random.choice(valid_moves)

# Check your answer
q_1.check()

# Q2
def agent_q2(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    for col in valid_moves:
        if check_winning_move(obs, config, col, obs.mark):
            return col
    for col in valid_moves:
        if check_winning_move(obs, config, col, obs.mark%2+1):
            return col
    return random.choice(valid_moves)

# Check your answer
q_2.check()

# Q3
# Check your answer (Run this code cell to receive credit!)
q_3.solution()

# Q4
def my_agent(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    for col in valid_moves:
        if check_winning_move(obs, config, col, obs.mark):
            return col
    for col in valid_moves:
        if check_winning_move(obs, config, col, obs.mark%2+1):
            return col
    return random.choice(valid_moves)

from kaggle_environments import evaluate, make

env = make("connectx", debug=True)
env.run([my_agent, "random"])
# env.render(mode="ipython")

# Q5
import inspect
import os

def write_agent_to_file(function, file):
    with open(file, "a" if os.path.exists(file) else "w") as f:
        f.write(inspect.getsource(function))
        print(function, "written to", file)

write_agent_to_file(my_agent, "submission.py")

# Check that submission file was created
q_5.check()
