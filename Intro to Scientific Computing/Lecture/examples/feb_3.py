#Feb 3, lecture

#example:  find the smallest integer n such that
#1**3 + 2**3 + 3**3 + ... + n**3 < 10**6


#solution 1: use for loop

s = 0
for i in range(1, 100):
    s += i**3
    
    if (s >= 10**6):
        print('largest n=', i-1)
        s -= i**3
        break    #this is an important command to break out of loop
        #print ('i=', i)
        
print('s=',s)


#solution 2: use while loop
s=0;  i=1
while s  < 10**6 - i**3:
    s += i**3
    i += 1
print(s)    #a bug of extra n=45 which violate s <10**6



s=0;  i=1
while s  < 10**6:
    s += i**3
    i += 1
 
if (s> 10**6): s -= (i-1)**3   
print(s)    #a bug of extra n=45 which violate s <10**6


s=0;  i=1
while  i < 100:
    if (s + i**3 < 10**6):
         s += i**3 
    else:  
       break
    i += 1
    
print(s)










s=0;  i=1
while i < 100:    
    s += i**3
    if s > 10**6:
        s -= i**3
        break
    i += 1
print(s)    #this fixed the bug of extra n=45 above






#use while loop to print out all integers n such that
# 100 < n**3/n**(1/2) <10**4

n = 1
while  n < 10**4:
    if 100 < n**3/n**(0.5) < 10**4:
        print ('n=', n)
    if n**3/n**(0.5) >= 10**4:
        break
    n += 1
    

 


##find all the integers n such that
#  10**6 <= 2**2 + 4**4 + 6**6 + ... (2*n)**n <= 10**90

s = 0;
nlist = []
for i in range(2, 100, 2):  #use step length==2
    s += i**i
    if (s >= 10**6) and (s <= 10**90):
        nlist.append(i/2)
    if (s > 10**90):
        break

nlist
    
    
s = 0;
nlist2 = []
for i in range(1, 100):  #use step length==1
    s += (2*i)**(2*i)
    if (s >= 10**6) and (s <= 10**90):
        nlist2.append(i)
    if (s > 10**90):
        break

nlist2   
    
    
    
    
    
