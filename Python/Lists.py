# ================================================================
#  Kaggle - Python
#  Exercise: Lists
# ================================================================


# ----------------------------------------------------------------
#  Q1 - Select Second
# ----------------------------------------------------------------

def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) > 1:
        return L[1]
    else:
        return None

# Check your answer
q1.check()


# ----------------------------------------------------------------
#  Q2 - Losing Team Captain
# ----------------------------------------------------------------

def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[-1][1]

# Check your answer
q2.check()


# ----------------------------------------------------------------
#  Q3 - Purple Shell
# ----------------------------------------------------------------

def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    racers[-1], racers[0] = racers[0], racers[-1]

# Check your answer
q3.check()


# ----------------------------------------------------------------
#  Q4 - List Lengths
# ----------------------------------------------------------------

a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [3, 2, 0, 2]

# Check your answer
q4.check()


# ----------------------------------------------------------------
#  Q5 - Fashionably Late
# ----------------------------------------------------------------

def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    if name == arrivals[-1] or arrivals.index(name) < len(arrivals)/2:
        return False
    else:
        return True

# Check your answer
q5.check()
