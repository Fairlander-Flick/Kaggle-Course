# ================================================================
#  Kaggle - Advanced SQL
#  Exercise: Nested and Repeated Data
# ================================================================

# ----------------------------------------------------------------
#  Q1
# ----------------------------------------------------------------

max_commits_query = """
                    SELECT committer.name AS committer_name, COUNT(*) AS num_commits
                    FROM `bigquery-public-data.github_repos.sample_commits`
                    WHERE committer.date >= '2016-01-01' AND committer.date < '2017-01-01'
                    GROUP BY committer_name
                    ORDER BY num_commits DESC
                    """
# Check your answer
q_1.check()


# ----------------------------------------------------------------
#  Q2
# ----------------------------------------------------------------

# Fill in the blank
num_rows = 6
# Check your answer
q_2.check()


# ----------------------------------------------------------------
#  Q3
# ----------------------------------------------------------------

pop_lang_query = """
                 SELECT l.name as language_name, COUNT(*) as num_repos
                 FROM `bigquery-public-data.github_repos.languages`,
                     UNNEST(language) AS l
                 GROUP BY language_name
                 ORDER BY num_repos DESC
                 """
# Check your answer
q_3.check()


# ----------------------------------------------------------------
#  Q4
# ----------------------------------------------------------------

all_langs_query = """
                  SELECT l.name, l.bytes
                  FROM `bigquery-public-data.github_repos.languages`,
                      UNNEST(language) as l
                  WHERE repo_name = 'polyrabbit/polyglot'
                  ORDER BY l.bytes DESC
                  """
# Check your answer
q_4.check()
