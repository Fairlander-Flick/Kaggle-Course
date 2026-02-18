import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ================================================================
#  Kaggle - Data Visualization
#  Exercise: Bar Charts and Heatmaps
# ================================================================

# ----------------------------------------------------------------
#  Q1 - Load the Data
# ----------------------------------------------------------------

# Path of the file to read
ign_filepath = "../input/ign_scores.csv"

# Fill in the line below to read the file into a variable ign_data
ign_data = pd.read_csv(ign_filepath, index_col="Platform")

# Run the line below with no changes to check that you've loaded the data correctly
step_1.check()


# ----------------------------------------------------------------
#  Q2 - Review the Data
# ----------------------------------------------------------------

# Print the data
ign_data # Your code here


# What is the highest average score received by PC games, for any genre?
high_score = 7.759930
# On the Playstation Vita platform, which genre has the 
# lowest average score? Please provide the name of the column, and put your answer 
# in single quotes (e.g., 'Action', 'Adventure', 'Fighting', etc.)
worst_genre = 'Simulation'
# Check your answers
step_2.check()


# ----------------------------------------------------------------
#  Q3 - Bar Chart
# ----------------------------------------------------------------

# Set the width and height of the figure
plt.figure(figsize=(8, 6))
# Bar chart showing average score for racing games by platform
sns.barplot(x=ign_data['Racing'], y=ign_data.index)
# Add label for horizontal axis
plt.xlabel("")
# Add label for vertical axis
plt.title("Average Score for Racing Games, by Platform")

# Check your answer
step_3.a.check()


# ----------------------------------------------------------------
#  Q4 - Heatmap
# ----------------------------------------------------------------

# Heatmap showing average game score by platform and genre
# Set the width and height of the figure
plt.figure(figsize=(10,10))
# Heatmap showing average game score by platform and genre
sns.heatmap(ign_data, annot=True)
# Add label for horizontal axis
plt.xlabel("Genre")
# Add label for vertical axis
plt.title("Average Game Score, by Platform and Genre")

# Check your answer
step_4.a.check()
