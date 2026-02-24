# ================================================================
#  Kaggle - Intro to Deep Learning
#  Exercise: Deep Neural Networks
# ================================================================

# ----------------------------------------------------------------
#  Q1
# ----------------------------------------------------------------

# YOUR CODE HERE
input_shape = [8]

# Check your answer
q_1.check()


# ----------------------------------------------------------------
#  Q2
# ----------------------------------------------------------------

from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    # the hidden ReLU layers
    layers.Dense(units=512, activation='relu', input_shape=[8]),
    layers.Dense(units=512, activation='relu'),
    layers.Dense(units=512, activation='relu'),
    # the linear output layer 
    layers.Dense(units=1),
])

# Check your answer
q_2.check()


# ----------------------------------------------------------------
#  Q3
# ----------------------------------------------------------------

model = keras.Sequential([
    layers.Dense(32, input_shape=[8]),
    layers.Activation('relu'),
    layers.Dense(32),
    layers.Activation('relu'),
    layers.Dense(1),
])

# Check your answer
q_3.check()

