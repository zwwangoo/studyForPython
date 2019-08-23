import pandas as pd
from pandas import DataFrame

df = DataFrame(pd.read_csv('./food.csv'))
print(df)

df['food'] = df['food'].str.lower()
df = df.dropna()
print(df)
