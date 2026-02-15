# ================================================================
#  Kaggle - Pandas
#  Exercise: Summary Functions and Maps
# ================================================================

# ----------------------------------------------------------------
#  Q1 - Median Points
# ----------------------------------------------------------------

median_points = reviews.points.median()

# Check your answer
q1.check()


# ----------------------------------------------------------------
#  Q2 - Unique Countries
# ----------------------------------------------------------------

countries = reviews.country.unique()

# Check your answer
q2.check()


# ----------------------------------------------------------------
#  Q3 - Reviews Per Country
# ----------------------------------------------------------------

reviews_per_country = reviews.country.value_counts()

# Check your answer
q3.check()


# ----------------------------------------------------------------
#  Q4 - Centered Price
# ----------------------------------------------------------------

centered_price = reviews.price - reviews.price.mean()

# Check your answer
q4.check()


# ----------------------------------------------------------------
#  Q5 - Most Bargain Wine
# ----------------------------------------------------------------

bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']

# Check your answer
q5.check()


# ----------------------------------------------------------------
#  Q6 - Descriptor Counts
# ----------------------------------------------------------------

n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

# Check your answer
q6.check()


# ----------------------------------------------------------------
#  Q7 - Star Ratings
# ----------------------------------------------------------------

def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1
    
star_ratings = reviews.apply(stars, axis='columns')

# Check your answer
q7.check()
