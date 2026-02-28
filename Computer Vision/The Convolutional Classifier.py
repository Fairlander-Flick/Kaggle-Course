# ================================================================
#  Kaggle - Computer Vision: The Convolutional Classifier
# ================================================================

# ----------------------------------------------------------------
# Q1
# ----------------------------------------------------------------

# YOUR_CODE_HERE
pretrained_base.trainable = False

# Check your answer
q_1.check()

# ----------------------------------------------------------------
# Q2
# ----------------------------------------------------------------

from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    pretrained_base,
    layers.Flatten(),
    layers.Dense(6, activation='relu'),
    layers.Dense(1, activation='sigmoid'),
])

# Check your answer
q_2.check()

# ----------------------------------------------------------------
# Q3
# ----------------------------------------------------------------

# YOUR CODE HERE: what loss function should you use for a binary
# classification problem? (Your answer for each should be a string.)
optimizer = tf.keras.optimizers.Adam(epsilon=0.01)
model.compile(
    optimizer=optimizer,
    loss='binary_crossentropy',
    metrics=['binary_accuracy'],
)

# Check your answer
q_3.check()

# ----------------------------------------------------------------
# Q4
# ----------------------------------------------------------------

# View the solution (Run this code cell to receive credit!)
q_4.check()
