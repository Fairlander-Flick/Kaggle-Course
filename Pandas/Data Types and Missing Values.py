# ================================================================
#  Kaggle - Pandas
#  Exercise: Data Types and Missing Values
# ================================================================

# ----------------------------------------------------------------
#  Q1 - Data Type
# ----------------------------------------------------------------

# Your code here
dtype = reviews.points.dtype

# Check your answer
q1.check()


# ----------------------------------------------------------------
#  Q2 - Strings
# ----------------------------------------------------------------

point_strings = reviews.points.astype(str)

# Check your answer
q2.check()


# ----------------------------------------------------------------
#  Q3 - Missing Prices
# ----------------------------------------------------------------

missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)
# Cute alternative solution: if we sum a boolean series, True is treated as 1 and False as 0
n_missing_prices = reviews.price.isnull().sum()
# or equivalently:
n_missing_prices = pd.isnull(reviews.price).sum()

# Check your answer
q3.check()


# ----------------------------------------------------------------
#  Q4 - Reviews Per Region
# ----------------------------------------------------------------

reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)

# Check your answer
q4.check()
