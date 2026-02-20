# ================================================================
#  Kaggle - Intro to SQL
#  Select, From & Where
# ================================================================

# ----------------------------------------------------------------
#  Q1
# ----------------------------------------------------------------

# Or to get each country just once, you could use
first_query = """
              SELECT DISTINCT country
              FROM `bigquery-public-data.openaq.global_air_quality`
              WHERE unit = "ppm"
              """
# Set up the query (cancel the query if it would use too much of 
# your quota, with the limit set to 10 GB)
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
first_query_job = client.query(first_query, job_config=safe_config)

# API request - run the query, and return a pandas DataFrame
first_results = first_query_job.to_dataframe()

# View top few rows of results
print(first_results.head())

# Check your answer
q_1.check()


# ----------------------------------------------------------------
#  Q2
# ----------------------------------------------------------------

zero_pollution_query = """
                       SELECT *
                       FROM `bigquery-public-data.openaq.global_air_quality`
                       WHERE value = 0
                       """

safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
query_job = client.query(zero_pollution_query, job_config=safe_config)

zero_pollution_results = query_job.to_dataframe()

print(zero_pollution_results.head())

# Check your answer
q_2.check()
