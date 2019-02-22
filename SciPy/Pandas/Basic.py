import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print df

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print df2
print df2.describe()
# Transposing df
print(df.T)

df.sort_index(axis=1, ascending=False)
print df

print(df.sort_values(by='B'))
print(df['A'])
print(df.loc[:, ['A', 'B']])
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print df2[df2['E'].isin(['two', 'four'])]
df.to_csv("testdata.csv")

df3 = pd.read_csv("testdata.csv")
print df3