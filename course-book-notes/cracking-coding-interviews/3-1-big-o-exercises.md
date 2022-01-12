## Big O Exercises

##### Example 1: 

```
def foo(array):
    sum = 0
    product = 1
    n = len(array)

    for i in range(n):
        sum += array[i]
    for i in n:
        product *= array[i]

    print(sum + " " + product)
```
This will take O(N) time. The fact that we iterate through the array twice doesn't matter. 

##### Example 2:

```
def printpairs(array):
    n = len(array)
    for i in range(n):
        for j in range(n):
            print(f"{array[i]},{array[j]}")

```
The runtime: O(N^2) because the nested loops are executed N times. Also the code is printing two pairs of numbers. There are O(N^2) pairs, so the runtime is O(N^2).

#### Example 3

```
def printunorderedpairs(array):
    n = len(array)
    for i in range(n):
        for j in range(i+1, n): #start at i+1
            print(f"{array[i]},{array[j]}")

```
Runtime: O(N^2)

#### Example 4
def printunorderedpairs(array_a, array_b):
    for i in range(len(array_a)):
        for j in range(len(array_b)):
            print(f"{array_a[i]},{array_b[j]}")

```
Runtime: O(ab) since there are two inputs. It's not O(N^2).


* The runtime of sorting 1 element in array os O(NlogN). When sorting a elements, runtime is O(a*NlogN). 
