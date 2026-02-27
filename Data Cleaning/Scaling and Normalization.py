# ================================================================
#  Kaggle - Data Cleaning: Scaling and Normalization
# ================================================================

# ----------------------------------------------------------------
# Q1
# ----------------------------------------------------------------

# select the usd_goal_real column
original_goal_data = pd.DataFrame(kickstarters_2017.goal)

# TODO: Your code here
scaled_goal_data = minmax_scaling(original_goal_data, columns=['goal'])

# Check your answer
q1.check()

# ----------------------------------------------------------------
# Q2
# ----------------------------------------------------------------

# Check your answer (Run this code cell to receive credit!)
q2.check()
