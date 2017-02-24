# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import math
import matplotlib.pylab as plt

x = np.linspace(0, 2*np.pi, 100)
row=2; col=3
for i in range(1,row*col+1):
    fx=np.sin(i*x)
    plt.subplot(row, col, i)
    plt.tight_layout()
    plt.title('y= sin({}*x)'.format(i)) #need some hacking
    plt.plot(x,fx)   #to make the space between subplots Larger
plt.show()

a=-10;b=2;n=100
x=np.linspace(a, b, n)
fig=plt.figure()
plt.plot(x, np.exp(x),'r-.',lw=5, label='exp(x)')
plt.plot(x, np.exp(5*x),'g-',lw=6, label='exp(5x)')
plt.plot(x, np.exp(10*x),'b:',lw=2, label='exp(10x)')
plt.legend(loc='best')
plt.savefig('fig.png')
plt.show()

fig2=plt.figure()
plt.semilogy(x, np.exp(x),'r-.',lw=5, label='$f=e^x$')
plt.semilogy(x, np.exp(5*x),'g-',lw=6, label='$f=e^{5x}$')
plt.semilogy(x, np.exp(10*x),'b:',lw=2, label='$f=e^{10x}$')
plt.xlabel('x');plt.ylabel('y=f(x)')
plt.legend(loc='best')
plt.savefig('fig_semilogy.png')
plt.show(fig2)

#explore pl.semilogx() and plt.LogLog() after class
#also, check plt.fplot() and plt.bar()

###############################################################################
#basic umpy functions: .empty(), .zeros(), .ones(), .identity() or .eye(), .diag()

np.empty(3) #.empty(generate an 'empty' array or desired shape)

np.empty((2,3))

[np.zeros(3), np.ones(4)]
np.zeros((3,4))


v=np.zeros(5)

M=np.zeros((10,2))

I=np.eye(5)

np.diag(I)

N=np.diag([1,2,3,4,5,6])
N.size
#N.dim
np.size(N)

row=10;col=4
del N
N=np.zeros((row,col))
for i in range(row):
    for j in range(col):
        N[i,j] = (i+1)*(j+i)**2

N.reshape((5,8))