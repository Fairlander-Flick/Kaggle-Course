# ================================================================
#  Kaggle - Data Visualization
#  Exercise: Line Charts
# ================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------------------------------
#  Q1 - Load the Data
# ----------------------------------------------------------------

# Path of the file to read
museum_filepath = "../input/museum_visitors.csv"

# Fill in the line below to read the file into a variable museum_data
museum_data = pd.read_csv(museum_filepath, index_col="Date", parse_dates=True)

# Run the line below with no changes to check that you've loaded the data correctly
step_1.check()


# ----------------------------------------------------------------
#  Q2 - Review the Data
# ----------------------------------------------------------------

# Fill in the line below: How many visitors did the Chinese American Museum 
# receive in July 2018?
ca_museum_jul18 = 2620 

# Fill in the line below: In October 2018, how many more visitors did Avila 
# Adobe receive than the Firehouse Museum?
avila_oct18 = 19280-4622

# Check your answers
step_2.check()


# ----------------------------------------------------------------
#  Q3 - Convince the Museum Board
# ----------------------------------------------------------------

# Set the width and height of the figure
plt.figure(figsize=(12,6))
# Line chart showing the number of visitors to each museum over time
sns.lineplot(data=museum_data)
# Add title
plt.title("Monthly Visitors to Los Angeles City Museums")
# Check your answer
step_3.check()


# ----------------------------------------------------------------
#  Q4 - Assess Seasonality
# ----------------------------------------------------------------

# Line plot showing the number of visitors to Avila Adobe over time
# Set the width and height of the figure
plt.figure(figsize=(12,6))
# Add title
plt.title("Monthly Visitors to Avila Adobe")
# Line chart showing the number of visitors to Avila Adobe over time
sns.lineplot(data=museum_data['Avila Adobe'])
# Add label for horizontal axis
plt.xlabel("Date")
# Check your answer
step_4.a.check()
