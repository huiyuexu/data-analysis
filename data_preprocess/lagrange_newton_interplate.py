# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 11:25:38 2018

@author: Amos
"""

import pandas as pd
from scipy.interpolate import lagrange

inputfile = './data/catering_sale.xls' #销量数据路径
outputfile = './tmp/sales.xls' #输出数据路径

data = pd.read_excel(inputfile)
#data[u'日期'].to_excel('./tmp/sales0.xls')
#异常值过滤，变为空值
#null_raw = list((data['销量']<400) | (data['销量']>5000))
#data.loc[:, '销量'][(data['销量']<400) | (data['销量']>5000)] = None
data.loc[(data['销量']<400) | (data['销量']>5000), '销量'] = None
#data.to_excel('./tmp/sales1.xls')

#自定义列向量插值函数
def polyinterp_column(s, n, k=5):
    y = s [list(range(n-k, n)) + list(range(n+1, n+1+k))]
    y = y[y.notnull()]    #剔除空值
    return lagrange(y.index, list(y))(n)    #插值并返回结果

for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            #data[i][j] = polyinterp_column(data[i], j)
            data.loc[j, [i]] = polyinterp_column(data[i], j)

data.to_excel(outputfile)
