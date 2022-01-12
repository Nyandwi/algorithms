## Lecture 3 - Sets and Sorting

[Video](https://www.youtube.com/watch?v=oS9aPzUNG-s&list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY&index=4)

[Course Materials](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2020/)

### Last lectures  review:
* Interface: Collection of specifications (e.g, sequence & set). It's like specifications. 
* Data structures: Way to store data that supports a set of operations. 


### Sets and Sorting

* A set is a container that contains say all unique students in the classroom. 

Set Interface
------------
* A container:: 
  * build(A): Given an iterable A, build a sequence from items in A 
  * len(A): return the number of stored items

* Static: find(k): return the stored item with key k
* Dynamic: 
  * insert(x): add x to set(replace item with key x.key if one already exists)
  * delete(k): remove and return the stored item with key k

* Order: 
  * iter_ord(): return the stored items one by one in key order
  * find_min(): return the stored item with smallest key
  * find_max(): return the stored item with largest key
  * find_next(k): return the stored item with smallest key larger than k. 
  * find_prev(k): return the stored item with largest key smaller than k. 

The above are set interfaces. Not data structures. Sets just specify the operations. A set is like dictionary in Python(key-value pairs). 

* An unordered array is a perfectly a resonable way to implement a set interface and searching that array will take linear time every single time I search. 
* Array is a data structure. 
* How long it takes to search for any given element in sorted array: Log(n) time 
* How long it takes to build a sorted array: nlog(n)


### Sorting

* Sorting is a way to arrange the elements in a collection in a way that is convenient for processing.

* Sorting vocabulary:
  * Destructive: overwrites the input array.
  * In place: Uses O(1) extra space. 

* Permutation Sort

```
def permutation_sort(A):
    '''Sort A'''
    for B in permutations(A):
        if is_sorted(B):
            return B
``` 

* Permutation Sort is a sorting algorithm that sorts the input array in a permutation.(by Copilot)

* How to check array A is sorted:
```
for i in range(n-1):
    if A[i] <= A[i+1]:
        continue
    else:
        return False
```

* Helper function for selection sort:

```
def prefix_max(A,i):
    '''Return the largest element in A[:i+1]'''
    if > 0:
        j = prefix_max(A, i-1)
        if A[i] < A[j]:
            return j
    return i
```

* Selection sort

```
def selection_sort(A, i=None):
    ```Sort A[:i +1]'''
    if i is None: i=len(A)-1
    if i>0:
        j = prefix_max(A,i)
        A[i], A[j] = A[j], A[i]
        Selection_sort(A, i-1)
```

* Merge Sort

...Recursively sort first half and second half (may assume power of two)
.....

For course notes:https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2020/lecture-notes/MIT6_006S20_lec3.pdf