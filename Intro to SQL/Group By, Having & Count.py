# ================================================================
#  Kaggle - Intro to SQL
#  Group By, Having & Count
# ================================================================

# ----------------------------------------------------------------
#  Q1
# ----------------------------------------------------------------

# Query to select prolific commenters and post counts
prolific_commenters_query = """
                            SELECT `by` AS author, COUNT(1) AS NumPosts
                            FROM `bigquery-public-data.hacker_news.full`
                            GROUP BY author
                            HAVING COUNT(1) > 10000
                            """
# Set up the query (cancel the query if it would use too much of 
# your quota, with the limit set to 1 GB)
safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
query_job = client.query(prolific_commenters_query, job_config=safe_config)

# API request - run the query, and return a pandas DataFrame
prolific_commenters = query_job.to_dataframe()

# View top few rows of results
print(prolific_commenters.head())

# Check your answer
q_1.check()


# ----------------------------------------------------------------
#  Q2
# ----------------------------------------------------------------

# Query to determine how many posts were deleted
deleted_posts_query = """
                      SELECT COUNT(1) AS num_deleted_posts
                      FROM `bigquery-public-data.hacker_news.full`
                      WHERE deleted = True
                      """
                      
# Set up the query
query_job = client.query(deleted_posts_query)

# API request - run the query, and return a pandas DataFrame
deleted_posts = query_job.to_dataframe()

# View results
print(deleted_posts)

num_deleted_posts = 227736

# Check your answer
q_2.check()
