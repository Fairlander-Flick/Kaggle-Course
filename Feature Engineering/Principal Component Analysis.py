# ================================================================
#  Kaggle - Feature Engineering
#  Principal Component Analysis
# ================================================================

# ----------------------------------------------------------------
#  Q1 - PCA
# ----------------------------------------------------------------

# View the solution (Run this cell to receive credit!)
q_1.check()


# ----------------------------------------------------------------
#  Q2 - Interpret Component Loadings
# ----------------------------------------------------------------

# Solution 1: Inspired by loadings
X = df.copy()
y = X.pop("SalePrice")

X["Feature1"] = X.GrLivArea + X.TotalBsmtSF
X["Feature2"] = X.YearRemodAdd * X.TotalBsmtSF

score = score_dataset(X, y)
print(f"Your score: {score:.5f} RMSLE")


# Solution 2: Uses components
X = df.copy()
y = X.pop("SalePrice")

X = X.join(X_pca)
score = score_dataset(X, y)
print(f"Your score: {score:.5f} RMSLE")

# Check your answer
q_2.check()


# ----------------------------------------------------------------
#  Q3 - PCA Applications
# ----------------------------------------------------------------

# View the solution (Run this cell to receive credit!)
q_3.check()
