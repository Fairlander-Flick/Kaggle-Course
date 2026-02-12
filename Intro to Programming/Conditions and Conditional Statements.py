# ================================================================
#  Kaggle - Intro to Programming
#  Exercise: Conditions and Conditional Statements
# ================================================================


# ----------------------------------------------------------------
#  Q1 - Grade Calculator
# ----------------------------------------------------------------

def get_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80 and score <= 89:
        grade = "B"
    elif score >= 70 and score <= 79:
        grade = "C"
    elif score >= 60 and score <= 90:
        grade = "D"
    else:
        grade = "F"
    return grade

# Check your answer
q1.check()


# ----------------------------------------------------------------
#  Q2 - Cost of Engraving Project
# ----------------------------------------------------------------

def cost_of_project(engraving, solid_gold):
    engraving_length = len(engraving)
    if solid_gold == True:
        cost = engraving_length * 10 + 100
    else:
        cost = engraving_length * 7 + 50
    return cost

# Check your answer
q2.check()


# ----------------------------------------------------------------
#  Q3 - Water Bill Calculator
# ----------------------------------------------------------------

def get_water_bill(num_gallons):
    if num_gallons <= 8000:
        bill = num_gallons * 5 / 1000
    elif num_gallons >= 8001 and num_gallons <= 22000:
        bill = num_gallons * 6 / 1000
    elif num_gallons >= 22001 and num_gallons <= 30000:
        bill = num_gallons * 7 / 1000
    else:
        bill = num_gallons * 10 / 1000
    return bill

# Check your answer
q3.check()


# ----------------------------------------------------------------
#  Q4 - Phone Bill Calculator
# ----------------------------------------------------------------

def get_phone_bill(gb):
    if gb < 15:
        bill = 100
    else:
        bill = (gb - 15) * 100 + 100
    return bill

# Check your answer
q4.check()


# ----------------------------------------------------------------
#  Q5 - Food Labels Analysis
# ----------------------------------------------------------------

# Zucaritas Cereal
# https://world.openfoodfacts.org/product/7501008023624/zucaritas-kellogg-s
get_labels("solid", 40, 150, 0, 0, 150, 16)

# Mozzarella Sticks
# https://world-es.openfoodfacts.org/producto/0062325540104/mozzarella-cheese-sticks
get_labels("solid", 21, 68, 3, 0.2, 208, 0)

# Pillsbury Cookies
# https://world.openfoodfacts.org/product/0069700118545/biscuits-au-sucre-pretraches
get_labels("solid", 30, 120, 1.5, 0.1, 110, 9)

# Sunkist Orange Soda
# https://world-es.openfoodfacts.org/producto/0078000113464/orange-soda-sunkist
get_labels("liquid", 355, 160, 0, 0, 65, 44)
