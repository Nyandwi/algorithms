### Merge Sort

def merge_sort(A):
    """
    Given a list A, sort it using merge sort. 
    First divide the list into two halves, then resursively sort each half.
    Return the sorted list.

    If the list has length less than 2, return the list since it's already sorted. 
    """
    n = len(A)
    if n < 2:
        return A
    mid = n // 2 #floor division
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
    return merge(left, right)

def merge(left, right):
    """
    Given two sorted lists, merge them into one sorted list. 
    Save the sorted list into the result list.

    left: left sorted sublist
    right: right sorted sublist

    i and j are variables to be used later. 
    i: index of the left sublist
    j: index of the right sublist
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

sorted = merge_sort([3,2,1,4,5,6,10,9,8,7])
print(sorted)