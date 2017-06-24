#a very very very simple sorting algorithm
import sys
n = int(raw_input().strip())
unsorted = []
sortedList = []
unsorted_i = 0
for unsorted_i in xrange(n):
    unsorted_t = int(raw_input().strip())
    unsorted.append(unsorted_t)
i = 0    
while len(unsorted) > i:
    sortedList = sortedList + filter(lambda x: x == min(unsorted), unsorted)
    unsorted = filter(lambda x: x > min(unsorted), unsorted)
    
    
    
for i in sortedList:
    print i
