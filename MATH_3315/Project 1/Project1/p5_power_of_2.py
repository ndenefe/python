#
# Noah Denefe ndenefe@smu.edu
# (as in professional public domain code. just in case someone see your 
#  brilliant code and want to contact you, e.g. to offer you a job. 
#  no joking here, this problem is likely the hardest in Project 1)
#
#===========================================================

def find_power_of_2(n1, n2):
    '''The inputs are two integers n1 <= n2, find all the numbers in [n1, n2] that 
       are power of 2, return them in increasing order in a list.

       Special notes:  
       (1) either n1 or n2 or both can be negative! 
       (2) if you use loop with step=2, then be careful about -1 and 1, they are power_of_2. 
    ''' 
    L1=[]
    x=0
    for i in range(n1+1,n2+1):
        x=abs(i)**.5        
        if type(x) is int:
            L1.append(i)
    return L1


#===================================================================
def  is_power_of_2 (n):   
    ''' return true if n is a power of 2, and False if not '''
    return (abs(n)**.5==int(abs(n)**.5))



#===================================================================
def find_power_of_2_fast(n1, n2):   #a fast way to find power of 2 
    '''The inputs are two integers n1 < n2, find all the numbers in [n1, n2] that 
       are power of 2, return them in increasing order in a list.
    ''' 
    L1=[]
    x=0
    for i in range(n1+1,n2+1):
        x=abs(i)**.5        
        if type(x) is int:
            L1.append(i)
    return L1


#===================================================================
def verification(pn1, pn2):
    if pn1>pn2: pn1, pn2 = pn2, pn1

    DEBUG = True
    #DEBUG = False
    global total_failcount

    #generate the exact power_of_2 according to the input powers
    #(here if pn1<0, then construct -2**abs(pn1) instead of 2**pn1; same for pn2) 
    if pn2<=0:
        pow_exact=[-2**abs(i) for i in range(pn1, pn2+1) ]
    elif pn1<=0:
        pow_exact=[-2**abs(i) for i in range(pn1,1) ] + [ 2**i for i in range(0,pn2+1)]
    else: #0 < pn1 <= pn2
        pow_exact=[ 2**i for i in range(pn1, pn2+1) ]

    #test cases: n1<=n2<=0,  n1<=0<=n2, 0<=n1<=n2. (these are controlled by the signs of pn1, pn2)
    #boundary cases should also be tested: (e.g., one of n1, n2, or both, are power_of_2) 

    n1=pow_exact[0];  n2=pow_exact[-1]
    if DEBUG:
        print('\n\n n1={}, pn1={};   n2={}, pn2={}'.format(n1, pn1, n2, pn2))        
        print("power_of_2 for this test: {}".format(pow_exact))

    TEST=True    
    your_pow2 = find_power_of_2(n1, n2);
    if pow_exact == your_pow2:
        print("Both end-points are power_of_2 case: Passed!")
    else:
        print("Both end-points are power_of_2 case: ****** failed ******"); 
        TEST=False;  total_failcount+=1
        if DEBUG:
            print("power_of_2 you got  : {}".format(your_pow2))

    your_pow2 = find_power_of_2(n1, n2+1);
    if is_power_of_2(n2+1): 
        pow_exactR = list(pow_exact) + [n2+1]
    else:
        pow_exactR = list(pow_exact)
    if pow_exactR == your_pow2:
        print("Left end-point is power_of_2 case: Passed!")
    else:
        print("Left end-point is power_of_2 case: ****** failed ******"); 
        TEST=False;  total_failcount+=1
        if DEBUG:
            print("power_of_2 you got  : {}".format(your_pow2))

    your_pow2 = find_power_of_2(n1-1, n2);
    if is_power_of_2(n1-1): 
        pow_exactL = [n1-1] + list(pow_exact)
    else:
        pow_exactL = list(pow_exact)
    if pow_exactL == your_pow2:
        print("Right end-points is power_of_2 case: Passed!")
    else:
        print("Right end-points is power_of_2 case: ****** failed ******"); 
        TEST=False;  total_failcount+=1
        if DEBUG:
            print("power_of_2 you got  : {}".format(your_pow2))

    your_pow2 = find_power_of_2(n1-1, n2+1);
    pow_exactLR = list(pow_exact)
    if is_power_of_2(n1-1):  pow_exactLR = [n1-1] + pow_exactLR
    if is_power_of_2(n2+1):  pow_exactLR = pow_exactLR + [n2+1]
    if pow_exactLR == your_pow2:
        print("Neither end-points are power_of_2 case: Passed!")
    else:
        print("Neither end-points are power_of_2 case: ****** failed ******"); 
        TEST=False;  total_failcount+=1
        if DEBUG:
            print("power_of_2 you got  : {}".format(your_pow2))

    return TEST

