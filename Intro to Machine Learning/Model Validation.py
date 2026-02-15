# ================================================================
#  Kaggle - Intro to Machine Learning
#  Exercise: Model Validation
# ================================================================

import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

# Read the home data
home_data = pd.read_csv(iowa_file_path)

# Create target object and call it y
y = home_data.SalePrice

# Create X
feature_names = ["LotArea", "YearBuilt", "1stFlrSF", "2ndFlrSF",
                      "FullBath", "BedroomAbvGr", "TotRmsAbvGrd"]
X = home_data[feature_names]

# Split into validation and training data
from sklearn.model_selection import train_test_split

# ----------------------------------------------------------------
#  Q1 - Split Data
# ----------------------------------------------------------------

# Split into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Check your answer
step_1.check()


# ----------------------------------------------------------------
#  Q2 - Specification and Training
# ----------------------------------------------------------------

# You imported DecisionTreeRegressor in your last exercise
# and that code has been copied to the setup code above. So, no need to
# import it again

# Specify the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit iowa_model with the training data.
iowa_model.fit(train_X, train_y)


# Check your answer
step_2.check()


# ----------------------------------------------------------------
#  Q3 - Make Predictions with Validation Data
# ----------------------------------------------------------------

# Predict with all validation observations
val_predictions = iowa_model.predict(val_X)

# Check your answer
step_3.check()

# print the top few validation predictions
print(val_predictions[:5])

# print the top few actual prices from validation data
print(val_y.head())


# ----------------------------------------------------------------
#  Q4 - Calculate Mean Absolute Error in Validation Data
# ----------------------------------------------------------------

from sklearn.metrics import mean_absolute_error
val_mae = mean_absolute_error(val_predictions, val_y)

# uncomment following line to see the validation_mae
print(val_mae)

# Check your answer
step_4.check()
