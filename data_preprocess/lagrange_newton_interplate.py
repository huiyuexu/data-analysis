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
#异常值过滤，变为空值
data['销量'][data['销量']<400 | data['销量']>5000] = None

#自定义列向量插值函数
def polyinterp_column(s, n, k=5):
    y = s 
    
    

    
for i in data.columns:
    for j in range(len(data)):
        if data[i].isnull():
            data[i][j] = polyinterp_column(data[i], j)

data.to_excel(outputfile)
