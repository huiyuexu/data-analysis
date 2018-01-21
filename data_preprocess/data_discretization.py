# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:35:38 2018
@author: Amos
"""
#数据离散化
import pandas as pd

DATA_FILE = './data/discretization_data.xls' #参数初始化
DATA = pd.read_excel(DATA_FILE) #读取数据
DATA = DATA.loc[:, u'肝气郁结证型系数']
k = 4

#等宽离散化
d1 = pd.cut(DATA, k, labels=range(k))

#等频率离散化
w = [1.0*i/k for i in range(k+1)]
#m = DATA.describe()
#n = DATA.describe(percentiles=w)
w = DATA.describe(percentiles=w)[4:(4+k+1)]
w[0] = w[0]*(1-1e-10)
d2 = pd.cut(DATA, w, labels=range(k))

from sklearn.cluster import KMeans #引入KMeans
#一维聚类离散化
kmodel = KMeans(n_clusters=k, n_jobs=2) #建立模型
#kmodel.fit(DATA.reshape((len(DATA), 1)))  #训练模型
#c = pd.DataFrame(kmodel.cluster_centers_).sort(0)   #输出聚类中心，并且排序
#w = pd.rolling_mean(c, 2).iloc[1:] #相邻两项求中点，作为边界点
#w = [0] + list(w[0]) + [DATA.max()] #把首末边界点加上
#d3 = pd.cut(DATA, w, labels = range(k))

def cluster_plot(d, k): #自定义作图函数来显示聚类结果
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

    plt.figure(figsize=(8, 3))
    for j in range(0, k):
        plt.plot(DATA[d==j], [j for i in d[d==j]], 'o')
    plt.ylim(-0.5, k-0.5)
    return plt

cluster_plot(d1, k).show()
cluster_plot(d2, k).show()
#cluster_plot(d3, k).show()   
