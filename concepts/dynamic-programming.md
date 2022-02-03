# Dynamic Programming
<a name='0'></a>
**********
**Content:**
- [Dynamic Programming](#dynamic-programming)
    - [1. Introduction](#1-introduction)
    - [2. Solving Fibonacci Series With Dynamic Programming](#2-solving-fibonacci-series-with-dynamic-programming)
    - [3. Dynamic Programming With Bottom Up Approach](#3-dynamic-programming-with-bottom-up-approach)
    - [4. Summary: Dynamic Programming Vs Recursion Vs Divide and Conquer](#4-summary-dynamic-programming-vs-recursion-vs-divide-and-conquer)
    - [5. References and Further Learning](#5-references-and-further-learning)
************

<a name='1'></a>
### 1. Introduction

* Dynamic programming is an efficient technique that is used to solve problems that have overlapping problems (subproblems that contains other subproblems).

* A particular problem has overlapping problems if an optimal solution involves solving the same problem multiple times.

* Dynamic programming solves each subproblem once, save or cache the results, and use the results later rather than recomputing the subproblem. Storing the results of all possible subproblems in a systematic way reduce the time and space required to reach to the optimal solution. The work is merely minimized.

* Dynamic programming is used to solve optimization problems - Optimization problems are problems whose solutions maximizes or minimizes some function. Example of optimization: gradient descent that minimize the loss function.

* Dynamic programming is typically employed when optimizing the recursive algorithm. If a recursive algorithm computes some subproblems more than once, we can save the results of those subproblems(in a table) and use them later thereby saving time and space and minimizing the work to be done. 

* The process of storing the computed results of subproblems and using them later wherever possible is called `memoization`.

* Dynamic programming is suited for optimization problems that have an inherent `left to right` order such as string characters, rooted trees and integer sequences.

* Let's efficiently solve the fibonacci series with dynamic programming.

<a name='2'></a>
### 2. Solving Fibonacci Series With Dynamic Programming

* Fibonacci series is a hello world of recursion and dynamic programming. 
* A fibonacci series is a series in which a current number n is equivalent to the addition of two previous number in the sequence. Below is the expression of a fibonacci series.

>`F(n) = F(n-1) + F(n-2)`, 
`F(0) = 0, F(1) = 1, F(2) = 1, F(3) = 2, F(4) = 3 ...`

* Before we seek to optimize the fibonacci series, let's implement it with recursion.

```python

def fibo(n):
    """
    Base cases: fibo(0) = 0, fibo(1) = 1
    """

    if n == 0 or n == 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

```

* Fibonacci series of large numbers are hard to compute. Take for example: Computing `fibo(120)`  gives `8,670,007,398,507,948,658,051,921` and if we assume each recursive call takes a nanosecond, it would take 250,000 years to finish. The reason why it takes lots of time to compute fibonacci series is that there are multiple similar recursive calls that are computed at every step. In fact, the idea behind dynamic programming is identifying those similar recursive calls and store their results to avoid computing them more than once.

* Let's take an example for `fibo(5)`. Below is the recursive tree of `fibo(5)`. As you can notice, it has `3 fibo(2)` and `2 fibo(3)`.

![fibo](../images/fibo.JPG)

* If we modify the recursive tree like below, we could potentially save work needed to find the number of the series since we are not recomputing the functions that already have values.

![fibo2](../images/fibo-2.JPG)


* Let's now compute the fibonacci series efficiently using dynamic programming. The only thing we do is to store the results of the similar recursive calls and reuse them everytime we face them rather than recomputing twice or thirdth or fourth...

```python

def fibo_2(n, mimo = {}):
    """
    Find the fibonnacci of n.
    mimo: a dictionary to save results of overlapping recursive calls....
    ...n as keys and their results as values.
    If n > 1 is already in mimo, return its value. It's the result of the series
    Else: find its result, save it to memo and return it
    """
    
    if n == 1 or n == 0:
        return n
    
    if n > 1:
        if n in mimo:
            return mimo[n]
        else:
            result = fibo_2(n - 1, mimo) + fibo_2(n - 2, mimo)
            mimo[n] = result
            return result
```

```
fibo_2(3)
2
fibo_2(120)
5358359254990966640871840
```
* `fibo_2(n)` in few words: If `n` is either 1 or 0, return 1 since the fibonacci of 1 or 0 is 1. If `n` is greater than 1 and is in `mimo`(initialized as `empty dictionary` to store `overlapping recursive calls`), return the value of `n` in `mimo` (we are saving `n` as keys in `mimo` dictionary and their results as values). If `n` is not in `mimo`, it means we haven't computed it yet, and so compute it and save the results in `memo`.

* Now we have a very efficient fibonacci series for computing even large series for resonably short time. Computing `fibo_2(120)` takes fraction of milliseconds when it was almost impossible to find it with normal recursive function. Indeed, normal recursive function would take `thousands of years` to find it if we assume each recursive call takes 1 nanosecond. That really demonstrates the beauty of dynamic programming.
  
* The runtime of `fibo_2(n)` is `O(n)` since we are caching the results and there are only n values to pass to `fibo_2(n).` Looking the value in a dictionary takes `O(1)` constant time, so we don't count that. This also much better than O(2<sup>n</sup>) of normal recursive function.

<a name='3'></a>
### 3. Dynamic Programming With Bottom Up Approach

* The approach we used to solve the above fibonacci series with dynamic programming is typically called `top-down approach` where we start solving the problem from the top, divide it into subproblems, save the results of the overlapping subproblems and reuse the results later.
  
* In the bottom-up approach, we solve the problem by starting with simplest case. For fibonacci series, we start with finding the fibonacci of 0, then 1, then 2, then 3, etc...and we make sure to use the previous results.

```python
def fib_bottom(n):
    if n == 1 or n == 0:
        return n
    
    a = 0
    b = 1
    
    for _ in range(n):
        c = a + b
        a = b
        b = c
        
    return c
```
```
fib_bottom(120)
5358359254990966640871840
```

* **What we are doing above:** As usual, if n is 0 or 1, its fibonacci number is n. We start with assigning 0 to variable `a` and 1 to `b` as the simplest cases. Then at every step all the way to n, we find `c` as sum of `a` and `b`(c is like the fibonacci of i but we are not using i), `update a with b` and `update b with c`. 

* The runtime of the algorithm is `O(n)` for looping through the list `range(n)`. Finding `fib_bottom(120)` also takes a fraction of milliseconds.

<a name='4'></a>
### 4. Summary: Dynamic Programming Vs Recursion Vs Divide and Conquer

* Dynamic programming is an efficient technique that is used to solve problems that have overlapping subproblems (subproblems that contains other subproblems).

* Recursion is a technique used to solve the kind of problems that can be defined in simpler versions of themselves. In essense, recursion is based on divide and conquer technique.

* For some problems, recursive approach is not usually efficient due to the overlapping recursive calls that takes lots of space. Dynamic programming is used to optimize the recursive functions that have overlapping recursive calls.
  
* Divide and conquer is a well-known and popular technique used to divide a given problem into different subproblems, recursively solve each subproblem and merge the results to form the final solution. Algorithms such as merge sort, quick sort, and binary search use divide and conquer technique.

* Dynamic programming is not all you need. It's only helpful and efficient when the number of unique subproblems are significantly smaller than the total number of subproblems. 

<a name='5'></a>
### 5. References and Further Learning

* Introduction to Computation and Programming Using Python, John V. Guttag
* Algorithm Design Manual - Skienna
* Introduction to Algorithms - MIT Press


[BACK TO TOP](#0)