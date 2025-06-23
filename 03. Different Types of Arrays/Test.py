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
customArray = np.full_like(x, 99) # Creates a new array with the same shape and type as another array.
print(customArray)

# Create a matrix using random decimal numbers
randomDecimalArray = np.random.rand(4, 2) # creates a random numbers between 0 and 1
print(randomDecimalArray)