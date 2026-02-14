# ================================================================
#  Kaggle - Python
#  Exercise: Booleans and Conditionals
# ================================================================


# ----------------------------------------------------------------
#  Q1 - Sign Function
# ----------------------------------------------------------------

# Your code goes here. Define a function called 'sign'
def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0

# Check your answer
q1.check()


# ----------------------------------------------------------------
#  Q2 - Candies to Smash (with print)
# ----------------------------------------------------------------

def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if total_candies == 1:
        print("Splitting 1 candy")
    else:
        print("Splitting", total_candies, "candies")
    return total_candies % 3

to_smash(91)
to_smash(1)


# ----------------------------------------------------------------
#  Q3 - Weather Preparedness Bug
# ----------------------------------------------------------------

def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)

# Check your answer
q3.check()


# ----------------------------------------------------------------
#  Q4 - Boolean Conversion
# ----------------------------------------------------------------

def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return True if number < 0 else False

# Check your answer
q4.check()


# ----------------------------------------------------------------
#  Q5 - Hot Dog Toppings
# ----------------------------------------------------------------

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion

# Check your answer
q5.a.check()

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not ketchup and not mustard and not onion

# Check your answer
q5.b.check()

def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return ketchup ^ mustard

# Check your answer
q5.c.check()


# ----------------------------------------------------------------
#  Q6 - Exactly One Topping
# ----------------------------------------------------------------

def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    if (int(ketchup) + int(mustard) + int(onion)) == 1:
        return True
    else:
        return False

# Check your answer
q6.check()


# ----------------------------------------------------------------
#  Q7 - Blackjack Heuristic
# ----------------------------------------------------------------

def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay.
    When calculating a hand's total value, we count aces as "high" (with value 11) if doing so
    doesn't bring the total above 21, otherwise we count them as low (with value 1). 
    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,
    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.
    """
    if player_total > 13:
        return False
    else:
        return False
