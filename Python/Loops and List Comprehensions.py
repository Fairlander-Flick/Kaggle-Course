# ================================================================
#  Kaggle - Python
#  Exercise: Loops and List Comprehensions
# ================================================================


# ----------------------------------------------------------------
#  Q1 - Has Lucky Number
# ----------------------------------------------------------------

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for i in nums:
        if i % 7 == 0:
            return True
    return False

# Check your answer
q1.check()


# ----------------------------------------------------------------
#  Q2 - Elementwise Greater Than
# ----------------------------------------------------------------

def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    temp = []
    for i in L:
        if i <= thresh:
            temp.append(False)
        else:
            temp.append(True)
    return temp

# Check your answer
q2.check()


# ----------------------------------------------------------------
#  Q3 - Boring Menu
# ----------------------------------------------------------------

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False

# Check your answer
q3.check()


# ----------------------------------------------------------------
#  Q4 - Slot Machine Average Payout
# ----------------------------------------------------------------

def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    # Play slot machine n_runs times, calculate payout of each
    payouts = [play_slot_machine()-1 for i in range(n_runs)]
    # Calculate the average value
    avg_payout = sum(payouts) / n_runs
    return avg_payout
    
estimate_average_slot_payout(10000000)
