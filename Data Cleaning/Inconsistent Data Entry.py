# ================================================================
#  Kaggle - Data Cleaning: Inconsistent Data Entry
# ================================================================

# ----------------------------------------------------------------
# Q1
# ----------------------------------------------------------------

# TODO: Your code here
unis = professors['Graduated from'].unique()
print(unis)

# Check your answer (Run this code cell to receive credit!)
q1.check()

# ----------------------------------------------------------------
# Q2
# ----------------------------------------------------------------

# TODO: Your code here
professors['Graduated from'] = professors['Graduated from'].str.strip()

# Check your answer
q2.check()

# ----------------------------------------------------------------
# Q3
# ----------------------------------------------------------------

# get all the unique values in the 'City' column
countries = professors['Country'].unique()

# sort them alphabetically and then take a closer look
countries.sort()
countries

# TODO: Your code here!
matches = fuzzywuzzy.process.extract("usa", countries, limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)
replace_matches_in_column(df=professors, column='Country', string_to_match="usa", min_ratio=70)

# Check your answer
q3.check()
