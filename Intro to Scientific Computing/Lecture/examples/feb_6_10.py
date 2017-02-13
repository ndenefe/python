# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 -- 10

"""

#exercise: find all points in 2-dim plane with integer coordinates 
#that are inside the region (x-2)**2 + (y-3.5)**2 <=25

pL=[]
for x in range(-5, 10):
    for y in range(-5, 10):
        if (x-2)**2 + (y-3.5)**2 <= 25:
            pL.append((x,y))
            
print(len(pL))
print(pL)



def  cubic_sum(n):
    s =0
    for i in range(1, n+1):
        s += i**3
    return s


#find the largetst n such that s(n)<10**6
for n in range(1000):
    print('n=', n)
    if cubic_sum(n) >= 10**6:
            print('maxim n=', n-1)
            break        
    
    

#return max of a float list
def mymax(L):
    tmp = L[0]
    for item in L[1:]:
        if item > tmp:
            tmp = item
            
    return tmp



    
#exercise:  find all integers (n1, n2) such that
# n1**2 + (n1+2)**2 + (n1+4)**2 + ... + n2**2  are within
# 10**3 to 10**6  (these bounds may change, need to design your code in a better way
#                  so that changes in the bounds can be easily incorporated without 
#                  lots of change to your code)
# 
# assume n1< n2, and n1 and n2 are both odd or both even
#

def  sum(n1, n2, lowb=10**3, upperb=10**6):
    s=0
    for i in range(n1, n2+2, 2):    
        s += i**2
    
    #return more than 1 value: make the function provide more info to its caller
    if lowb <= s <= upperb:  
      return  (True, s)
    else: 
      return (False, s)
    

num2=[];  
LOW=100; UPP=10**7   #note the convenience of using variables over using hard-numbers: 
                     #you do NOT need to change the many places where the same number reappear.
                     #(if you use a same hard-number in many places, during update, if you forget 
                     #to change one place, your code may not work as expected. but if you use
                     #a variable to store the same hard-number, you only need to change the
                     #variable assignment, and its new value will be broadcast to its corresponding places) 
for n1 in range(1,  int(UPP**0.5)+1):   
    for n2 in range(n1+2, int(UPP**0.5)+1, 2):
        (in_out, s) = sum(n1, n2, lowb=LOW, upperb=UPP)
        if  in_out:  num2.append((n1,n2))
        if s > 10**6: break

print(num2)
#num2==num


#
#example of receiveing values from a function
#
def  tst(x, pow=1):
    return (x**pow, 2*x**pow, 3*x**pow)

L=[]; L2=[]
for _ in range(1,10):
    tmp = tst(_, pow=2)
    L.append(tmp)
    L2.append((tmp[0], tmp[-1]))

print(L)
print(L2)


L=[]; L2=[]
for _ in range(1,10):
    t1, t2, t3 = tst(_, pow=2)
    L.append((t1, t2, t3))
    L2.append((t1, t3))

print(L)
print(L2)


#test (this leads to an error!!)
t0, t1 = tst(1, pow=0)



#        
#copy  (a true shallow copy, or no copy)
#  
L = [1, 2, 6, 10, 'aaa']
L2 = L         #note: this is not a true copy!!
L2 == L
L2 is L        #L2 is just the same as L
L2[0]= True
print('L2=', L2)
print(L)       #changing L2 will be the same as changing L
L is L2  
    
L = [1, 2, 6, 10, 'aaa'] 
L3 = L.copy()   #this is a true (shallow) copy
L3==L           #True, they have the same value
L3 is L         #False, since L3 and L point to different memories (references)
L3[1] =False
print('L3=', L3)   
print(L)       #changing L3 does not affect L
    
