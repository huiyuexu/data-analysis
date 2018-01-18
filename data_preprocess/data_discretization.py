# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 17:36:54 2018

@author: Amos
"""
from scipy.io import loadmat

inputfile= './data/leleccum.mat' #提取自Matlab的信号文件
mat = loadmat(inputfile)
signal = mat['leleccum'][0]



