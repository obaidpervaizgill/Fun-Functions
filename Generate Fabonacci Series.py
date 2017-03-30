# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 23:27:19 2017

@author: z3470247
"""

def fabonacciSeries (length):
    count = 0
    List = [0,1]
    while (count < length):
        List.append(List[len(List)-2] + List[len(List)-1])
        count = len(List)
    return(List)
if __name__ == "__main__":
    print(fabonacciSeries(20))