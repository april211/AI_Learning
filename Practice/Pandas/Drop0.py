import pandas as pd
import numpy as np



""" df = pd.DataFrame(np.arange(12).reshape(3, 4),
                  columns=['A', 'B', 'C', 'D'])
print(df)


print(df.drop(['B', 'C'], axis=1))

print(df.drop(columns=['B', 'C']))

print(df['D'])
 """

df = pd.read_csv("Practice\\Pandas\\bike.csv", index_col='datetime')
