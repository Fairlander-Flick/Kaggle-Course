# ================================================================
#  Kaggle - Time Series: Seasonality
# ================================================================

import pandas as pd
from statsmodels.tsa.deterministic import CalendarFourier, DeterministicProcess


# Q1
# ----------------------------------------------------------------
# View the solution (Run this line to receive credit!)
q_1.check()


# Q2
# ----------------------------------------------------------------
y = average_sales.copy()

fourier = CalendarFourier(freq='M', order=4)
dp = DeterministicProcess(
    index=y.index,
    constant=True,
    order=1,
    seasonal=True,
    additional_terms=[fourier],
    drop=True,
)
X = dp.in_sample()

# Check your answer
q_2.check()


# Q3
# ----------------------------------------------------------------
# View the solution (Run this cell to receive credit!)
q_3.check()


# Q4
# ----------------------------------------------------------------
X_holidays = pd.get_dummies(holidays)

# Join to training data
X2 = X.join(X_holidays, on='date').fillna(0.0)
# Check your answer
q_4.check()
