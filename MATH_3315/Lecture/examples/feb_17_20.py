# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17, 20  09:07:30 2017

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
#Excise:
#plot the sigmoid function  f(x) = 1/(1 + exp(-x)) 
#for x in [-5, 5]
#

x = np.arange(-5, 5+0.02, 0.02)
fx = 1/ (1 + np.exp(-x))
gx = np.tanh(x)
fveri = np.zeros(len(x))
#varification
for i in range(len(x)):
    fveri[i] = 1 / (1 + np.exp(- x[i]))
    print('i={},  verification={}'.format(i,fveri[i] == fx[i]))

fig = plt.figure()
plt.plot(x, fx, 'g-', label='sigmoid')
plt.legend(loc='best')
plt.show(fig)


#plot everything using plt.XXXX()

fig2 = plt.figure()
plt.plot(x, fx, 'r-.', label='f(x)=1/(1+exp(-x))')
plt.plot(x, gx, 'b--', linewidth=10, label='f(x)=tanh(x)')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('function y = f(x)')
plt.savefig('test_fig2.jpg')
plt.show(fig2)



#besides np.arange(), we can use np.linspace() to construct 
#a vector 
x = np.linspace(0, 2*np.pi, 100)
#plot two subplots in one row
fig4 = plt.figure()
plt.subplot(1,2, 1)
fx1 = np.sin(x)
plt.plot(x, fx1)
plt.subplot(1,2, 2)
fx2 = np.sin(x*2)
plt.plot(x, fx2)
plt.show(fig4)

x = np.linspace(0, 2*np.pi, 100)
#plot two subplots in one column
fig5 = plt.figure()
#plt.subplot(2,1, 1)
plt.subplot(2,1, 2)
fx1 = np.sin(x)
plt.plot(x, fx1)
#plt.subplot(2,1, 2)
plt.subplot(2,1, 1)
fx2 = np.sin(x*2)
plt.plot(x, fx2)
plt.show(fig5)


row = 2; col =3
for i in range(1, row*col+1):
    fx = np.sin(i*x)
    plt.subplot(row, col, i)
    plt.plot(x, fx)
plt.show()


