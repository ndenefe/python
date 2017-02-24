import numpy as np
#basic umpy functions: .empty(), .zeros(), .ones(), .identity() or .eye(), .diag()

np.empty(3) #.empty(generate an 'empty' array or desired shape)

np.empty((2,3))

[np.zeros(3), np.ones(4)]
np.zeros((3,4))


v=np.zeros(5)

M=np.zeros((10,5))

I=np.eye(5)

np.diag(I)

N=np.diag([1,2,3,4,5,6])
N.size
N.ndim
np.size(N)

row=10;col=4
del N
N=np.zeros((row,col))
for i in range(row):
    for j in range(col):
        N[i,j] = (i+1)*(j+i)**2

N.reshape((5,8))
N.reshape((5,8),order='F')

v = np.random.randint(1,20,6)
print('v={}'.format(v))

#v2 = v
#v2 = v[:] #this is no longer a shallow copy of v
v3=v.copy() #this is a true shallow copy of v
v3[0] =1000
print('v={}, v3={}'.format(v,v3))

#don't use this
v4 = list(v)
v4[0]=-10000
print('v={}, v4={}'.format(v,v4))

###############################################################################
#array indexing
M = np.random.rand(5,4); print(M)
M[2,1]
M[3,]
M[3,:]
M[3] #essentially M is 1-d (but labelled as 2-d)

M[:,1]
#M[,1] not working

M[1:, 2:]
M[1:4,2:]
M[1:4,2:3]