# ================================================================
#  Kaggle - Feature Engineering
#  Mutual Information
# ================================================================

# ----------------------------------------------------------------
#  Q1 - Calculate MI Scores
# ----------------------------------------------------------------

X = df.copy()
y = X.pop('SalePrice')

mi_scores = make_mi_scores(X, y)
print(mi_scores.head(20))
# print(mi_scores.tail(20))  # uncomment to see bottom 20

plt.figure(dpi=100, figsize=(8, 5))
plot_mi_scores(mi_scores.head(20))
# plot_mi_scores(mi_scores.tail(20))  # uncomment to see bottom 20


# ----------------------------------------------------------------
#  Q2 - Examine Features
# ----------------------------------------------------------------

sns.catplot(x="BldgType", y="SalePrice", data=df, kind="boxen");
# YOUR CODE HERE: 
feature = "GrLivArea"

sns.lmplot(
    x=feature, y="SalePrice", hue="BldgType", col="BldgType",
    data=df, scatter_kws={"edgecolor": 'w'}, col_wrap=3, height=4,
);


# ----------------------------------------------------------------
#  Q3 - Top MI Scores
# ----------------------------------------------------------------

mi_scores.head(10)
