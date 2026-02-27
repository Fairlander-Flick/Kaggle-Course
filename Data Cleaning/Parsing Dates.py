# ================================================================
#  Kaggle - Data Cleaning: Parsing Dates
# ================================================================

# ----------------------------------------------------------------
# Q1
# ----------------------------------------------------------------

# TODO: Your code here!
earthquakes['Date'].head()

# Check your answer (Run this code cell to receive credit!)
q1.check()

# ----------------------------------------------------------------
# Q2
# ----------------------------------------------------------------

earthquakes[3378:3383]

date_lengths = earthquakes.Date.str.len()
date_lengths.value_counts()

indices = np.where([date_lengths == 24])[1]
print('Indices with corrupted data:', indices)
earthquakes.loc[indices]

# TODO: Your code here
earthquakes.loc[3378, "Date"] = "02/23/1975"
earthquakes.loc[7512, "Date"] = "04/28/1985"
earthquakes.loc[20650, "Date"] = "03/13/2011"
earthquakes['date_parsed'] = pd.to_datetime(earthquakes['Date'], format="%m/%d/%Y")
# Check your answer
q2.check()

# ----------------------------------------------------------------
# Q3
# ----------------------------------------------------------------

# try to get the day of the month from the date column
day_of_month_earthquakes = earthquakes['date_parsed'].dt.day

# Check your answer
q3.check()

# ----------------------------------------------------------------
# Q4
# ----------------------------------------------------------------

# TODO: Your code here!
# remove na's
day_of_month_earthquakes = day_of_month_earthquakes.dropna()

# plot the day of the month
sns.distplot(day_of_month_earthquakes, kde=False, bins=31)

# Check your answer (Run this code cell to receive credit!)
q4.check()
