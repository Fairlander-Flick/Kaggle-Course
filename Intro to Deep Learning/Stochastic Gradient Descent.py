# ================================================================
#  Kaggle - Intro to Deep Learning
#  Exercise: Stochastic Gradient Descent
# ================================================================

# ----------------------------------------------------------------
#  Q1
# ----------------------------------------------------------------

model.compile(
    optimizer="adam",
    loss="mae",
)

# Check your answer
q_1.check()


# ----------------------------------------------------------------
#  Q2
# ----------------------------------------------------------------

history = model.fit(
    X, y,
    batch_size=128,
    epochs=200,
)
# Check your answer
q_2.check()


# ----------------------------------------------------------------
#  Q3
# ----------------------------------------------------------------

# View the solution (Run this cell to receive credit!)
q_3.check()


# ----------------------------------------------------------------
#  Q4
# ----------------------------------------------------------------

learning_rate = 0.15
batch_size = 16
num_examples = 64

animate_sgd(
    learning_rate=learning_rate,
    batch_size=batch_size,
    num_examples=num_examples,
    steps=50, 
    true_w=3.0, 
    true_b=2.0, 
)

# View the solution (Run this cell to receive credit!)
q_4.check()
