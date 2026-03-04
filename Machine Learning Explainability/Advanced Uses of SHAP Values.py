# ================================================================
#  Kaggle - Machine Learning Explainability: Advanced Uses of SHAP Values
# ================================================================

import shap


# Q1
# ----------------------------------------------------------------
# set following variable to 'diag_1_428' or 'payer_code_?'
feature_with_bigger_range_of_effects = "diag_1_428"

# Check your answer
q_1.check()


# Q2
# ----------------------------------------------------------------
# Check your answer (Run this code cell to receive credit!)
q_2.solution()


# Q3
# ----------------------------------------------------------------
# Set following var to "diag_1_428" if changing it to 1 has bigger effect.  Else set it to 'payer_code_?'
bigger_effect_when_changed = "diag_1_428"

# Check your answer
q_3.check()


# Q4
# ----------------------------------------------------------------
# Check your answer (Run this code cell to receive credit!)
q_4.solution()


# Q5
# ----------------------------------------------------------------
# Check your answer (Run this code cell to receive credit!)
q_5.solution()


# Q6
# ----------------------------------------------------------------
shap.summary_plot(shap_values[1], small_val_X)

# Your code here
shap.dependence_plot('num_lab_procedures', shap_values[1], small_val_X)
shap.dependence_plot('num_medications', shap_values[1], small_val_X)
