# ================================================================
#  Kaggle - Intro to Game AI and Reinforcement Learning: One-Step Lookahead
# ================================================================

# Q1
# TODO: Assign your values here
A = 1e10
B = 1e4
C = 1e2
D = -1
E = -1e6
# Check your answer (this will take a few seconds to run!)
q_1.check()

# Q2
# Check your answer (Run this code cell to receive credit!)
q_2.solution()

# Q3
def my_agent(obs, config):
    # Your code here: Amend the agent!
    import random
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    return random.choice(valid_moves)

# Run this code cell to get credit for creating an agent
q_3.check()
