# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 09:25:59 2017

@author: 26454302
"""

#numpy

import numpy as np

v = np.zeros(5)

M = np.zeros((10, 5))

I = np.eye(5)

np.diag(I)

N = np.diag([1,2,3,4,5, 6])
N.size
#N.dim
np.size(N)

row=10; col=4
del N
N = np.zeros((row, col))
for i in range(row):
    for j in range(col):
        N[i,j] = (i+1)*(j+1)**2
        
N.reshape((5,8))       
N.reshape((5,8), order='F')  