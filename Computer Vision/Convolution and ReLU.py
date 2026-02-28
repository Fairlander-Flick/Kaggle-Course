# ================================================================
#  Kaggle - Computer Vision: Convolution and ReLU
# ================================================================

# ----------------------------------------------------------------
# Q1
# ----------------------------------------------------------------

# YOUR CODE HERE: Define a kernel with 3 rows and 3 columns.
kernel = tf.constant([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1],
])
# Uncomment to view kernel
visiontools.show_kernel(kernel)

# Check your answer
q_1.check()

# Reformat for batch compatibility.
image = tf.image.convert_image_dtype(image, dtype=tf.float32)
image = tf.expand_dims(image, axis=0)
kernel = tf.reshape(kernel, [*kernel.shape, 1, 1])
kernel = tf.cast(kernel, dtype=tf.float32)

# ----------------------------------------------------------------
# Q2
# ----------------------------------------------------------------

# YOUR CODE HERE: Give the TensorFlow convolution function (without arguments)
conv_fn = tf.nn.conv2d
# Check your answer
q_2.check()

# ----------------------------------------------------------------
# Q3
# ----------------------------------------------------------------


relu_fn = tf.nn.relu

# Check your answer
q_3.check()

# ----------------------------------------------------------------
# Q4
# ----------------------------------------------------------------

# View the solution (Run this code cell to receive credit!)
q_4.check()

image_filter = tf.nn.conv2d(
    input=image,
    filters=kernel,
    strides=1,
    padding='VALID',
)
image_detect = tf.nn.relu(image_filter)

# The first matrix is the image after convolution, and the second is
# the image after ReLU.
display(sympy.Matrix(tf.squeeze(image_filter).numpy()))
display(sympy.Matrix(tf.squeeze(image_detect).numpy()))
