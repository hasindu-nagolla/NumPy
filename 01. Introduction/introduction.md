## NumPy (Numerical Python) - is an open-source library that provides,

01. Efficient array storage and operations.
02. Mathematical functions for linear algebra, statistics, and Fourier transforms.

## Installation

``` 
pip install numpy
```
## Import to the workspace

```
import numpy as np
```

## Why is NumPy faster than normal Python lists?

in generally, we are learning lists as array in Python. But technically, Python lists are not real arrays like in C, Java, or NumPy. Because;

01. It can hold different same types in same time.
02. Objects stored separately (non-contiguous)
03. Slower (due to type flexibility)
04. Not optimized for maths operations

## Why is NumPy faster than normal Python lists?

### Lets think, we need to store number 5 in two ways,

- using a python list = myList = [5]
- using a NumPy array = myArray = np.array([5], dtype = np.int32)

01. Memory & Storage

In NumPy, NumPy knows the type of every number (e.g., int32 = 32-bit number). So it stores numbers directly in binary like this:
```
00000000 00000000 00000000 00000101  ← just 32 bits for number 5
```
It is very compact and fast.

In Python lists, Python doesn't just store. it also stores,
- The value
- The type
- Some extra information like memory address

so instead of 32 bits, it takes much more space like,
```
00000001 00111101 11111110 ...  ← lots of extra binary data
```
