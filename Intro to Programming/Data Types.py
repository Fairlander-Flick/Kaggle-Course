# ================================================================
#  Kaggle - Intro to Programming
#  Exercise: Data Types
# ================================================================


# ----------------------------------------------------------------
#  Q1 - Floats and Integers
# ----------------------------------------------------------------

# Define a float
y = 1.
print(y)
print(type(y))

# Convert float to integer with the int function
z = int(y)
print(z)
print(type(z))

# How int() handles different values
print(int(1.2321))
print(int(1.747))
print(int(-3.94535))
print(int(-2.19774))


# ----------------------------------------------------------------
#  Q2 - Booleans and Arithmetic
# ----------------------------------------------------------------

print(3 * True)
print(-3.1 * True)
print(type("abc" * False))
print(len("abc" * False))


# ----------------------------------------------------------------
#  Q3 - Expected Cost with Basement
# ----------------------------------------------------------------

def get_expected_cost(beds, baths, has_basement):
    value = beds * 30000 + baths * 10000 + int(has_basement) * 40000 + 80000
    return value

# Check your answer
q3.check()


# ----------------------------------------------------------------
#  Q4 - Boolean Addition
# ----------------------------------------------------------------

print(False + False)
print(True + False)
print(False + True)
print(True + True)
print(False + True + True + True)


# ----------------------------------------------------------------
#  Q5 - Cost of Engraving Project
# ----------------------------------------------------------------

def cost_of_project(engraving, solid_gold):
    if solid_gold:
        cost = len(engraving) * 10 + 100
    else:
        cost = len(engraving) * 7 + 50
    return cost

# Check your answer
q5.check()
