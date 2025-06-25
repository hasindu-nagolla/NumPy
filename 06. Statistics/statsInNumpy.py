# =====================================================
# Statistics with NumPy Arrays
# =====================================================
import numpy as np

# ---------------------------------------------
# Example 2D Array
# ---------------------------------------------

exampleArray = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Statistics Array:\n", exampleArray)

# ---------------------------------------------
# Minimum Values
# ---------------------------------------------

# Minimum value in the entire array
print("\nMinimum value (overall):", np.min(exampleArray))

# Minimum value in each row (axis=1 → row-wise)
print("Minimum value per row (axis=1):", np.min(exampleArray, axis=1))

# ---------------------------------------------
# Axis Explanation
# ---------------------------------------------
# axis=0 → column-wise (downward through rows)
# axis=1 → row-wise (rightward through columns)

# ---------------------------------------------
# Maximum Values
# ---------------------------------------------

# Maximum value in each row
print("Maximum value per row (axis=1):", np.max(exampleArray, axis=1))

# ---------------------------------------------
# Sum of Elements
# ---------------------------------------------

# Sum of all elements
print("\nTotal sum of all elements:", np.sum(exampleArray))

# Sum of each column (axis=0)
print("Column-wise sum (axis=0):", np.sum(exampleArray, axis=0))

# Sum of each row (axis=1)
print("Row-wise sum (axis=1):", np.sum(exampleArray, axis=1))
