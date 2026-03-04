# ================================================================
#  Kaggle - Machine Learning Explainability: SHAP Values
# ================================================================

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.inspection import PartialDependenceDisplay
import shap


# Q1
# ----------------------------------------------------------------
# Run this code cell to receive credit!
q_1.solution()


# Q2
# ----------------------------------------------------------------
feature_name = 'number_inpatient'
PartialDependenceDisplay.from_estimator(my_model, val_X, [feature_name])
plt.show()


# Q3
# ----------------------------------------------------------------
feature_name = 'time_in_hospital'
PartialDependenceDisplay.from_estimator(my_model, val_X, [feature_name])
plt.show()


# Q4
# ----------------------------------------------------------------
# A simple pandas groupby showing the average readmission rate for each time_in_hospital.

# Do concat to keep validation data separate, rather than using all original data
all_train = pd.concat([train_X, train_y], axis=1)

all_train.groupby(['time_in_hospital']).mean().readmitted.plot()
plt.show()


# Q5
# ----------------------------------------------------------------
# Use SHAP values to show the effect of each feature of a given patient

sample_data_for_prediction = val_X.iloc[0].astype(float)  # to test function

def patient_risk_factors(model, patient_data):
    # Create object that can calculate shap values
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(patient_data)
    shap.initjs()
    return shap.force_plot(explainer.expected_value[1], shap_values[1], patient_data)
