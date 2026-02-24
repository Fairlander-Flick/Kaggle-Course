# ================================================================
#  Kaggle - Intro to Deep Learning
#  Exercise: A Single Neuron
# ================================================================

# ----------------------------------------------------------------
#  Q1
# ----------------------------------------------------------------

input_shape = [11]

# Check your answer
q_1.check()


# ----------------------------------------------------------------
#  Q2
# ----------------------------------------------------------------

from tensorflow import keras
from tensorflow.keras import layers

# YOUR CODE HERE
model = keras.Sequential([
    layers.Dense(units=1, input_shape=[11])
])

# Check your answer
q_2.check()


# ----------------------------------------------------------------
#  Q3
# ----------------------------------------------------------------

w, b = model.weights

print("Weights\n{}\n\nBias\n{}".format(w, b))
# Check your answer
q_3.check()
