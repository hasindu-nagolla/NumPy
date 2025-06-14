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