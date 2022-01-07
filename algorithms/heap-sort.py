## Heap Sort
### Reference implementation: https://www.programiz.com/dsa/heap-sort
### Heap sort Python: https://docs.python.org/3/library/heapq.html
### Read: https://en.wikipedia.org/wiki/Heapsort

# Heap Sort in python

def heapify(arr, n, i):
      # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
  
    if l < n and arr[i] < arr[l]:
        largest = l
  
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
  
  
def heapSort(arr):
    n = len(arr)
  
    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
  
    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]
  
        # Heapify root element
        heapify(arr, i, 0)
  
  
# arr = [1, 12, 9, 5, 6, 10]
# heapSort(arr)
# n = len(arr)
# print("Sorted array is")
# for i in range(n):
#     print("%d " % arr[i], end='')
import heapq
def heap_in_python(arr):

    h = []

    for i in range(len(arr)):
        heapq.heappush(h, i)

    return [heapq.heappop(h) for i in range(len(h))]

arr = heap_in_python([1,4,5,3,5])
print(arr)

