import numpy as np
import pandas as pd

data = 2,3,4,5,6,7
index = 10,11,12, 16, 17 ,18

s = pd.Series(data, index=index)

print(s)