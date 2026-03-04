# ================================================================
#  Kaggle - Machine Learning Explainability: Permutation Importance
# ================================================================

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import eli5
from eli5.sklearn import PermutationImportance


# Q1
# ----------------------------------------------------------------
# Check your answer (Run this code cell to receive credit!)
q_1.solution()


# Q2
# ----------------------------------------------------------------
# Make a small change to the code below to use in this problem. 
perm = PermutationImportance(first_model, random_state=1).fit(val_X, val_y)

# Check your answer
q_2.check()

# visualize your results
eli5.show_weights(perm, feature_names = val_X.columns.tolist())


# Q3
# ----------------------------------------------------------------
# Check your answer (Run this code cell to receive credit!)
q_3.solution()


# Q4
# ----------------------------------------------------------------
# create new features
data['abs_lon_change'] = abs(data.dropoff_longitude - data.pickup_longitude)
data['abs_lat_change'] = abs(data.dropoff_latitude - data.pickup_latitude)

features_2  = ['pickup_longitude',
               'pickup_latitude',
               'dropoff_longitude',
               'dropoff_latitude',
               'abs_lat_change',
               'abs_lon_change']

X = data[features_2]
new_train_X, new_val_X, new_train_y, new_val_y = train_test_split(X, y, random_state=1)
second_model = RandomForestRegressor(n_estimators=30, random_state=1).fit(new_train_X, new_train_y)

# Create a PermutationImportance object on second_model and fit it to new_val_X and new_val_y
perm2 = PermutationImportance(second_model, random_state=1).fit(new_val_X, new_val_y)

# show the weights for the permutation importance you just calculated
eli5.show_weights(perm2, feature_names = features_2)

# Check your answer
q_4.check()


# Q5
# ----------------------------------------------------------------
# Check your answer (Run this code cell to receive credit!)
q_5.solution()


# Q6
# ----------------------------------------------------------------
# Check your answer (Run this code cell to receive credit!)
q_6.solution()
