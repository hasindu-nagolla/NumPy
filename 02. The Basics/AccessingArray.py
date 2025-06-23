# NumPy 2D and 3D Array Indexing and Modification Examples
import numpy as np

# =====================================================
# 2-D Array Example
# =====================================================

# Create a 2D array (2 rows × 7 columns)
a = np.array([
    [1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14]
])
print("2D Array:\n", a)

# ---------------------------------------
# Accessing elements in a 2D array
# ---------------------------------------

# Get a specific element -> row 1, column 5 (indexing starts from 0)
print("\nElement at [1, 5]:", a[1, 5])

# Get a specific row (row 0)
print("Row 0:\n", a[0, :])

# Get a specific column (column 2)
print("Column 2:\n", a[:, 2])

# Get elements using slicing: start=1, end=6 (exclusive), step=2 from row 0
print("Sliced elements (row 0, index 1 to 5, step 2):", a[0, 1:6:2])

# ---------------------------------------
# Modifying elements in a 2D array
# ---------------------------------------

# Change a specific element at row 1, column 5
a[1, 5] = 20
print("\nAfter modifying a[1, 5]:\n", a)

# Change all values in column 2
a[:, 2] = [1, 2]
print("After modifying column 2:\n", a)

# =====================================================
# 3-D Array Example
# =====================================================

# Create a 3D array with shape (2, 2, 2)
b = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("\n3D Array:\n", b)

# ---------------------------------------
# Accessing elements in a 3D array
# ---------------------------------------

# Access element at [0, 1, 1] => first block, second row, second column
tempVariable = b[0, 1, 1]
print("\nElement at [0, 1, 1]:", tempVariable)

# ---------------------------------------
# Modifying values in a 3D array
# ---------------------------------------

# Replace second row of each block with new values
b[:, 1, :] = [
    [9, 9],   # For first block
    [8, 8]    # For second block
]
print("\nAfter modifying b[:, 1, :]:\n", b)

# Print the shape of the 3D array
print("\nShape of b:", b.shape)
