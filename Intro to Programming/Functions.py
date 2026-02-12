# ================================================================
#  Kaggle - Intro to Programming
#  Exercise: Functions
# ================================================================

import math


# ----------------------------------------------------------------
#  Q1 - Expected Cost of a Home
# ----------------------------------------------------------------

def get_expected_cost(beds, baths):
    value = 30000 * beds + 10000 * baths + 80000
    return value

# Check your answer
q1.check()


# ----------------------------------------------------------------
#  Q2 - Compare Home Options
# ----------------------------------------------------------------

option_one = get_expected_cost(2, 3)
option_two = get_expected_cost(3, 2)
option_three = get_expected_cost(3, 3)
option_four = get_expected_cost(3, 4)

print(option_one)
print(option_two)
print(option_three)
print(option_four)

# Check your answer
q2.check()


# ----------------------------------------------------------------
#  Q3 - Paint Cost Calculator
# ----------------------------------------------------------------

def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    cost = ((sqft_walls + sqft_ceiling) / sqft_per_gallon) * cost_per_gallon
    return cost

# Check your answer
q3.check()


# ----------------------------------------------------------------
#  Q4 - Calculate Project Cost
# ----------------------------------------------------------------

project_cost = get_cost(432, 144, 400, 15)

# Check your answer
q4.check()


# ----------------------------------------------------------------
#  Q5 - Actual Cost (Rounding Up Gallons)
# ----------------------------------------------------------------

def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    cost = (math.ceil((sqft_walls + sqft_ceiling) / sqft_per_gallon)) * cost_per_gallon
    return cost

# Check your answer
q5.check()
