# =====================================================
# Reorganizing Arrays in NumPy
# =====================================================
import numpy as np

# ---------------------------------------------
# Initial 2D Array
# ---------------------------------------------

array = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

print("Original Array:\n", array)
print("Shape of Original Array:", array.shape)

# ---------------------------------------------
# Reshaping Arrays
# ---------------------------------------------

# Reshape to (8, 1)
afterArray = array.reshape(8, 1)
print("\nReshaped Array (8x1):\n", afterArray)
print("Shape after reshaping:", afterArray.shape)

# NOTE:
# Reshaping must preserve total number of elements.
# For example, array.reshape(2, 3) would raise an error because 8 ≠ 2×3

# ---------------------------------------------
# Vertical Stacking (vstack)
# ---------------------------------------------

# Vectors to stack vertically
V1 = np.array([1, 2, 3, 4])
V2 = np.array([5, 6, 7, 8])  # Ensure same shape as V1

print("\nVertical Stack (2 Vectors):\n", np.vstack([V1, V2]))

# Multiple vertical stacks
print("\nVertical Stack (V1 + 3x V2):\n", np.vstack([V1, V2, V2, V2]))

# ---------------------------------------------
# Horizontal Stacking (hstack)
# ---------------------------------------------

# 2x3 and 2x2 matrices
H1 = np.ones([2, 3])   # 2 rows × 3 columns, all 1s
H2 = np.zeros([2, 2])  # 2 rows × 2 columns, all 0s

# Horizontally stack H1 and H2
print("\nHorizontal Stack (H1 + H2):\n", np.hstack((H1, H2)))

# Stack with more copies of H2
print("\nHorizontal Stack (H1 + 3x H2):\n", np.hstack((H1, H2, H2, H2)))
