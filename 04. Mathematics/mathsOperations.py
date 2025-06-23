# NumPy Mathematical Capabilities
import numpy as np

# =====================================================
# Basic Element-wise Arithmetic Operations
# =====================================================

# Create a 1D array
a = np.array([1, 2, 3, 4])
print("1D Array:\n", a)

# ----------------------------------------
# Arithmetic operations with scalars
# ----------------------------------------

# Add 2 to each element
print("\nAfter adding 2 to each element:\n", a + 2)

# Subtract 2 from each element
print("After subtracting 2 from each element:\n", a - 2)

# Multiply each element by 2
print("After multiplying each element by 2:\n", a * 2)

# Divide each element by 2
print("After dividing each element by 2:\n", a / 2)

# ----------------------------------------
# Arithmetic operations with another array
# ----------------------------------------

# Create another array for element-wise operations
b = np.array([1, 0, 1, 0])
print("\nSecond Array:\n", b)

# Element-wise addition
print("Element-wise addition (a + b):\n", a + b)

# ----------------------------------------
# Power and Trigonometric Functions
# ----------------------------------------

# Square each element
print("\nAfter squaring each element (a ** 2):\n", a ** 2)

# Apply sine function to each element
print("After applying sine function to each element:\n", np.sin(a))

# ----------------------------------------
# Additional Notes
# ----------------------------------------
# For more NumPy operations, refer to:
# https://numpy.org/doc/stable/reference/routines.math.html
