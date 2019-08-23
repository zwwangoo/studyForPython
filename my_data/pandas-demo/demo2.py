import pandas as pd
from pandas import DataFrame

print('在读取数据时，添加列名：')
columns = ['num', 'name', 'age', 'weight', 'w1', 'w2', 'w3', 'm1', 'm2', 'm3']
data = DataFrame(pd.read_csv('./data.csv', names=columns))

print(data)
print('删除全空行：')
data.dropna(how='all', inplace=True)
print(data)

print('缺失的Age列数据补全平均值：')
data['age'].fillna(data['age'].mean(), inplace=True)
print(data)

print('统一单位：')

rows_with_lbs = data['weight'].str.contains('lbs').fillna(False)
print(data[rows_with_lbs])

for index, row in data[rows_with_lbs].iterrows():
    weight = int(float(row['weight'][:3]) / 2.2)
    data.at[index, 'weight'] = '{}kgs'.format(weight)

print(data)
data.to_csv('data1.csv', index=False)
