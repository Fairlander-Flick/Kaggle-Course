# ================================================================
#  Kaggle - Pandas
#  Exercise: Creating, Reading and Writing
# ================================================================

# ----------------------------------------------------------------
#  Q1 - Create a DataFrame
# ----------------------------------------------------------------

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.
fruits = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])

# Check your answer
q1.check()
fruits


# ----------------------------------------------------------------
#  Q2 - Create a DataFrame with Index
# ----------------------------------------------------------------

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruit_sales.
fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
                index=['2017 Sales', '2018 Sales'])

# Check your answer
q2.check()
fruit_sales


# ----------------------------------------------------------------
#  Q3 - Create a Series
# ----------------------------------------------------------------

quantities = ['4 cups', '1 cup', '2 large', '1 can']
items = ['Flour', 'Milk', 'Eggs', 'Spam']
ingredients = pd.Series(quantities, index=items, name='Dinner')


# Check your answer
q3.check()
ingredients


# ----------------------------------------------------------------
#  Q4 - Read CSV
# ----------------------------------------------------------------

reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col=0)

# Check your answer
q4.check()
reviews


# ----------------------------------------------------------------
#  Q5 - Write to CSV
# ----------------------------------------------------------------

# Your code goes here
animals.to_csv("cows_and_goats.csv")

# Check your answer
q5.check()
