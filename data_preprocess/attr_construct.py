# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 18:54:48 2018

@author: Amos
"""
import pandas as pd

#构造线损率这个属性

inputfile= './data/electricity_data.xls' #供入供出电量数据
outputfile = './tmp/electricity_data.xls' #属性构造后数据文件

data = pd.read_excel(inputfile)
data[u'线损率'] = (data[u'供入电量'] - data[u'供出电量'])/data[u'供入电量']
data.to_excel(outputfile)
