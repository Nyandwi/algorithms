# Smallest Difference: Given two arrays of integers, 
# compute the pair of values (one value in each array) 
# with the smallest (non-negative) difference. Return the difference.


## Sort the arrays, iterate through them and return the min...

import sys

def min_d(arr11, arr22):
    
    arr1 = sorted(arr11)
    arr2 = sorted(arr22)
    
    min_di = sys.maxsize
    pair = []
    
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            
            if abs(arr2[j] - arr1[i]) < min_di:
                min_di = abs(arr2[j] - arr1[i])
                pair = [arr1[i], arr2[j]]
                
    return min_di, pair