# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 09:02:26 2017

@author: ndenefe
"""
import numpy as np
import math
import matplotlib.pylab as plt

#sigmoid

x=np.arange(-5,5+.02,0.02)
fx = 1/(1+np.exp(-x))
#gx = (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
gx = np.tanh(x)
#varification
fveri = np.zeros(len(x))#create an array of same length zeroed out
for i in range(len(x)):
    fveri[i]=1/(1+np.exp(-x[i]))
    print('i={}, verification={}'.format(i,fveri[i]==fx[i]))

fig = plt.figure()
plt.plot(x,fx,'g-',label='sigmoid')
plt.legend(loc='best')
plt.show(fig)

fig2 = plt.figure()
plt.plot(x,fx,'r-.',label='sigmoid')
plt.plot(x,gx,'b--', linewidth=2, label='tanh')
plt.legend(loc='best')
plt.savefig('test_fig2.png')
plt.show(fig2)

