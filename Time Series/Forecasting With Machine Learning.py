# ================================================================
#  Kaggle - Time Series: Forecasting With Machine Learning
# ================================================================

import pandas as pd
from sklearn.multioutput import RegressorChain
from xgboost import XGBRegressor


# Q1
# ----------------------------------------------------------------
# YOUR CODE HERE: Match the task to the dataset. Answer 1, 2, or 3.
task_a = 2
task_b = 1
task_c = 3

# Check your answer
q_1.check()


# Q2
# ----------------------------------------------------------------
# View the solution (Run this cell to receive credit!)
q_2.check()


# Q3
# ----------------------------------------------------------------
y = family_sales.loc[:, 'sales']

X = make_lags(y, lags=4).dropna()

y = make_multistep_target(y, steps=16).dropna()

y, X = y.align(X, join='inner', axis=0)

# Check your answer
q_3.check()


# Q4
# ----------------------------------------------------------------
model = RegressorChain(base_estimator=XGBRegressor())

# Check your answer
q_4.check()
