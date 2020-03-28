import pandas as pd

df1 = pd.DataFrame({'key': list('bbaca'), 'data1': range(5)})
#   key  data1
#   0   b      0
#   1   b      1
#   2   a      2
#   3   c      3
#   4   a      4

df2 = pd.DataFrame({'key': list('abd'), 'data2': range(3)})
#   key  data2
#   0   a      0
#   1   b      1
#   2   d      2

df = pd.merge(df1, df2, on='key')
print(df)
pd.concat()

