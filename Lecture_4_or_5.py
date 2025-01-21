"""    Vectors:
● A vector is a quantity defined by a magnitude and a direction.
● A vector can be represented by an array of numbers called scalars. 


Representing Vectors in Python :
● In python, a vector can be represented in many ways, the
simplest being a regular python list of numbers.
○ [1,1,1,1]
● Since Machine Learning requires lots of scientific calculations,
it is much better to use NumPy's ndarray, which provides a
lot of convenient and optimized implementations of essential
mathematical operations on vectors.
● numpy.array([1,1,1,1])


Vectorized Operations:
● Vectorized operations are far more efficient Than loops written in Python to do the same thing

"""

import numpy as np
x = np.random.rand(5,5)
y = np.random.rand(5,5)

def multiply_vector(a,b):
    return a@b

print(multiply_vector(x,y))

"""In NumPy, the term shape refers to the dimensions of an array. 
It is an attribute that describes the number of elements along each axis of the array"""

def multiply_loops(A, B):
    C = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[1]):
        for j in range(B.shape[0]):
            C[i, j] = A[i, j] * B[j, i]
    return C
print(" ")
print("Multiple using loops")
print(multiply_loops(x,y))


import timeit
# Measure time
execution_time = timeit.timeit(lambda: multiply_vector(x, y), number=1000)
print(f"Execution time for 1000 iterations: {execution_time:.6f} seconds")

execution_time = timeit.timeit(lambda: multiply_loops(x, y), number=1000)
print(f"Execution time for 1000 iterations: {execution_time:.6f} seconds")


# Addition in NumPy arrays
a = np.array([20, 50, 67, 34])
b = np.array([90, 45, 76, 23])
c = a+b
print(c)


# Subtraction in NumPy arrays
d = a-b
print(d)


# Element wise product in NumPy arrays
m = np.array([[1,1],
              [0,1]])
n = np.array([[2,0],
              [3,4]])
print(m*n)

# Matrix Product in NumPy arrays
print(np.dot(m,n))

# Division in NumPy arrays
a = np.array( [20, 30, 40, 50] )
b = np.arange(1, 5)
c = a / b
print(c)

# Integer Division in NumPy arrays
c = a//b
print(c)

# Modulus in NumPy arrays
c= a%b
print(c)

# Exponents in NumPy arrays
c = a**b
print(c)


# Conditional Operators on NumPy arrays
m = np.array([20, -5,30, 40 ])
print(m<[15, 16, 35, 36])
print(m<25)
# to get the elements below 25
print(m[m<25])


# Conditional Operators on NumPy arrays
""" 
What is Broadcasting ?
In general, when NumPy expects arrays of the same shape but
finds that this is not the case, it applies the so-called 
broadcasting rules.
Basically there are 2 rules of Broadcasting to remember.
First rule of Broadcasting
[[[1, 3 ]]] + [5] ==> [[[6, 8]]]
Shape (1(depth), 1(row), 2(col)) (1, ) (1, 1, 2)
Note: in 1d array there is not depth of array
If the arrays do not have the same rank, then a 1 will be
prepended to the smaller ranking arrays until their ranks match."""

h = np.arange(5).reshape(1,1,5)
print(h)
print(h+[10,20,30,40,50])

"""Second rule of Broadcasting
On adding a 2D array of shape (2,1) to a 2D ndarray of shape
(2, 3). NumPy will apply the second rule of broadcasting"""

k = np.arange(6).reshape(2,3)
l = np.array([100,200,300])
print(k+l)

print(np.arange(3)+5)
print(np.ones((3,3))+ np.arange(3))
print(np.arange(3).reshape((3,1))+np.arange(3))


# Mathematical and statistical functions on NumPy arrays
# Finding Mean of NumPy array elements
"""The ndarray object has a method mean() which finds the mean
of all the elements in the array regardless of the shape of the
numpy array"""

a = np.array([[-2.5, 3.1, 7], [10, 11, 12]])
print("mean =", a.mean())


"""Similar to mean there are other ndarray methods which can be
used for various computations.
min - returns the minimum element in the ndarray
max - returns the maximum element in the ndarray
sum - returns the sum of the elements in the ndarray
prod - returns the product of the elements in the ndarray
std - returns the standard deviation of the elements in the
ndarray.
var - returns the variance of the elements in the ndarray."""

a = np.array([[-2.5, 3.1, 7], [10, 11, 12]])
for func in(a.min, a.max, a.sum, a.prod, a.std, a.var):
    print(func.__name__,"=",func())


# Summing across different axes
c= np.arange(24).reshape(2,3,4)
print("print the c: ",c)
print("Sum acrosss matrices: " ,c.sum(axis=0))      #sum across matrices
print("Sum acrosss axis 1: " ,c.sum(axis=1))
print("Sum acrosss axis 2: " ,c.sum(axis=2))


"""Matrix 1:
[[ 0  1  2  3]    # Row 1
 [ 4  5  6  7]    # Row 2
 [ 8  9 10 11]]   # Row 3

Matrix 2:
[[12 13 14 15]    # Row 1
 [16 17 18 19]    # Row 2
 [20 21 22 23]]   # Row 3
 
sum across axis =0
 [[ 0+12  1+13  2+14  3+15]    -> [[12 14 16 18]
 [ 4+16  5+17  6+18  7+19]        [20 22 24 26]
 [ 8+20  9+21 10+22 11+23]]       [28 30 32 34]]

sum across axis =1
Matrix 1:
[[0+4+8 1+5+9 2+6+10 3+7+11]] -> [[12 15 18 21]
Matrix 2:
[[12+16+20 13+17+21 14+18+22 15+19+23]] -> [[48 51 54 57]]


Sum across axis=2:
Matrix 1:
[[0+1+2+3] [4+5+6+7] [8+9+10+11]] -> [[ 6] [22] [38]]
Matrix 2:
[[12+13+14+15] [16+17+18+19] [20+21+22+23]] -> [[54] [70] [86]]

"""


# Transposing Matrices
"""The T attribute is equivalent to calling transpose() when the
rank is ≥2"""

m1= np.arange(6).reshape(2,3)
print("Matrix: ",m1)
print("Matrix Transpose: ", m1.T)


# Solving a system of linear scalar equations
"""The solve function solves a system of linear scalar equations,
such as:
2x + 6y = 6
5x + 3y = -9"""
from scipy import linalg
coeffs = np.array([[2,6],[5,3]])
depvars = np.array([6,-9])
sol = linalg .solve(coeffs, depvars)
print(sol)