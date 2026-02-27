# ================================================================
#  Kaggle - Data Cleaning: Handling Missing Values
# ================================================================

# ----------------------------------------------------------------
# Q1
# ----------------------------------------------------------------

# modules we'll use
import pandas as pd
import numpy as np

# read in all our data
sf_permits = pd.read_csv("../input/building-permit-applications-data/Building_Permits.csv")

# set seed for reproducibility
np.random.seed(0) 

# TODO: Your code here!
sf_permits.head()

# Check your answer (Run this code cell to receive credit!)
q1.check()

# ----------------------------------------------------------------
# Q2
# ----------------------------------------------------------------

# get the number of missing data points per column
missing_values_count = sf_permits.isnull().sum()

# how many total missing values do we have?
total_cells = np.product(sf_permits.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
percent_missing = (total_missing/total_cells) * 100
# Check your answer
q2.check()

# ----------------------------------------------------------------
# Q3
# ----------------------------------------------------------------

# Check your answer (Run this code cell to receive credit!)
q3.check()

# ----------------------------------------------------------------
# Q4
# ----------------------------------------------------------------

# Check your answer (Run this code cell to receive credit!)
q4.check()

# ----------------------------------------------------------------
# Q5
# ----------------------------------------------------------------

# remove all columns with at least one missing value
sf_permits_with_na_dropped = sf_permits.dropna(axis=1)

# calculate number of dropped columns
cols_in_original_dataset = sf_permits.shape[1]
cols_in_na_dropped = sf_permits_with_na_dropped.shape[1]
dropped_columns = cols_in_original_dataset - cols_in_na_dropped

# Check your answer
q5.check()

# ----------------------------------------------------------------
# Q6
# ----------------------------------------------------------------

sf_permits_with_na_imputed = sf_permits.fillna(method='bfill', axis=0).fillna(0)

# Check your answer
q6.check()
