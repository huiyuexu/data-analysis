#-*- coding: utf-8 -*-

import pandas as pd

s = pd.Series([1,2,3], index=['a', 'b', 'c'])
d = pd.DataFrame([[1,2,3], [3,4,5]],columns = ['a','b','c'])
ds = pd.DataFrame(s)

print(d.head())
print(d.describe())

print(s)
