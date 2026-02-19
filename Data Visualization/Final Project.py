import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ================================================================
#  Kaggle - Data Visualization
#  Exercise: Final Project
# ================================================================

# ----------------------------------------------------------------
#  Q1 - Check for a Dataset
# ----------------------------------------------------------------

# Check for a dataset with a CSV file
step_1.check()


# ----------------------------------------------------------------
#  Q2 - Specify Filepath
# ----------------------------------------------------------------

# Fill in the line below: Specify the path of the CSV file to read
my_filepath = "/kaggle/input/datasets/amar5693/screen-time-sleep-and-stress-analysis-dataset/Smartphone_Usage_Productivity_Dataset_50000.csv"

# Check for a valid filepath to a CSV file in a dataset
step_2.check()


# ----------------------------------------------------------------
#  Q3 - Load the Data
# ----------------------------------------------------------------

# Fill in the line below: Read the file into a variable my_data
my_data = pd.read_csv(my_filepath)

# Check that a dataset has been uploaded into my_data
step_3.check()


# ----------------------------------------------------------------
#  Q4 - Visualize the Data
# ----------------------------------------------------------------

# Step 1: Specify the path and read the dataset
my_filepath = "/kaggle/input/datasets/amar5693/screen-time-sleep-and-stress-analysis-dataset/Smartphone_Usage_Productivity_Dataset_50000.csv"
my_data = pd.read_csv(my_filepath)

# Step 2: Define Age Groups
# Creating bins for the ages: 15-24, 25-34, 35-44, 45-54, 55-64, 65+
bins = [15, 25, 35, 45, 55, 65, 120] 
labels = ['15-24', '25-34', '35-44', '45-54', '55-64', '65+']

# Apply binning to create a new column
my_data['Age_Group'] = pd.cut(my_data['Age'], bins=bins, labels=labels, right=False)

# Step 3: Filter data for iOS users for specific analysis
ios_users = my_data[my_data['Device_Type'] == 'iOS']

# Step 4: Calculate specific counts for iOS users
female_ios_count = ios_users[ios_users['Gender'] == 'Female'].shape[0]
male_ios_count = ios_users[ios_users['Gender'] == 'Male'].shape[0]

print(f"Number of Female iOS users: {female_ios_count}")
print(f"Number of Male iOS users: {male_ios_count}")

# Step 5: Visualization
# Setting the visual style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 8))

# Creating the bar plot to compare Age Groups and Gender
# This will show if young females have higher weekend screen time
plot = sns.barplot(
    data=my_data, 
    x='Age_Group', 
    y='Weekend_Screen_Time_Hours', 
    hue='Gender', 
    palette='viridis'
)

# Adding titles and labels
plt.title('Weekend Screen Time Analysis by Age Group and Gender', fontsize=16)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Average Weekend Screen Time (Hours)', fontsize=12)
plt.legend(title='Gender')

# Step 6: Numerical Summary (Pivot Table)
pivot_summary = my_data.groupby(['Age_Group', 'Gender'])['Weekend_Screen_Time_Hours'].mean().unstack()
print("\nMean Weekend Screen Time Summary:")
print(pivot_summary)

# Final step for Kaggle exercise validation
step_4.check()
