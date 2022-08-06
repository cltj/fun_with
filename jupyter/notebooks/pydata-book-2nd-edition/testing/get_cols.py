import pandas as pd

df = pd.read_csv('costmanagementexport.csv')

cols = list(df.columns)
col_len, row_len = df.shape

#print("Columns: " + (str(col_len) + '\n' + "Rows: " + str(row_len)))

for elem in cols[0:65]:
    obj = pd.Series(df[elem].drop_duplicates())
    if len(obj) > 1:
        print(elem + ': ' + str(len(obj)), tuple(obj.values))
    else:
        print('Only one value')

