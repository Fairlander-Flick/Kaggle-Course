import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ================================================================
#  Kaggle - Data Visualization
#  Exercise: Scatter Plots
# ================================================================

# ----------------------------------------------------------------
#  Q1 - Load the Data
# ----------------------------------------------------------------

# Path of the file to read
candy_filepath = "../input/candy.csv"

# Fill in the line below to read the file into a variable candy_data
candy_data = pd.read_csv(candy_filepath, index_col="id")

# Run the line below with no changes to check that you've loaded the data correctly
step_1.check()


# ----------------------------------------------------------------
#  Q2 - Review the Data
# ----------------------------------------------------------------

# Print the first five rows of the data
candy_data.head(5) # Your code here

# Fill in the line below: Which candy was more popular with survey respondents:
# Print the first five rows of the data
candy_data.head()
# Which candy was more popular with survey respondents:
# '3 Musketeers' or 'Almond Joy'?
more_popular = '3 Musketeers'
# Which candy has higher sugar content: 'Air Heads'
# or 'Baby Ruth'?
more_sugar = 'Air Heads'
# Check your answers
step_2.check()


# ----------------------------------------------------------------
#  Q3 - Scatter Plot
# ----------------------------------------------------------------

# Scatter plot showing the relationship between 'sugarpercent' and 'winpercent'
sns.scatterplot(x=candy_data['sugarpercent'], y=candy_data['winpercent']) # Your code here

# Check your answer
step_3.a.check()


# ----------------------------------------------------------------
#  Q4 - Regression Plot
# ----------------------------------------------------------------

# Scatter plot w/ regression line showing the relationship between 'sugarpercent' and 'winpercent'
sns.regplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])

# Check your answer
step_4.a.check()


# ----------------------------------------------------------------
#  Q5 - Scatter Plot with Hue
# ----------------------------------------------------------------

# Scatter plot showing the relationship between 'pricepercent', 'winpercent', and 'chocolate'
sns.scatterplot(x=candy_data['pricepercent'], y=candy_data['winpercent'], hue=candy_data['chocolate'])

# Check your answer
step_5.check()


# ----------------------------------------------------------------
#  Q6 - LM Plot
# ----------------------------------------------------------------

# Color-coded scatter plot w/ regression lines
sns.lmplot(x="pricepercent", y="winpercent", hue="chocolate", data=candy_data)
# Check your answer
step_6.a.check()


# ----------------------------------------------------------------
#  Q7 - Swarm Plot
# ----------------------------------------------------------------

# Scatter plot showing the relationship between 'chocolate' and 'winpercent'
sns.swarmplot(x=candy_data['chocolate'], y=candy_data['winpercent'])
# Check your answer
step_7.a.check()
