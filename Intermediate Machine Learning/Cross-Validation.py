# ================================================================
#  Kaggle - Intermediate Machine Learning
#  Exercise: Cross-Validation
# ================================================================

# Q1
def get_score(n_estimators):
    my_pipeline = Pipeline(steps=[
        ('preprocessor', SimpleImputer()),
        ('model', RandomForestRegressor(n_estimators, random_state=0))
    ])
    scores = -1 * cross_val_score(my_pipeline, X, y,
                                  cv=3,
                                  scoring='neg_mean_absolute_error')
    return scores.mean()

# Check your answer
step_1.check()

# Q2

results = {}
for i in range(1,9):
    results[50*i] = get_score(50*i)
# Check your answer
step_2.check()

# Q3
n_estimators_best = min(results, key=results.get)

# Check your answer
step_3.check()
