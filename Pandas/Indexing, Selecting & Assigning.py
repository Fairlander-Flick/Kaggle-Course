# ================================================================
#  Kaggle - Pandas
#  Exercise: Indexing, Selecting & Assigning
# ================================================================

# ----------------------------------------------------------------
#  Q1 - Select Description Column
# ----------------------------------------------------------------

# Your code here
desc = reviews["description"]

# Check your answer
q1.check()


# ----------------------------------------------------------------
#  Q2 - Select First Description
# ----------------------------------------------------------------

first_description = reviews.description.iloc[0]

# Check your answer
q2.check()
first_description


# ----------------------------------------------------------------
#  Q3 - Select First Row
# ----------------------------------------------------------------

first_row = reviews.iloc[0]

# Check your answer
q3.check()
first_row


# ----------------------------------------------------------------
#  Q4 - Select First 10 Descriptions
# ----------------------------------------------------------------

first_descriptions = reviews.description.iloc[:10]

# Check your answer
q4.check()
first_descriptions


# ----------------------------------------------------------------
#  Q5 - Select Sample Reviews
# ----------------------------------------------------------------

indices = [1, 2, 3, 5, 8]
sample_reviews = reviews.loc[indices]

# Check your answer
q5.check()
sample_reviews


# ----------------------------------------------------------------
#  Q6 - Select Columns and Indices
# ----------------------------------------------------------------

cols = ['country', 'province', 'region_1', 'region_2']
indices = [0, 1, 10, 100]
df = reviews.loc[indices, cols]

# Check your answer
q6.check()
df


# ----------------------------------------------------------------
#  Q7 - Select Rows and Columns (Slicing)
# ----------------------------------------------------------------

cols = ['country', 'variety']
df = reviews.loc[:99, cols]

# Check your answer
q7.check()
df


# ----------------------------------------------------------------
#  Q8 - Filter by Country
# ----------------------------------------------------------------

italian_wines = reviews[reviews.country == 'Italy']

# Check your answer
q8.check()


# ----------------------------------------------------------------
#  Q9 - Complex Filtering
# ----------------------------------------------------------------

top_oceania_wines = reviews.loc[
    (reviews.country.isin(['Australia', 'New Zealand']))
    & (reviews.points >= 95)
]

# Check your answer
q9.check()
top_oceania_wines
