# ================================================================
#  Kaggle - Pandas
#  Exercise: Grouping and Sorting
# ================================================================

# ----------------------------------------------------------------
#  Q1 - Reviews Written
# ----------------------------------------------------------------

# Your code here
reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()

# Check your answer
q1.check()


# ----------------------------------------------------------------
#  Q2 - Best Rating Per Price
# ----------------------------------------------------------------

best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()

# Check your answer
q2.check()


# ----------------------------------------------------------------
#  Q3 - Price Extremes
# ----------------------------------------------------------------

price_extremes = reviews.groupby('variety').price.agg([min, max])

# Check your answer
q3.check()


# ----------------------------------------------------------------
#  Q4 - Sorted Varieties
# ----------------------------------------------------------------

sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)

# Check your answer
q4.check()


# ----------------------------------------------------------------
#  Q5 - Reviewer Mean Ratings
# ----------------------------------------------------------------

reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()

# Check your answer
q5.check()


# ----------------------------------------------------------------
#  Q6 - Country Variety Counts
# ----------------------------------------------------------------

country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)

# Check your answer
q6.check()
