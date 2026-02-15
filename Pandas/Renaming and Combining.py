# ================================================================
#  Kaggle - Pandas
#  Exercise: Renaming and Combining
# ================================================================

# ----------------------------------------------------------------
#  Q1 - Rename Columns
# ----------------------------------------------------------------

# Your code here
renamed = reviews.rename(columns=dict(region_1='region', region_2='locale'))

# Check your answer
q1.check()


# ----------------------------------------------------------------
#  Q2 - Rename Index
# ----------------------------------------------------------------

reindexed = reviews.rename_axis('wines', axis='rows')

# Check your answer
q2.check()


# ----------------------------------------------------------------
#  Q3 - Combine Datasets (Concat)
# ----------------------------------------------------------------

combined_products = pd.concat([gaming_products, movie_products])

# Check your answer
q3.check()


# ----------------------------------------------------------------
#  Q4 - Combine Datasets (Join)
# ----------------------------------------------------------------

powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))

# Check your answer
q4.check()
powerlifting_combined
