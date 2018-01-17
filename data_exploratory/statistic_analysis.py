# -*- coding: utf-8 -*-

import pandas as pd

catering_sale = './data/catering_sale.xls'
data = pd.read_excel(catering_sale, index_col = u'日期')

print(data.describe(),'\n')
print('total: ',len(data))

data = data[(data[u'销量']>400) & (data[u'销量']<5000)]
statistics = data.describe()

s = statistics
s.loc['range'] = s.loc['max'] - s.loc['min']
s.loc['var'] = s.loc['std'] / s.loc['mean']
s.loc['dis'] = s.loc['75%'] - s.loc['25%']
 
print(statistics)
