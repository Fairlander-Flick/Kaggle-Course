# ================================================================
#  Kaggle - Intro to Machine Learning
#  Exercise: Your First Machine Learning Model
# ================================================================

import pandas as pd

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

# Read the home data
home_data = pd.read_csv(iowa_file_path)

# ----------------------------------------------------------------
#  Q1 - Specify Prediction Target
# ----------------------------------------------------------------

# print the list of columns in the dataset to find the name of the prediction target
print(home_data.columns)
y = home_data.SalePrice

# Check your answer
step_1.check()


# ----------------------------------------------------------------
#  Q2 - Create X
# ----------------------------------------------------------------

feature_names = ["LotArea", "YearBuilt", "1stFlrSF", "2ndFlrSF",
                      "FullBath", "BedroomAbvGr", "TotRmsAbvGrd"]

X = home_data[feature_names]

# Check your answer
step_2.check()

# Review data
# print description or statistics from X
print(X.describe())

# print the top few lines
print(X.head())


# ----------------------------------------------------------------
#  Q3 - Specify and Fit Model
# ----------------------------------------------------------------

from sklearn.tree import DecisionTreeRegressor
iowa_model = DecisionTreeRegressor(random_state=1)
iowa_model.fit(X, y)

# Check your answer
step_3.check()


# ----------------------------------------------------------------
#  Q4 - Make Predictions
# ----------------------------------------------------------------

predictions = iowa_model.predict(X)
print(predictions)

# Check your answer
step_4.check()
