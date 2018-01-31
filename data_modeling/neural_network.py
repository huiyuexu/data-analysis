# -*- coding: utf-8 -*-
#使用神经网络算法预测销量高低

import pandas as pd

inputfile = './data/sales_data.xls'
data = pd.read_excel(inputfile, index_col = u'序号')

data[data == u'高'] = 1
data[data == u'是'] = 1
data[data == u'好'] = 1
data[data != 1] = -1
x = data.iloc[:,:3].astype(int)
y = data.iloc[:,3].astype(int)

from keras.models import Sequential
from keras.layers.core import Dense, Activation

#建立模型
model = Sequential();
model.add(Dense(input_dim = 3, output_dim = 10))
model.add(Activation('relu')) #用relu函数作为激活函数，能够大幅提供准确度
model.add(Dense(input_dim = 10, output_dim = 1))
model.add(Activation('sigmoid')) #由于是0-1输出，用sigmoid函数作为激活函数

#编译模型：
#由于我们做的是二元分类，所以我们指定损失函数为binary_crossentropy，以及模式为binary
#另外常见的损失函数还有mean_squared_error、categorical_crossentropy等，请阅读帮助文件。
#求解方法我们指定用adam，还有sgd、rmsprop等可选
model.compile(loss = 'binary_crossentropy',
              optimizer = 'adam')

model.fit(x, y, epochs = 100, batch_size = 10) #训练模型，学习一千次
yp = model.predict_classes(x).reshape(len(y)) #分类预测

from cm_plot import *
cm_plot(y, yp).savefig('./data/neiral_network.png')
