import PIL.Image as image
import numpy as np
from sklearn import preprocessing
from sklearn.cluster import KMeans


def load_path(path):

    f = open(path, 'rb')
    img = image.open(f)
    data = []
    width, height = img.size
    for x in range(width):
        for y in range(height):
            a, b, c = img.getpixel((x, y))
            data.append([a, b, c])

    f.close()
    mm = preprocessing.MinMaxScaler()
    data = mm.fit_transform(data)
    return np.mat(data), width, height


img, width, height = load_path('wx.jpg')
kmean = KMeans(n_clusters=2)
labels = kmean.fit_predict(img)
labels = labels.reshape([width, height])
pic_mark = image.new('L', (width, height))
for x in range(width):
    for y in range(height):
        pic_mark.putpixel((x, y), int(256/(labels[x][y]+1))-1)
pic_mark.save('wx1.jpg', 'JPEG')
