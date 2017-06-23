#a very very very simple sorting algorithm
integer = [2,5,4,1]

def quickSort(externalListObject): 
    
    i = 0
    internalListObject = externalListObject
    sortedList = []
    
    while len(internalListObject) > i:
        sortedList = sortedList + filter(lambda x: x == min(internalListObject), internalListObject)
        internalListObject = filter(lambda x: x > min(internalListObject), internalListObject)
    print(sortedList)
        
if __name__ == '__main__':
    quickSort(integer)
