# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 16:14:38 2018

@author: Amos

规范化：归一化
"""

import pandas as pd
import numpy as np

datafile = './data/normalization_data.xls'
data = pd.read_excel(datafile, header = None)

data_n1 = (data - data.min())/(data.max() - data.min())    #最小-最大规范化
data_n2 = (data - data.mean())/data.std()                  #零-均值规范化
data_n3 = data/10**np.ceil(np.log10(data.abs().max()))    #小数定标规范化

print(data_n1)
print(data_n2)
print(data_n3)
