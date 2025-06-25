# =====================================================
# Linear Algebra in NumPy
# =====================================================
import numpy as np

# ---------------------------------------------
# Matrix Creation
# ---------------------------------------------

# Create a 2x3 matrix filled with 1s
a = np.ones((2, 3))
print("Matrix A (2x3 - Ones):\n", a)

# Create a 3x2 matrix filled with the value 2
b = np.full((3, 2), 2)
print("\nMatrix B (3x2 - Filled with 2s):\n", b)

# ---------------------------------------------
# Matrix Multiplication
# ---------------------------------------------

# Matrix multiplication: A (2x3) × B (3x2) = Result (2x2)
result = np.matmul(a, b)
print("\nResult of A × B (Matrix Multiplication):\n", result)

# ---------------------------------------------
# Identity Matrix and Determinant
# ---------------------------------------------

# Create a 3x3 identity matrix
c = np.identity(3)
print("\nIdentity Matrix C (3x3):\n", c)

# Calculate the determinant of the identity matrix
determinant = np.linalg.det(c)
print("\nDeterminant of Identity Matrix C:", determinant)

# ---------------------------------------------
# Reference
# ---------------------------------------------

# For more linear algebra functions, see:
# https://numpy.org/doc/stable/reference/routines.linalg.html
