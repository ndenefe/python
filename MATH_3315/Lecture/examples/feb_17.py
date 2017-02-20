# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 09:07:30 2017

@author: 26454302
"""
import numpy as np
import math
import matplotlib.pylab as plt


v = [ x * np.pi/8  for x in range(0,17) ]
v
v2 = [ x * np.pi/100  for x in range(0,200+1) ]

#math.sin(v)  #this leads to an erro
sinv = np.sin(v)
sinv2 = np.sin(v2)

fig, aix=plt.subplots()

#aix.plot(sinv, '-*')
aix.plot(sinv2)
fig.show()
#fig=plt.plot(sinv)
#fig.show()
#plt.plot(sinv).show()

fig2, aix2=plt.subplots()

#aix.plot(sinv, '-*')
#aix2.plot(np.cos(v2))
#aix2.plot(v2, np.cos(v2), '-x')
aix2.plot(v2, np.sin(v2), 'r-.',  v2, np.cos(v2), 'y-x')
fig2.show()


v2 = np.array(v2)
fig3, aix3=plt.subplots()
#aix2.plot(v2, np.cos(v2), '-x')
aix3.plot(v2, np.sin(v2), 'r-.', label='sin(x)')
aix3.plot(v2, np.cos(v2), 'y-x', label='cos(x)')
aix3.plot(v2, np.sin(v2**2), 'c--', label='sin(x**2)')
aix3.legend(loc='best')
fig3.show()


a = [1, 2, 5]
aa = np.array(a)
a*3      #this duplicates a 3 times
aa*3    #this multiply each item in aaby 3

a**2   #this couase an error (cannot square a list)
aa**2  #this squares each item in aa

#



