# ================================================================
#  Kaggle - Data Cleaning: Character Encodings
# ================================================================

# ----------------------------------------------------------------
# Q1
# ----------------------------------------------------------------

sample_entry = b'\xa7A\xa6n'
print(sample_entry)
print('data type:', type(sample_entry))

before = sample_entry.decode("big5-tw")
new_entry = before.encode()
# Check your answer
q1.check()

# ----------------------------------------------------------------
# Q2
# ----------------------------------------------------------------

# TODO: Load in the DataFrame correctly.
police_killings = pd.read_csv("../input/fatal-police-shootings-in-the-us/PoliceKillingsUS.csv", encoding='Windows-1252')

# Check your answer
q2.check()

# ----------------------------------------------------------------
# Q3
# ----------------------------------------------------------------

# TODO: Save the police killings dataset to CSV
police_killings.to_csv("my_file.csv")

# Check your answer
q3.check()
