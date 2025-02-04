"""What is Pandas?

● One of the most widely used Python libraries in Data Science after
NumPy and Matplotlib
● The Pandas library Provides
○ High-performance
○ Easy-to-use data structures and
○ Data analysis tools"""




# creating a series
import numpy as np
import pandas as pd
s= pd.Series([2,-1,3,5])
a = pd.Series([2,-1,3,5], index=['a','b','c','d'], name="profit")
print(s)
print("Series with docarated : ", a)
print(np.square(s))
# Arithmetic operation on the series
print(s+[1000,2000,3000,4000])
# Broadcasting
print(s+1000)
# Binary and conditional operations
print(s<0)
"""Note: series accept heterogenous type of data but ndarray does not accept
series is col data but ndarray is row Data 
series is give indexing with data but ndarray does not gave
In series with also mention another index that also not numerical index its is like ["a","b"....]
we can docarate data in series"""


# Index labels - Integer location
s2 = pd.Series([68,83,112,68])
print(s2)
# Index labels - Set Manually
s2 = pd.Series([68,83,112,68], index=["alice","bob","charles","darwin"])
print(s2)
# Access the items in series
# ● By specifying integer location
print(s2[1])      #pandas take it as label index 
# ● By specifying label
print(s2["bob"])

# Access the items in series - Recommendations
# ● Use the loc attribute when accessing by label
print(s2.iloc[1])
# ● Use iloc attribute when accessing by integer location
print(s2.loc["bob"])

# practice question
s3 = pd.Series([1,2,3,4,5], index=["one", 2,"three",4,5])
print(s3[2])  # in this firstly it check in label index and gave value if value not found then it take from series like in next question
print(s3.iloc[3])  #its is treating as integer index not label index


# Init from Python dict:pass python dic to series
weights ={"alice":68, "bob":83 , "colin":86 , "darwin":68}
s3 = pd.Series(weights)
print(s3)


# Control the elements to include and specify their order
s4 =pd.Series(weights, index =["colin","bob"])
print(" ")
print(s4)
s4 =pd.Series(weights, index =["colin","bob","suhani"])    #its convert into float beacuse its also help in missing data and for missing data its used NaN(not a number) that is floating number that why it convert into float
print(" ")
print(s4)


# Automatic alignment
"""● When an operation involves multiple Series objects
● Pandas automatically aligns items by matching index labels"""
print(" ")
print(s2+s3)
# Do not forget to set the right index labels, else you may get surprising results
s5 = pd.Series([1000,1000,1000,1000])
print(" ")
print(s2+s5)
# Series name - A Series can have a name
print(" ")
s6 = pd.Series([83,68], index =["bob","alice"], name="Weights")
print(s6)   #whats is the difference bw s6 and weights .. s6 is variable that assign a series and weight is a name of that series

# init with a scaler
meaning = pd.Series(42, ["life", "universe","everything"])
print(" ")
print(meaning)



# # plotting a series
# import pandas as pd
# import matplotlib.pyplot as plt

# temperatures = [4.4, 5.1, 6.1, 6.2, 6.1, 6.1, 5.7, 5.2, 4.7, 4.1, 3.9, 3.5]
# s7 = pd.Series(temperatures, name="Temperature")
# s7.plot()
# plt.show()




"""Pandas - DataFrame Objects
● A DataFrame object represents
○ A spreadsheet,
○ With cell values,
○ Column names
○ And row index labels
● Visualize DataFrame as dictionaries of Series"""
 
# Creating a DataFrame - Pass a dictionary of Series objects
people_dict = {
    "weight": pd.Series([68, 83, 112],index=["alice", "bob", "charles"]),
    "birthyear": pd.Series([1984, 1985, 1992], index=["bob", "alice", "charles"], name="year"),
    "children": pd.Series([0, 3], index=["charles","bob"]),
    "hobby": pd.Series(["Biking", "Dancing"], index=["alice", "bob"]),
}
people = pd.DataFrame(people_dict)
print(people)