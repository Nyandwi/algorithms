### BINARY SEARCH

"""
Idea: To search a given key q in an array of keys S and size n, 
compare q to the middle key(S[n/2]). 
>If q is in the top half of S[n/2], keep it there and recursively repeat the process. 
>If q is in bottom half, do the same things. Recursively search the key q in bottom half.
"""

def binary_search(arr, key, low, high):
    """
    arr: array that contains keys
    key: a key to be searched in array arr
    low: low indice of array arr
    high: high indice of array arr
    """
    middle = (low+high) // 2

    if low > high:
        return -1 #key is not found

    if arr[middle] == key:
        return middle
    
    if arr[middle] < key:
        return binary_search(arr, key, low, middle-1)
    else:
        return binary_search(arr, key, middle+1, high)


# arr = [3,5,6,4,8,9,2]
# binary_search(arr, 5, 0, 6)



