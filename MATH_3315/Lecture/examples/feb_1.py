# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 09:01:49 2017

@author: 26454302
"""

#find the sum of 1+2+3+...+10**6
s=0
for i in range(1, 10**6+1):
    s+=i
    #print('i=', i)
    
print('sum=',s)


s6=0
for item in range(6, 1000, 6):
    s6 += item
   
print('sum6=', s6)   

s66=0
for i in range(1, 1000):
    if i % 6 == 0:
        s66 += i
        print('i=', i)

print('sum66=', s66)

#still using step length =1, find the sum of even number 
#and sum of odd number for integers in [100, 10**6] in one loop

sumeven = 0;   sumodd=0
for ii  in range(100, 10**6+1):
    if ii%2 !=0:
        sumodd += ii
    else:
        sumeven += ii
        
print("sumeven=", sumeven)
print("sumodd=", sumodd)