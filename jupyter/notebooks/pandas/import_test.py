import numpy as np
import pandas as pd

# data = 2,3,4
index = 10,11,12

# test = pd.Series(data, index=index)

# print(test)

# A series (one-dimensional array) can hold any value

val1= 1,2,3
val2 =[4,5,6]
val3 = "Nope"
val4 = {"key1":"value1","key2":"value2"}

s1 = pd.Series(val1, index=index)
s2 = pd.Series(val2)
s3 = pd.Series(val3)
s4 = pd.Series(val4)

print(s1,s2,s3,s4)