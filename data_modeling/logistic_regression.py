# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 19:36:10 2018

@author: Amos
"""
#某银行在降低贷款拖欠率的数据进行回归建模
#逻辑回归 自动建模
import pandas as pd
import numpy

#参数初始化
filename = './data/bankloan.xls'
data = pd.read_excel(filename)

x = data.iloc[:, :8].as_matrix()
y = data.iloc[:, 8].as_matrix()

from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR 


lr = LR() #建立逻辑货柜模型
lr.fit(x, y) #用筛选后的特征数据来训练模型
print(u'逻辑回归模型训练结束。')
print(u'未经过筛选特性模型的平均正确率为：%s' % lr.score(x, y))

#建立随机逻辑回归模型
rlr = RLR() #帅选变量
rlr.fit(x, y)
#rlr.get_support()   #获取特征筛选结果，也可以通过.scores_方法获取各个特征的分数
selected_col = numpy.append(rlr.get_support(),[False])
print(u"通过随机逻辑回归模型筛选特征结束")
print(u"有效特征为：%s" % ",".join(data.columns[selected_col]))
x = data[data.columns[selected_col]].as_matrix()    # 筛选好特征

lr = LR() #建立逻辑货柜模型
lr.fit(x, y) #用筛选后的特征数据来训练模型
print(u'逻辑回归模型训练结束。')
print(u'模型的平均正确率为：%s' % lr.score(x, y)) #给出模型的平均正确率，本例为81.4%
