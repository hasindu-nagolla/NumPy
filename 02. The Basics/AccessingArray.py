import numpy as np

# =====================================================
# 2-D array example
# =====================================================

# Create a 2D array
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)

# Return a specific element from the array [row, column]
print(a[1, 5])

# Get a specific row from the array
print(a[0, :])

# Get a specific column from the array
print(a[:, 2])

# Getting a little more fancy [startIndex:endIndex:stepSize]
print(a[0, 1:6:2])

# Change the value of a specific element in the array

a[1, 5] = 20  # change the element at row 1, column 5
print(a)

# change the entire column 2, if it is a 3D array, we need to specify 3 values
a[:, 2] = [1, 2]
print(a)

# =====================================================
# 3-D array example
# =====================================================

# Create a 3D array
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(b)

# Accessing a index in a 3D array
tempVariable = b[0, 1, 1]
print(tempVariable)

# Replace a value in a 3D array
b[:, 1, :] = [[9, 9], [8, 8]]
print(b)

print(b.shape)