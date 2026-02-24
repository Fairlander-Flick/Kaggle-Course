# ================================================================
#  Kaggle - Intro to Deep Learning
#  Exercise: Binary Classification
# ================================================================

# ----------------------------------------------------------------
#  Q1
# ----------------------------------------------------------------

from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.BatchNormalization(input_shape=input_shape),
    layers.Dense(256, activation='relu'),
    layers.BatchNormalization(),
    layers.Dropout(0.3),
    layers.Dense(256, activation='relu'),
    layers.BatchNormalization(),
    layers.Dropout(0.3),
    layers.Dense(1, activation='sigmoid'),
])

# Check your answer
q_1.check()


# ----------------------------------------------------------------
#  Q2
# ----------------------------------------------------------------

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['binary_accuracy'],
)

# Check your answer
q_2.check()


# ----------------------------------------------------------------
#  Q3
# ----------------------------------------------------------------

# View the solution (Run this cell to receive credit!)
q_3.check()
