import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ================================================================
#  Kaggle - Data Visualization
#  Exercise: Choosing Plot Types and Custom Styles
# ================================================================

# ----------------------------------------------------------------
#  Q1 - Line Chart
# ----------------------------------------------------------------

# Change the style of the figure
sns.set_style("dark")

# Line chart 
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)

# Mark the exercise complete after the code cell is run
step_1.check()
