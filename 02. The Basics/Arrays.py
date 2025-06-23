# NumPy Array Basics: Dimensions, Shape, Type, and Size
import numpy as np

# =====================================================
# Create NumPy Arrays
# =====================================================

# 1-dimensional array (dtype is optional, inferred automatically)
a = np.array([1, 2, 3], dtype='int')
print("1D Integer Array:\n", a)

# 2-dimensional array with float type
b = np.array([
    [9.0, 8.0, 7.0],
    [6.0, 5.0, 4.0]
])
print("\n2D Float Array:\n", b)

# =====================================================
# Array Dimensions
# =====================================================

print("\nNumber of Dimensions:")
print("a.ndim =", a.ndim)  # Output: 1
print("b.ndim =", b.ndim)  # Output: 2

# =====================================================
# Array Shape
# =====================================================

print("\nShape of Arrays (rows, columns):")
print("a.shape =", a.shape)  # Output: (3,)
print("b.shape =", b.shape)  # Output: (2, 3)

# =====================================================
# Data Type of Array Elements
# =====================================================

print("\nData Type of Array Elements:")
print("a.dtype =", a.dtype)  # Output: int
print("b.dtype =", b.dtype)  # Output: float64

# =====================================================
# Size of Each Element (in bytes)
# =====================================================

print("\nSize of Each Element (in bytes):")
print("a.itemsize =", a.itemsize)  # e.g., 4 bytes for int32, 2 for int16
print("b.itemsize =", b.itemsize)  # 8 bytes for float64

# =====================================================
# Total Number of Elements
# =====================================================

print("\nTotal Number of Elements in Each Array:")
print("a.size =", a.size)  # Output: 3
print("b.size =", b.size)  # Output: 6
