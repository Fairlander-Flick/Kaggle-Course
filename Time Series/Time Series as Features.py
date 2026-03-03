# ================================================================
#  Kaggle - Time Series: Time Series as Features
# ================================================================

import pandas as pd
import matplotlib.pyplot as plt


# Q1
# ----------------------------------------------------------------
# YOUR CODE HERE
y_ma = y.rolling(7, center=True).mean()

ax = y_ma.plot()
ax.set_title("Seven-Day Moving Average");

# Check your answer
q_1.check()


# Q2
# ----------------------------------------------------------------
# View the solution (Run this cell to receive credit!)
q_2.check()


# Q3
# ----------------------------------------------------------------
q_3.check()


# Q4
# ----------------------------------------------------------------
X_lags = make_lags(y_deseason, lags=1)

X_promo = pd.concat([
    make_lags(onpromotion, lags=1),
    onpromotion,
    make_leads(onpromotion, leads=1),
], axis=1)

X = pd.concat([X_time, X_lags, X_promo], axis=1).dropna()
y, X = y.align(X, join='inner')

# Check your answer
q_4.check()


# Q5
# ----------------------------------------------------------------
y_lag = supply_sales.loc[:, 'sales'].shift(1)
onpromo = supply_sales.loc[:, 'onpromotion']

mean_7 = y_lag.rolling(7).mean()
median_14 = y_lag.rolling(14).median()
std_7 = y_lag.rolling(7).std()
promo_7 = onpromo.rolling(7, center=True).sum()


# Check your answer
q_5.check()
