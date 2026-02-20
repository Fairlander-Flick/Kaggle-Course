# ================================================================
#  Kaggle - Intro to SQL
#  Getting Started With SQL and BigQuery
# ================================================================

# ----------------------------------------------------------------
#  Q1
# ----------------------------------------------------------------

# List all the tables in the "chicago_crime" dataset
tables = list(client.list_tables(dataset))

# Print number of tables in the dataset
print(len(tables))

num_tables = 1

# Check your answer
q_1.check()


# ----------------------------------------------------------------
#  Q2
# ----------------------------------------------------------------

# Construct a reference to the "crime" table
table_ref = dataset_ref.table("crime")

# API request - fetch the table
table = client.get_table(table_ref)

# Print information on all the columns in the "crime" table in the "chicago_crime" dataset
print(table.schema)

num_timestamp_fields = 2

# Check your answer
q_2.check()


# ----------------------------------------------------------------
#  Q3
# ----------------------------------------------------------------

fields_for_plotting = ['latitude', 'longitude'] # Put your answers here

# Check your answer
q_3.check()
