# ================================================================
#  Kaggle - Feature Engineering
#  Clustering With K-Means
# ================================================================

# ----------------------------------------------------------------
#  Q1 - K-Means Clustering
# ----------------------------------------------------------------

# View the solution (Run this cell to receive credit!)
q_1.check()


# ----------------------------------------------------------------
#  Q2 - Cluster Labels
# ----------------------------------------------------------------

X = df.copy()
y = X.pop("SalePrice")

features = [
    "LotArea",
    "TotalBsmtSF",
    "FirstFlrSF",
    "SecondFlrSF",
    "GrLivArea",
]

# Standardize
X_scaled = X.loc[:, features]
X_scaled = (X_scaled - X_scaled.mean(axis=0)) / X_scaled.std(axis=0)

kmeans = KMeans(n_clusters=10, n_init=10, random_state=0)
X["Cluster"] = kmeans.fit_predict(X_scaled)
# Check your answer
q_2.check()


# ----------------------------------------------------------------
#  Q3 - Cluster-Distance Features
# ----------------------------------------------------------------

kmeans = KMeans(n_clusters=10, n_init=10, random_state=0)

# YOUR CODE HERE: Create the cluster-distance features using `fit_transform`
X_cd = kmeans.fit_transform(X_scaled)

# Label features and join to dataset
X_cd = pd.DataFrame(X_cd, columns=[f"Centroid_{i}" for i in range(X_cd.shape[1])])
X = X.join(X_cd)

# Check your answer
q_3.check()
