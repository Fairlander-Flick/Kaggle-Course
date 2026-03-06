# ================================================================
#  Kaggle - Intro to Game AI and Reinforcement Learning: N-Step Lookahead
# ================================================================

# Q1
# Check your answer (Run this code cell to receive credit!)
q_1.solution()

# Q2
# Fill in the blank
num_leaves = 7*7*7

# Check your answer
q_2.check()

# Q3
# Fill in the blank
selected_move = 3

# Check your answer
q_3.check()

# Q4
# Check your answer (Run this code cell to receive credit!)
q_4.solution()

# Q5
def my_agent(obs, config):
    import random
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    for col in valid_moves:
        if check_winning_move(obs, config, col, obs.mark):
            return col
    for col in valid_moves:
        if check_winning_move(obs, config, col, obs.mark%2+1):
            return col
    return random.choice(valid_moves)

# Run this code cell to get credit for creating an agent
q_5.check()
