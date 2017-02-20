# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 09:15:22 2017

@author: 26454302
"""

#list comprehension  (a quick way to generate a list from an iterable)

#L = range(0.1, 1, 0.1)  #non int in range not allowed
Lit = tuple(range(1, 10, 1)); print(Lit)
L = [ _*.1  for _ in Lit]; print(L)


D = { 1: 'A', 2: 'BB', 3: 'CCC'}

LD = [ _ for _ in  D]; print(LD)  #default to iterate over keys
LDk = [ _ for _ in  D.keys()]; print(LDk)
LDv = [ _ for _ in  D.values()]; print(LDv) 

# 
#

L2d = [(x, y) for x in range(2, 13) for y in range(2, 9)]

import math
XYZ=range(0, 10)
L3d= [(x, y, z) for x in XYZ for y in XYZ for z in XYZ]
L3df = [(math.exp(-x), math.log(1+y), math.exp(z**2)) for x in XYZ for y in XYZ for z in XYZ]

L = []
for x in XYZ:
    for y in XYZ:
        for z in XYZ:
            #L.append((x,y,z))
            L.append((math.exp(-x), math.log(1+y), math.exp(z**2)))              

L == L3df


#lambda function

f = lambda x:  x**2
type(f)
f(10)
f(.2)

g = lambda x, y :  (x**2, y**(1/2))
type(g)
g(2, 9)   


g3 = lambda x, y, z :  (x**2, y**(1/2), x+y +z )
type(g3)
g3(2, 9, 10)    


gL = lambda x, y, z :  [ x, y, z]
type(gL)
gL([2, 9, 10], True, 'AAA')    

    
    






