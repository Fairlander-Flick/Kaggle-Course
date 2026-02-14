# ================================================================
#  Kaggle - Python
#  Exercise: Functions and Getting Help
# ================================================================


# ----------------------------------------------------------------
#  Q1 - Round to Two Places
# ----------------------------------------------------------------

def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    number = round(num,2)
    return number

# Check your answer
q1.check()


# ----------------------------------------------------------------
#  Q2 - Rounding and Negative Arguments
# ----------------------------------------------------------------

# Put your test code here
number = 12.3456
print(round(number, -1))


# ----------------------------------------------------------------
#  Q3 - Candies to Smash (with default)
# ----------------------------------------------------------------

def to_smash(total_candies, friends = 3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % friends

# Check your answer
q3.check()


# ----------------------------------------------------------------
#  Q4 - Functions and help()
# ----------------------------------------------------------------

round_to_two_places(9.9999)

x = -10
y = 5
# Which of the two variables above has the smallest absolute value?
smallest_abs = min(abs(x),abs(y))
print(smallest_abs)

def f(x):
    y = abs(x)
    return y

print(f(-5))
