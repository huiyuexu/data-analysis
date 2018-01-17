# -*- coding: utf-8 -*-

#帕累托分析
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

dish_profit = './data/catering_dish_profit.xls'
data = pd.read_excel(dish_profit, index_col = u'菜品名')

data = data[u'盈利'].copy()
data.sort_index(ascending = False)

plt.figure()
data.plot(kind='bar')    #柱状图
plt.ylabel(u'盈利(元)')

p = 1.0*data.cumsum()/data.sum()
p.plot(color = 'r', secondary_y = True, style = '-o',linewidth = 2)    #线
#添加注释，即85%处的标记。这里包括了指定箭头样式。
plt.annotate(format(p[6], '.4%'), \
             xy = (6, p[6]), \
             xytext=(6*0.9, p[6]*0.9), \
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2")) 
plt.ylabel(u'盈利（比例）')

plt.show()
