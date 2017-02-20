# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 09:08:40 2017

@author: 26454302
"""

#string construction

A=123;  B="  M  ";   C="@#$"
str1 = str(A)+B+C
str1 = str(A)+'+'+B +"+" +C

str21= "+".join([str(A), B, C])
str22= ",".join([str(A), B, C]); print(str22)

str3 = '{}+{}+{}'.format(A, B, C); print(str3)
str32 = '{}{}{}{}{}'.format(A, '+', B, '+', C); print(str32)


#python style .format()

A=['a', 'd', True];  B=(1, 5, 9)

strL = "A={}, B={}".format(A, B); print(strL)
#this is the same as
print("A={}, B={}".format(A, B))

import math
print("pi/10**9 = {}, e*100 = {}".format(math.pi*10**-9, math.e*100))
print("pi/10**9 = {:.15f}, e*100 = {:.7e}".format(math.pi*10**-9, math.e*100))



##on screen input
Ainput = input("input a list")
type(Ainput)

Bin = input(' input an integer ')
type(Bin)

Ainput = eval(input("input a list "))
type(Ainput); print(Ainput)

Bin = eval(input(' input an integer '))
type(Bin); print(Bin)



#input output from/to files
#fileheader 
fh = open('mytest.txt', 'w')
#fh.write('line 1st')
n = 100
for i in range(1, n+1):
    linestr = "line {}; {}\n".format(i,  (i, i**2, i**3))    
    fh.write(linestr)
    
fh.close()


#read from the file, and print each line on screen
fhr = open('mytest.txt', 'r')
for line in fhr:
    #print(line)  #try to see if you can remove the linebreak in screen output
    linestr = line.replace('\n', '') 
    #print(linestr)  #removes the line break
    Lst = linestr.split(',')   
    print( int(Lst[0].split('(')[-1]), int(Lst[1]), int(Lst[2].split(')')[0]))
fhr.close()



