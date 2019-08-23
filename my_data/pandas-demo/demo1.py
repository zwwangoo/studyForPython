from pandas import DataFrame

data = {
    'Chinese': [66, 95, 95, 90, 80, 80],
    'English': [65, 85, 92, 88, 90, 90],
    'Math': [None, 98, 96, 77, 90, 90]
}

df = DataFrame(data, index=['ZhangFei', 'GuanYu',
                            'ZhaoYun', 'HangZhen', 'DianWei', 'DianWei'],
               columns=['Chinese', 'English', 'Math'])

print('去除重复行:')
df = df.drop_duplicates()
print(df)

print('补全空:')
df['Math'].fillna(0, inplace=True)
print(df)

# -------
print('新增总分列:')


def total(df):
    df['Total'] = df['Chinese'] + df['English'] + df['Math']
    return df


df = df.apply(total, axis=1)
print(df)

print(df.describe())
