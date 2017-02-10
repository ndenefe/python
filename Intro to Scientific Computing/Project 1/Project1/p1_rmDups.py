#
# Noah Denefe ndenefe@smu.edu 
#
#===========================================================

def removeDups(L1, L2):  #there are at least two different ways to implement this
    '''The inputs L1, L2 are two lists,
       return a list that contains all the items in L1 that are not in L2 
    ''' 
    RL=[]
    for item in L1:
        if item not in L2:
            RL.append(item)
    return RL
    
    
       
def removeDups2(L1, L2):
    '''The inputs L1, L2 are two lists,
       return a list that contains all the items in L1 that are not in L2 
    '''
    RL=[]
    for i in range(len(L1)):
        dup = 0
        for j in range(len(L2)):
            if L1[i]==L2[j]:
                dup=1
        if dup==0:
            RL.append(L1[i])
    return RL
            


#===========================================================
if __name__=='__main__':

    import random, copy

    L1=['a','b','c','d'];  L2=['a','b', 1, 'd']

    for i in range(2000):
        L1.append(random.gauss(0,1))    

    L2.append(L1[100:600])
    random.shuffle(L2);  L2.append(L1[800:2000:10])

    L1d = copy.deepcopy(L1); L2d=copy.deepcopy(L2)

    ## call your function here ##
    L3 = removeDups(L1, L2);  
    #L3 = removeDups2(L1, L2);  
 
    test1=False;  test2=False
    for item in L3:
        if item in L2d:
            print('Redundancy removal test failed')
        elif item not in L1d:
            print('Have extra item {}, test failed'.format(item))       
        else:
            test1 = True    #end 'if' and 'for item'

    for item in L1d:
        if (item not in L2d) and (item not in L3):
            print("Missing item {}, test failed".format(item)) #end 'if' and 'for item'
    test2=True

    if test1 and test2:
        print("\n\tCongratulations, you have passed the tests for Problem 1!\n\n")
    else:
        print("\n\t***** Tests failed, need further debugging for Problem 1\n\n")

