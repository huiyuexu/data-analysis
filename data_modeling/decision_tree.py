# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 22:34:51 2018

@author: Amos
"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.tree import export_graphviz as to_graphviz
from sklearn.externals.six import StringIO

filename = "./data/sales_data.xls"
data = pd.read_excel(filename, index_col=u'序号')

#数据变换为类别标签
data[data == u'高'] = 1
data[data == u'是'] = 1
data[data == u'好'] = 1
data[data != 1] = -1
x = data.iloc[:,:3].astype(int)
y = data.iloc[:,3].astype(int)

#建立并训练决策树模型，基于信息熵
dtc = DTC(criterion='entropy')
dtc.fit(x, y)

with open("./tmp/tree.dot", 'w') as f:
    f = to_graphviz(dtc, feature_names = x.columns, out_file= f)
