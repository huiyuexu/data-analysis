# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 17:36:54 2018
@author: Amos
"""

#利用小波变换进行数据分析

from scipy.io import loadmat

inputfile= './data/leleccum.mat' #提取自Matlab的信号文件
mat = loadmat(inputfile)
signal = mat['leleccum'][0]

#导入PyWavelets
import pywt
coeffs = pywt.wavedec(signal, 'bior3.7', level=5)
#返回结果为level+1个数字，第一个数组为逼近系数数组，后面的依次是细节系数数组i
