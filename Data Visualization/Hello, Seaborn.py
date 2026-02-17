# ================================================================
#  Kaggle - Data Visualization
#  Exercise: Hello, Seaborn
# ================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------------------------------
#  Q1 - Explore the Feedback
# ----------------------------------------------------------------

# Fill in the line below
one = 1

# Check your answer
step_1.check()


# ----------------------------------------------------------------
#  Q2 - Load the Data
# ----------------------------------------------------------------

# Path of the file to read
fifa_filepath = "../input/fifa.csv"

# Read the file into a variable fifa_data
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)

# Check your answer
step_2.check()


# ----------------------------------------------------------------
#  Q3 - Plot the Data
# ----------------------------------------------------------------

# Set the width and height of the figure
plt.figure(figsize=(16,6))

# Line chart showing how FIFA rankings evolved over time
sns.lineplot(data=fifa_data)

# Check your answer
step_3.a.check()
