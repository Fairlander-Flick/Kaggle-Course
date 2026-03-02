# ================================================================
#  Kaggle - Time Series: Linear Regression With Time Series
# ================================================================

import pandas as pd
import numpy as np


# Q1
# ----------------------------------------------------------------
# View the solution (Run this line to receive credit!)
q_1.check()


# Q2
# ----------------------------------------------------------------
# View the solution (Run this cell to receive credit!)
q_2.check()


# Q3
# ----------------------------------------------------------------
from sklearn.linear_model import LinearRegression

df = average_sales.to_frame()

time = np.arange(len(df.index))  # time dummy

df['time'] = time

X = df.loc[:, ['time']]  # features
y = df.loc[:, 'sales']  # target

model = LinearRegression()
model.fit(X, y)

y_pred = pd.Series(model.predict(X), index=X.index)
# Check your answer
q_3.check()


# Q4
# ----------------------------------------------------------------
df = average_sales.to_frame()

lag_1 = df['sales'].shift(1)

df['lag_1'] = lag_1

X = df.loc[:, ['lag_1']]
X.dropna(inplace=True)  # drop missing values in the feature set
y = df.loc[:, 'sales']  # create the target
y, X = y.align(X, join='inner')  # drop corresponding values in target

model = LinearRegression()
model.fit(X, y)

y_pred = pd.Series(model.predict(X), index=X.index)
# Check your answer
q_4.check()
