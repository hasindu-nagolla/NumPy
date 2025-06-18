import numpy as np


# 1-dimensional array
a = np.array([1, 2, 3], dtype='int') # dtype='int' part is optional, numpy infers the type automatically.
print(a)

# 2-dimensional array with float type
b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(b)

# Get dimensions of the array
print(a.ndim)
print(b.ndim)

# Get shape of the array
print(a.shape)
print(b.shape)

# Get type of the array
print(a.dtype)
print(b.dtype)

# Get size of the element in bytes
print(a.itemsize)  # size of each element in bytes, when dtype='int16', it will return 2. when dtype='float64', it will return 8.
print(b.itemsize)  

# Get total size of the array
print(a.size)  # total number of elements in the array. it will return 3.
print(b.size)  

