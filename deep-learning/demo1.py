import os
import cv2
from keras import backend as K
from keras.layers import (
    Conv2D, MaxPooling2D, BatchNormalization, Activation,
    Dropout, Dense, Flatten, UpSampling2D,
    Input, add)
from keras.models import Model, Sequential, load_model
import numpy as np

girl = cv2.imread('girl.jpg')


def createmode():
    model = Sequential()

    # 加入一个卷积层，filter数量为3,卷积核size为(3, 3)
    model.add(Conv2D(3, (3, 3), input_shape=girl.shape, name='conv_1'))
    # 加入一个pooling层，size为(3, 3)
    model.add(MaxPooling2D(pool_size=(3, 3)))
    # 加入激活函数 'Relu', 只保留大于0的值
    model.add(Activation('relu'))

    model.add(Conv2D(3, (3, 3), input_shape=girl.shape, name='conv_2'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Activation('relu'))

    model.add(Conv2D(3, (3, 3), input_shape=girl.shape, name='conv_3'))

    model.add(Conv2D(3, (3, 3), input_shape=girl.shape, name='conv_4'))
    model.add(Activation('relu'))

    model.add(Flatten())  # 把上层输出平铺
    model.add(Dense(8, activation='relu', name='dens_1'))  # 加入全连接层，分为8类

    model.save_weights('girl.h5')


def visualize(img):
    img = np.squeeze(img, axis=0)
    max_img = np.max(img)
    min_img = np.min(img)
    img = img - (min_img)
    img = img / (max_img - min_img)
    img = img * 225
    cv2.imwrite(
        'layer1_noreshape_filter{}_{}x{}.jpg'.format(
            filter1, ke_width, ke_height),
        img)


if not os.path.exists('girl.h5'):
    createmode()

model2 = Sequential()
ke_width = 3
ke_height = 3
filter1 = 3

model2.add(Conv2D(filter1, (ke_width, ke_height),
                  input_shape=girl.shape, name='conv_1'))
model2.add(MaxPooling2D(pool_size=(3, 3)))
model2.add(Activation('relu'))
model2.load_weights('girl.h5', by_name=True)

girl_batch = np.expand_dims(girl, axis=0)
conv_girl = model2.predict(girl_batch)
visualize(conv_girl)
