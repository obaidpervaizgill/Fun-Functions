# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 21:48:25 2017

@author: z3470247
"""

def primeNumbers (start, end):   
    num = range(start,end+1)
    prime = []
    for i in range(0,len(num)):
        test = []
        ran =  [k for k in range(1,20) if k < num[i]]    
        for j in range(0,len(ran)):
            if num[i]%ran[j] == 0:
                test.append(ran[j])
            else:
                pass
        if len(test) > 1:
            pass
        else:
            prime.append(num[i])
    return(prime)
    
if __name__ == "__main__":
    print(primeNumbers(1,23))
        

        