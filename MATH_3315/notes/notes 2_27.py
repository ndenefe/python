# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 09:01:11 2017

@author: ndenefe
"""
import numpy as np



def dotprod(u, v):
    lenu = len(u)
    s=0
    if(len(v)!=lenu):
        print('length of vectors are different\n')
        return None
    for i in range(0,lenu):
        s += u[i]*v[i]
    return s
    
n=1000
u=np.random.rand(n)
v=np.random.randn(n)

print(dotprod(u,v))