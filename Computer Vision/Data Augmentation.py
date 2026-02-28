# ================================================================
#  Kaggle - Computer Vision: Data Augmentation
# ================================================================

# ----------------------------------------------------------------
# Q1
# ----------------------------------------------------------------

# View the solution (Run this code cell to receive credit!)
q_1.check()

# ----------------------------------------------------------------
# Q2
# ----------------------------------------------------------------

# View the solution (Run this code cell to receive credit!)
q_2.check()

# ----------------------------------------------------------------
# Q3
# ----------------------------------------------------------------

from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.InputLayer(input_shape=[128, 128, 3]),
    
    # Data Augmentation
    preprocessing.RandomContrast(factor=0.10),
    preprocessing.RandomFlip(mode='horizontal'),
    preprocessing.RandomRotation(factor=0.10),

    # Block One
    layers.BatchNormalization(renorm=True),
    layers.Conv2D(filters=64, kernel_size=3, activation='relu', padding='same'),
    layers.MaxPool2D(),

    # Block Two
    layers.BatchNormalization(renorm=True),
    layers.Conv2D(filters=128, kernel_size=3, activation='relu', padding='same'),
    layers.MaxPool2D(),

    # Block Three
    layers.BatchNormalization(renorm=True),
    layers.Conv2D(filters=256, kernel_size=3, activation='relu', padding='same'),
    layers.Conv2D(filters=256, kernel_size=3, activation='relu', padding='same'),
    layers.MaxPool2D(),

    # Head
    layers.BatchNormalization(renorm=True),
    layers.Flatten(),
    layers.Dense(8, activation='relu'),
    layers.Dense(1, activation='sigmoid'),
])

# Check your answer
q_3.check()

# ----------------------------------------------------------------
# Q4
# ----------------------------------------------------------------

# View the solution (Run this code cell to receive credit!)
q_4.solution()
