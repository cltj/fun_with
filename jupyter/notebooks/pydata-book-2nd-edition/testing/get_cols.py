import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('costmanagementexport.csv')

cols = list(df.columns)
col_len, row_len = df.shape

#print("Columns: " + (str(col_len) + '\n' + "Rows: " + str(row_len)))
columns = []
count = []
for elem in cols[0:65]:
    obj = pd.Series(df[elem].drop_duplicates())
    print(elem, str(len(obj))) #, tuple(obj.values))
    columns.append(elem)
    count.append(str(len(obj)))

my_dict = dict(zip(columns, count))
df = pd.DataFrame(my_dict, index=[range(col_len)])
print(df)




