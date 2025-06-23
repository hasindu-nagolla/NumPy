# NumPy Array Creation Examples
import numpy as np

# ------------------------------
# Create Arrays Filled with Zeros
# ------------------------------

# 1D array of zeros (length 10)
zerosArray = np.zeros((10))
print("1D Zeros Array:\n", zerosArray)

# 2D array of zeros (2x2)
zerosArray2D = np.zeros((2, 2))
print("\n2D Zeros Array:\n", zerosArray2D)

# 3D array of zeros (2x2x2)
zerosArray3D = np.zeros((2, 2, 2))
print("\n3D Zeros Array:\n", zerosArray3D)
# ➤ You can create arrays of any shape you want


# ------------------------------
# Create Arrays Filled with Ones
# ------------------------------

# 1D array of ones (length 10)
onesArray = np.ones((10))
print("\n1D Ones Array:\n", onesArray)

# 2D array of ones (2x2)
onesArray2D = np.ones((2, 2))
print("\n2D Ones Array:\n", onesArray2D)


# -------------------------------------
# Create Arrays with Custom Fill Values
# -------------------------------------

# 2x2 array filled with the number 99
customArray = np.full((2, 2), 99)
print("\n2D Custom Array (all 99s):\n", customArray)

# Create a new array with the same shape as x, filled with 99
x = np.array([[1, 2, 3], [4, 5, 6]])
customArray = np.full_like(x, 99)
print("\nCustom Array Using full_like():\n", customArray)


# ----------------------------------
# Random Number Arrays
# ----------------------------------

# Array of random decimal values between 0 and 1
randomDecimalArray = np.random.rand(4, 2)
print("\nRandom Decimal Array (4x2):\n", randomDecimalArray)

# Array of random integers between 1 and 10
randomIntegerArray = np.random.randint(1, 10, size=(3, 3))
print("\nRandom Integer Array (3x3):\n", randomIntegerArray)


# ------------------------------
# Identity Matrix
# ------------------------------

# 3x3 identity matrix
identityArray = np.identity(3)
print("\nIdentity Matrix (3x3):\n", identityArray)


# ------------------------------
# Repeating Elements
# ------------------------------

# Repeat a 2D array vertically
arrayRepeat = np.array([[1, 2, 3]])
r1 = np.repeat(arrayRepeat, 3, axis=0)  # Repeat the row 3 times
print("\nRepeated Array:\n", r1)


# ------------------------------
# Matrix Embedding (Nested Arrays)
# ------------------------------

# Create a 5x5 array filled with 1s
output = np.ones((5, 5))
print("\nBase Matrix (5x5 ones):\n", output)

# Create a 3x3 array of zeros with center element = 1
output2 = np.zeros((3, 3))
output2[1, 1] = 1
print("\nInner Matrix (3x3 with center = 1):\n", output2)

# Embed the inner matrix inside the outer matrix
output[1:4, 1:4] = output2
print("\nEmbedded Matrix:\n", output)


# ------------------------------
# Copying Arrays
# ------------------------------

# Direct assignment (both point to same memory)
a = np.array([1, 2, 3])
b = a
print("\nOriginal Array a:\n", a)
b[0] = 99  # Changing b also changes a
print("After modifying b:")
print("a =>", a, " b =>", b)

# Proper copying (independent copy)
b = a.copy()
b[0] = 100  # Now modifying b does NOT affect a
print("\nUsing copy():")
print("a =>", a, " b =>", b)