####################################################################
if __name__=='__main__':

    import numpy as np
    from timeit import default_timer 

    #delete the min, max variables from problem 2 (if you use the same spyder interface).
    #not necessary if you use python from command line, or use a python GUI with fresh start 
    try:
        del min, max  
    except:
        pass

    repeat=10
    TESTS={}
    failcount=0;  total_failcount=0

    for it in range(repeat):
        #test cases:  n1<n2<0, n1<=0=<n2, 0<n1<n2
        #test n1<n2<=0 cases
        pn12=np.random.randint(-18, 0, size=(2,1))
        pn1=min(pn12)[0]; pn2=max(pn12)[0]; 
        TESTS[(it,1)]=verification(pn1, pn2)

        #test n1<=0<=n2 cases
        pn1=np.random.randint(-17, -1)
        pn2=np.random.randint(1, 8)
        TESTS[(it,2)]=verification(pn1, pn2)       

        #test 0<=n1<=n2 cases
        pn1=np.random.randint(0, 10)
        pn2=np.random.randint(pn1, 17)
        TESTS[(it,3)]=verification(pn1, pn2)  


    for key in TESTS:
        if TESTS[key]==False: failcount +=1

    print("\n====== For all {} tests,  failcount={},  total_failcount={} ======"
          .format(3*repeat*4, failcount, total_failcount))
    if failcount==0:
        print("Congratulations for passing all tests for Problem 5!\n")
    else:
        print("\n****** Need to debug your code further ******\n")



    #for the second part of this problem, finding power_of_2 in range [1, 10**32]
    #will be OVERLY SLOW if you do not get the fast way solving this problem.
    #for this regard, you only need to find all power_of_2 in [1, 10**8], 
    #if you can go up to range(1, 10**32), you will get bonus points for this problem

    n1=1; n2=10**8 
    print("Now try to find all power_of_2 in [1, 10**8], it will take a long while")
    print("if you use a fixed step iteration.")
    print("Change the range to [1, 10**7] if your code takes too long to run ...")
    tstart = default_timer()
    #this will take quite a while for large n2-n1
    power2= find_power_of_2(n1, n2); print(power2)
    elapse1 = default_timer() - tstart
    print('elapsed time = %.5e\n' % elapse1)


    FAST_METHOD_DONE=False
    #FAST_METHOD_DONE=True   #uncomment this line if you do the fast method

    if FAST_METHOD_DONE:
        #the fast method should finish in a blink, it is exponentially faster than looping from 
        #n1 to n2 with a fixed step (usually it is easily 10**4 fold faster even for range(1,10**8)
        #the larger the range, the more significant speed of gain.)
        tstart = default_timer()
        powerf2 = find_power_of_2_fast(n1, n2);  print(powerf2)
        elapse2 = default_timer() - tstart

        print('elapsed time fast = %.5e,   fold_of_speed_gain=%.3e \n' % (elapse2,  elapse1/elapse2))   

        print('len(power2)={},  len(powerf2)={}'.format(len(power2), len(powerf2)))

        #if you implement the fast way correctly, it should be easy to go up to an astronomical number
        #such as 10**50
        powerf3 =find_power_of_2_fast(0, 10**50); 
        print(powerf3); print('len(power)=', len(powerf3))
