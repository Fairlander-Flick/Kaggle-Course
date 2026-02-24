# ================================================================
#  Kaggle - Intro to Deep Learning
#  Exercise: Overfitting and Underfitting
# ================================================================

# ----------------------------------------------------------------
#  Q1
# ----------------------------------------------------------------

# View the solution (Run this cell to receive credit!)
q_1.check()


# ----------------------------------------------------------------
#  Q2
# ----------------------------------------------------------------

# View the solution (Run this cell to receive credit!)
q_2.check()


# ----------------------------------------------------------------
#  Q3
# ----------------------------------------------------------------

from tensorflow.keras import callbacks
from tensorflow.keras.callbacks import EarlyStopping

early_stopping = EarlyStopping(
    min_delta=0.001, # minimium amount of change to count as an improvement
    patience=5, # how many epochs to wait before stopping
    restore_best_weights=True,
)
# Check your answer
q_3.check()


# ----------------------------------------------------------------
#  Q4
# ----------------------------------------------------------------

# View the solution (Run this cell to receive credit!)
q_4.check()
