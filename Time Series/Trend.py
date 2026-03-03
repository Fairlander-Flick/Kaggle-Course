# ================================================================
#  Kaggle - Time Series: Trend
# ================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.deterministic import DeterministicProcess


# Q1
# ----------------------------------------------------------------
# YOUR CODE HERE: Add methods to `food_sales` to compute a moving
# average with appropriate parameters for trend estimation.
trend = food_sales.rolling(
    window=12,
    center=True,
    min_periods=6,
).mean()

# Check your answer
q_1.check()

# Make a plot
ax = food_sales.plot(**plot_params, alpha=0.5)
ax = trend.plot(ax=ax, linewidth=3)


# Q2
# ----------------------------------------------------------------
# View the solution (Run this cell to receive credit!)
q_2.check()


# Q3
# ----------------------------------------------------------------
y = average_sales.copy()

dp = DeterministicProcess(index=y.index, order=3)
X = dp.in_sample()
X_fore = dp.out_of_sample(steps=90)


# Check your answer
q_3.check()


# Q4
# ----------------------------------------------------------------
# View the solution (Run this cell to receive credit!)
q_4.check()
