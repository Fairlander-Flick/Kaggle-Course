# ================================================================
#  Kaggle - Intermediate Machine Learning
#  Exercise: XGBoost
# ================================================================

# Q1
from xgboost import XGBRegressor
# Define the model
my_model_1 = XGBRegressor(random_state=0)

# Fit the model
my_model_1.fit(X_train, y_train)

# Check your answer
step_1.a.check()

from sklearn.metrics import mean_absolute_error
# Get predictions
predictions_1 = my_model_1.predict(X_valid)
# Check your answer
step_1.b.check()

mae_1 = mean_absolute_error(predictions_1, y_valid)
print("Mean Absolute Error:" , mae_1)

# Uncomment to print MAE
# print("Mean Absolute Error:" , mae_1)

# Check your answer
step_1.c.check()

# Q2

# Define the model
my_model_2 = XGBRegressor(n_estimators=1000, learning_rate=0.05)

# Fit the model
my_model_2.fit(X_train, y_train)

# Get predictions
predictions_2 = my_model_2.predict(X_valid)

# Calculate MAE
mae_2 = mean_absolute_error(predictions_2, y_valid)
print("Mean Absolute Error:" , mae_2)

# Uncomment to print MAE
# print("Mean Absolute Error:" , mae_2)

# Check your answer
step_2.check()

# Q3

# Define the model
my_model_3 = XGBRegressor(n_estimators=1)

# Fit the model
my_model_3.fit(X_train, y_train)

# Get predictions
predictions_3 = my_model_3.predict(X_valid)

# Calculate MAE
mae_3 = mean_absolute_error(predictions_3, y_valid)
print("Mean Absolute Error:" , mae_3)
# Uncomment to print MAE
# print("Mean Absolute Error:" , mae_3)

# Check your answer
step_3.check()
