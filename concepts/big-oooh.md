## Big Oh - Program Efficiency

* Big Oh or Big O time is a metric used to measure the efficiency of the algorithms. 
* To develop faster algorithms, it is extremely important to understand Big O. 
* Big O is a notation that describes the order of growth of an algorithm. The lower the order of growth, the better.
* Measuring program efficiency is one of the hardest challenges in solving computational problems. Programs can be implemented in different ways, with different algorithm, and can run on different machines. How one can measure the time efficieny of the algorithm regardless of the approach, type algorithm and machine running the algorithm?
* In addition to Big O, there are other two techniques for measuring the efficiency of the programs which are `timer` and `counting the operations`. Before we talk about Big O, let's see the downsides of those two techniques. 

### Measuring Program Efficiency with Timer and Counting Operations

#### Using Timer

* Measuring the program efficiency using `timer` means timing the program from the beggining of execution to the end of program execution.
* Python has two modules `time` and `timeit` that can be used to measure the runtime: the amount of time it takes to run a program. 
* As you can imagine, the fastest programs has low runtime. The higher the runtime, the slower the program.
* With `time` module, you start the time, run the program, and stop the clock. 
* See the code below:
  
```python
import time
import timeit

def add_numbers(L):
    """
    Add all numbers in a list
    and return sum
    """

    num_sum = 0
    for i in L:
        num_sum += i
    return num_sum

# Timing the program

t0 = time.time_ns()
num_sum = add_numbers([1,2,3,4,5,6,7,8,9,10])
t1 = time.time_ns() - t0
print(f"Solution: {num_sum}, function runtime in nanoseconds: {t1}ns")
# Output: num_sum = 55, function runtime in nanoseconds: 34000ns
# Time changes at every run!!
```

* Measuring the program efficiency with timer can not really tell us much about the efficiency of the program. Time varies for different inputs but it can not express the relationship between the inputs and time it takes to run the program.
  
* Also, timing evaluates the implementation and the capacity of the machine running the program.

* We need to find a better way of measuring the efficiency of the algorithms regardless of implementation and machines, but the size of the input data and the scalability.
* You can also use `cProfiler` to measure the time in more nice way.
  
#### Counting the Number of Operations

* Most operations such as mathematical, comparison, assignment take constant time.
* For example, assignment operator (`num = 0`) is one operation, `2*3 + 4` is two operations(addition and multiplication).
  
* Similar to timing the program execution, operation counts is not efficient too. The number of operations depend on the implementation and there is no clear definition of which operations to count.
  
* Counting the operations though consideration of input data and it's independent of computers, but still we need a better way of measuring the program efficiency. This is where Big O comes into the picture.

### Big O Again

* The better way of measuring the efficiency of the program should largely depend on the algorithm, scalability and the size of the inputs.
* The input could be an integer, a list, array, or multiple inputs to a function.
* There are 3 cases for Big O:
  * **Best case**: The minimum possible running time over all inputs of a given size. Say you are searching the element in a list and by luck, such element is the first element of the list.

  * **Average case**: The average running time over all possible inputs of a given size. For i input of a running time ti, average case is the average time for running all possible inputs n.
  
  * **Worst case**: Maximum running time over all possible inputs of a given size. Example of worst case time: Say you are searching the element in list, and that elements turns out to be the last element. You will have to go over all elements of the list until you find the target element. The element could also not be part of the list...worst! Exhausted resources!!

* The best case time is not useful. It can trick us to think that our program is faster but not actually true!
  
* Average case and worst case are sometime similar. 
  
* To summarize Big O:
  * Big O is used to measure the program's efficiency for large inputs. It measures the upper bound on the asymptotic growth or order of growth.
  * We are interested in the worst case. In real life, worst case scenarios occurs a lot. 
  * Big O evaluate the algorithm not the hardware and implementation.
* In Big O time measurements, additive and multiplicative constants are ignored. Our interests are in finding how the time grows with the input.

#### The Order of Big O

* Big O defines the order of growth of a particular program. O actually mean `Order` or On `the Order of n`, where n is the size of the input data to a program.
* There are at least 6 orders from the lowest to the highest:
  * Constant time: $O(1)$
  * Logarithmic time: $O(log n)$
  * Linear time: $O(n)$
  * Log-linear time: $O(nlogn)$
  * Polynomial time: $O(n^c)$, c is a constant
  * Exponential time: $O(c^n)$

* `O(1)` and `O(log n)` are fast, `O(n)` and `O(nlogn)` are not bad, and the latter two are very slow. Unless it's the only possible option, you should avoid having the algorithm that has runtime of `O(n^c)` or `O(c^n)`.
* $O(1)$ << $O(log n)$ << $O(n)$ << $O(nlogn)$ << $O(n^c)$ << $O(c^n)$.
* Below is the illustrations of 6 different orders of growth:

![image](../images/bigo.png)
Credit: MIT 6.0001, Lecture 10...More about the course in references.

* Let's talk about those orders in details.

##### 1. Constant time

