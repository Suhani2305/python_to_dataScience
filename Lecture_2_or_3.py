"""
numpy
Stands for "Numeric Python" or"Numerical Python"
Open Source ,
Module of Python , 
Provides fast mathematical functions

● NumPy’s main object is the homogeneous multidimensional
array
● It is a table of elements
 ○ usually numbers
 ○ all of the same type
 ○ indexed by a tuple of positive integers
● In NumPy dimensions are called axes
● The number of axes is rank 

"""

"""creating numpy array"""
# import numpy as np
# a = np.array([1,2,3,4,5,6,7,8])
# b = a.reshape(2,4)
# print(b)
# print(b[::-1]) 


"""function of numpy

1. np.zeroes  an array with all zeroes
x = np.zeros((3,4),dtype= np.int16)
print(x)


# 2. np.ones - an araay with all ones
y = np.ones((3,4), dtype = np.int16)
print(y)


3. np.full- an array with a given Value
print(np.full((3,4),67))

4. np.linspace - creating an array with evenly distributed numbers 
● Returns an array having a specific number of points
● Evenly distributed between two values
● The maximum value is included, contrary to arange
p = np.linspace(0,5/3


5. np.random.rand - creating an array with random numbers
generate random number between 0 and 1 where 0 and 1is exclusive
print(np.random.rand(2,3))


6. np.empty - creating an empty array
it generate garbage value that we should not used used 
difference between empty and random.rand is .. in random.rand its generate random value that we also use and assingn it but in empty it gives use garbage value that we should not used
print(np.empty((2,3)))
"""

"""
important attributes of a numpy object  
1. ndarray.ndim:  gives number of axes of the array
2 ndarray.shape: the dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension
3 ndarray.size : total number of elements of the array
4 ndarray.dtyp: Tells the datatype of the elements in the numpy array. All the elements in a numpy array have the same type.
c = np.arange(1,90)
print(c.dtype)
print(c)

5 ndarray.itemsize: The itemsize attribute returns the size (in bytes) of each item:
c = np.arange(1,5)
print(c.itemsize)
"""

"""
Reshaping arrays
The function reshape is used to reshape the numpy array. The
following example illustrates this.

# a = np.arange(6)
# print(a)
# b = a.reshape(2,3)
# print(b)  """

"""some diffrent things from regular python array
assign value to array element"""
# a[1:3]=-1
# print(a)

# print(b.itemsize)       # print number of element in an array

"""chnaging in the slice array also change original array """
# a_slice = a[1:5]
# a_slice[1]= 1000
# print(a)

"""Note :  
original index also modified 
if you want to copy of the data , you need to use the copy menthod as another slice  = a[2:6].copy()
"""

"""indexing  multi dimentional numpy arrays"""
# print(b[1,2])   # row 1, col 2
# print(b[1,:])   #row 1 , all col
# print(b[:,1])   #col 1 , all row

"""array[row_start : row_end , colu_start : colm end]"""
# print(b[0:2 , 1:3])


"""boolean indexing"""
# # a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# a = np.arange(12).reshape(3,4)
# print(a)
# rows_on = np.array([True,False,True])
# print(a[rows_on,:])



# import numpy as np

# a = np.arange(12).reshape(3, 4)
# print("Array a:")
# print(a)

"""Define boolean indexing array"""
# rows_on = np.array([True, False, True])  # This selects rows 0 and 2.

"""Use boolean indexing to select rows"""
# selected_rows = a[rows_on, :]  # Corrected: Access the rows specified by rows_on.
# print("\nSelected rows:")
# print(selected_rows)


"""matrix multiplication"""
# import numpy as np
# a=np.random.rand(2,2)
# b=np.random.rand(2,2)
# def multiply_vector(a,b):
#     return a@b

# print(multiply_vector(a,b))