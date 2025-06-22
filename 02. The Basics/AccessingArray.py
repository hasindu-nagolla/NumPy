import numpy as np

a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(a)

# Return a specific element from the array [row, column]
print(a[1,5])

# Get a specific row from the array 
print(a[0,:])

# Get a specific column from the array
print(a[:,2])

# Getting a little more fancy [startIndex:endIndex:stepSize]
print(a[0, 1:6:2])

a[1,55] = 20  # This will raise an error because the index is out of bounds