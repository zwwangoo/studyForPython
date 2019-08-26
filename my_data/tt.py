from matplotlib import pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

digits = load_digits()
data = digits.data

print(data)
print(digits.images[0])
plt.gray()
plt.imshow(digits.images[0])
plt.show()

train_x, test_x, train_y, test_y = train_test_split(
    data, digits.target, test_size=0.25, random_state=33)

# Z-Score 规范化
ss = preprocessing.StandardScaler()
train_ss_x = ss.fit_transform(train_x)
test_ss_x = ss.transform(test_x)

knn = KNeighborsClassifier()
knn.fit(train_ss_x, train_y)
predict_y = knn.predict(test_ss_x)
print('KNN准确率: %.4lf' % accuracy_score(predict_y, test_y))
