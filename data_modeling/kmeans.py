# -*- coding: utf-8 -*-

# 使用K-Means算法聚类消费行为特征数据
import pandas as pd
from sklearn.cluster import KMeans

k = 3 #聚类的类别
iteration = 5 #最大循环次数

inputfile = './data/consumption_data.xls'
outputfile = './tmp/out_consumption_data.xls'
#读取并标准化数据
data = pd.read_excel(inputfile)
data_zs = 1.0*(data - data.mean())/data.std()

#分为K类，并发数
model = KMeans(
        n_clusters=k, n_jobs=1, max_iter = iteration) 
#开始聚类
model.fit(data_zs)

#聚类结果
r1 = pd.Series(model.labels_).value_counts() #统计各个类别的数目
r2 = pd.DataFrame(model.cluster_centers_) #找出聚类中心
#横向连接（0是纵向），得到聚类中心对应的类别下的数目
r = pd.concat([r2, r1], axis=1)
r.columns = list(data.columns) + [u'类别数目']
#print(r)

#详细输出原始数据及其类别
r_detail = pd.concat(
        [data, pd.Series(model.labels_, index=data.index)], axis=1)
r_detail.columns = list(data.columns) + [u'聚类类别']
#print(r_detail)

'''
#自定义作图函数
def density_plot(data):
    import matplotlib.pyplot as plt
    #用来正常显示中文标签和负号
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    p = data.plot(
            kind='kde', linewidth = 2,
            subplots = True, sharex = False)
    [p[i].set_ylabel(u'密度') for i in range(k)]
    plt.legend()
    return plt

#作概率密度图
fig_output = './tmp/kmeans_pd_'
for i in range(k):
    data_r = data[r_detail[u'聚类类别'] == i].iloc[:, 1:]
    density_plot(data_r).savefig(u'%s%s'%(fig_output, i))
'''

#对kmeans结果可视化展示
from sklearn.manifold import TSNE

tsne = TSNE()
#数据降维度
tsne.fit_transform(data_zs)
tsne = pd.DataFrame(tsne.embedding_, index = data_zs.index)

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

#不同类别用不同颜色和样式绘图
d = tsne[r_detail[u'聚类类别'] == 0]
plt.plot(d[0], d[1], 'r.')
d = tsne[r_detail[u'聚类类别'] == 1]
plt.plot(d[0], d[1], 'go')
d = tsne[r_detail[u'聚类类别'] == 2]
plt.plot(d[0], d[1], 'b*')
plt.show()
