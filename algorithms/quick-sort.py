def quick_sort(list_values):
    """
    Given a list, sort it using quick sort algorithm.
    Working of quick sort: Take the last element as pivot,...
    Partition the array around the pivot, and recursively sort the two sub-lists.
    If the list contains one value, return the array. 
    """
    if len(list_values) < 2:
        return list_values
    
    pivot = list_values.pop()
    lower_than_pivot = []
    greater_than_pivot = []

    for i in list_values:
        if i < pivot:
            lower_than_pivot.append(i)
        else:
            greater_than_pivot.append(i)
        
    return quick_sort(lower_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

sorted_arr = quick_sort([4,6,7,9,3,10,8,2,1,5])
print(sorted_arr)
#Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == "__main__":
    pass