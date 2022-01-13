## Insertion Sort

def insertion_sort(arr, n):
    """
    Given an array/list of integers, 
    return sorted array
    """

    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key