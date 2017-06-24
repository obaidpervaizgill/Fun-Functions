# -*- coding: utf-8 -*-

def fibonacciSeries (length):
    count = 0
    List = [0,1]
    while (count < length):
        List.append(List[len(List)-2] + List[len(List)-1])
        count = len(List)
    return(List)
if __name__ == "__main__":
    print(fabonacciSeries(20))
