import numpy as np

# All 0s matrix
zerosArray = np.zeros((10))
print(zerosArray)


# All 0s matrix with dimensions
zerosArray2D = np.zeros((2, 2))
print(zerosArray2D)


zerosArray3D = np.zeros((2, 2, 2))
print(zerosArray3D)  # we can create array with different shapes whatsoever we want


# All 1s matrix
onesArray = np.ones((10))
print(onesArray)


# All 1s matrix with dimensions
onesArray2D = np.ones((2, 2))
print(onesArray2D)


# create matrixes with other numbers we want
customArray = np.full((2, 2), 99)
print(customArray)


# Create matrixes with other numbers we want using full_like
x = np.array([[1, 2, 3], [4, 5, 6]])
# Creates a new array with the same shape and type as another array.
customArray = np.full_like(x, 99)
print(customArray)


# Create a matrix using random decimal numbers
# creates a random numbers between 0 and 1
randomDecimalArray = np.random.rand(4, 2)
print(randomDecimalArray)


# Create a matrix using random integers
# creates a random integers between 1 and 10
randomIntegerArray = np.random.randint(1, 10, size=(3, 3))
print(randomIntegerArray)


# Create an Identity matrix
# creates a 3x3 identity matrix, can be any size
identityArray = np.identity(3)
print(identityArray)


# Repeat an array
arrayRepeat = np.array([[1, 2, 3]])
r1 = np.repeat(arrayRepeat, 3, axis=0)  # repeat each element 3 times
print(r1)


# Matrix embedding
output = np.ones((5, 5))
print(output)

output2 = np.zeros((3, 3))
output2[1, 1] = 1
print(output2)

output[1:4, 1:4] = output2
print(output)

# Copying arrays
a = np.array([1, 2, 3])
b = a  # Direct copy, both variables point to the same array
print(b)
b[0] = 99  # Modifying b will also modify a
print("now a is => ", a, "and b is => ", b)
