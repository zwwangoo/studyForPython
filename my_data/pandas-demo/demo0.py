from pandas import Series, DataFrame

x1 = Series([1, 2, 3, 4])
x2 = Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
x3 = Series({'a': 1, 'b': 2, 'c': 3, 'd': 4})

print(x1)
print(x2)
print(x3)

data = {'Chinese': [89, 99, 80, 42], 'math': [99, 98, 90, 34]}
df1 = DataFrame(data)
print(df1)

df2 = DataFrame(data, index=['zhangfei', 'zhaoyun', 'liubei', 'dianwei'])
print(df2)
