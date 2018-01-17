# -*- coding: utf-8 -*-

import pandas as pd

catering_sale = './data/catering_sale_all.xls' #餐饮数据，含有其他属性
data = pd.read_excel(catering_sale, index_col = u'日期') #读取数据，指定“日期”列为索引列

#print(data.corr()) 
print(data.corr()[u'百合酱蒸凤爪']) #只显示“百合酱蒸凤爪”与其他菜式的相关系数
print('\n')
print(data[u'百合酱蒸凤爪'].corr(data[u'翡翠蒸香茜饺'])) #计算“百合酱蒸凤爪”与“翡翠蒸香茜饺”的相关系数
