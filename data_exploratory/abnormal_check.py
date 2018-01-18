# -*- coding: utf-8 -*-D:\GitWork\Data\chapter3\demo\code\3-1_abnormal_check.py
# 3-1
'''
@ author: Amos
'''

import pandas as pd
import matplotlib.pyplot as plt

catering_sale = './data/catering_sale.xls'
data = pd.read_excel(catering_sale, index_col = u'日期')

plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

#建立图像
plt.figure()
p = data.boxplot(return_type = 'dict')
x = p['fliers'][0].get_xdata()    #‘flies’即为异常值
y = p['fliers'][0].get_ydata()

y.sort()

#用annotate添加注释
for i in range(len(x)):
    if i>0:
        plt.annotate(y[i], xy = (x[i], y[i]), xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
    else:
        plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i]+0.08,y[i]))

plt.show()
