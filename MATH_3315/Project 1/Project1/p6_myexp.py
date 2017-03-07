#
# Noah Denefe ndenefe@smu.edu 
#
#===========================================================
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
        
def myexp_pos(x, tol=10**(-10)):
    ''' Input x is nonnegative real, compute exp(x) using Taylor series '''
    s=1
    i=1
    ifact=1
    t=1
    while(abs(t)>tol):
        ifact=factorial(i)
        t=((x**i)/(ifact))
        if(t>tol):
            s+=((x**i)/(ifact))
        i+=1
        
    return s


#===========================================================
def myexp_neg(x, tol=10**(-10)):
    ''' Input x is negative real, compute exp(x) using Taylor series.
        (The three returned values exp1, exp2, exp3 are computed using
        formulas specified in the project pdf file.)
    '''
    exp1=1/(myexp_pos(-x,tol))
    exp2=0
    exp3=0





    return (exp1, exp2, exp3)


#===========================================================
if __name__=='__main__':
    import math
    import numpy as np

    tol = 10**(-12)

    for x in np.arange(0.0, 30.0, 0.5):
        myexp = myexp_pos(x, tol)
        mathexp = math.exp(x)
        absolute_error = abs(mathexp - myexp)
        relative_error = abs(mathexp - myexp)/mathexp
        print('exp({:6.2f})={:14.10e},  your_exp={:14.10e},  abs_err={:10.5e},  rel_err={:14.10e}'.
              format(x, mathexp, myexp, absolute_error,  relative_error))
        if abs(relative_error) > tol:
            print("Too large error from myexp_pos(), implementation can be wrong")


    for x in  list(np.arange(-60.0, -25.0, 2.0))+list(np.arange(-25.0, 0.)):
        (exp1, exp2, exp3) = myexp_neg(x, tol)
        mathexp = math.exp(x)
        errorV = [ abs(mathexp - expx) for expx in (exp1, exp2, exp3) ]
        print('\nexp({:6.2f})={:14.10e}'.format(x, mathexp)), 
        print('exp1={:14.10e}, exp2={:14.10e}, exp3={:14.10e}'.format(exp1,exp2,exp3))
        print('err1={:14.10e}, err2={:14.10e}, err3={:14.10e}'.format(errorV[0], errorV[1], errorV[2]))
        

##
## there is no pass or fail test in the problem, from the printed out errors above you can
## try to make sense of if your code is implemented correctly.
##
## among exp1, exp2, exp3, one of them should be consistently having large error (because 
## numerical cancelation error makes the summation scheme unreliable).  you'll need to find
## out which one is the least accurate by looking at your numerical results from the above tests.
## 

