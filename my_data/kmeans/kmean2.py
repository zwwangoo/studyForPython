from sklearn.cluster import KMeans
from sklearn import preprocessing
import matplotlib.pyplot as plt

import pandas as pd

data = pd.read_csv('data.csv')

# trans_x = data[['2019年国际排名', '2018世界杯']]
trans_x = data[['2019年国际排名', '2018世界杯', '2015亚洲杯']]
df = pd.DataFrame(trans_x)
min_main_scaler = preprocessing.MinMaxScaler()
trans_x = min_main_scaler.fit_transform(trans_x)
print(trans_x)
# plt.scatter(trans_x[:, 0], trans_x[:, 1])
# plt.plot()
# plt.show()

kmean = KMeans(n_clusters=3)
trans_y = kmean.fit_predict(trans_x)

result = pd.concat((data, pd.DataFrame(trans_y)), axis=1)
result.rename({0: '聚类'}, axis=1, inplace=True)
result.to_csv('data1.csv')
print(trans_x)

print(result)
