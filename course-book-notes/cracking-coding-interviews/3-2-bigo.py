### BIG O Exercises

### Example 1

def foo(array):
    sum = 0
    product = 1
    n = len(array)

    for i in range(n):
        sum += array[i]
    for i in range(n):
        product *= array[i]

    print(f"{sum}, {product}")
#foo([1,2,3,4])
#runtime: O(N)...The fact that we iterate through the array twice doesn't matter.



## Example 2
def printpairs(array):
    n = len(array)
    for i in range(n):
        for j in range(n): #range(start, stop, step=1)
            print(f"{array[i]},{array[j]}")

#printpairs([1,2,3,4,5])

#The runtime: O(N^2) because the nested loops are executed N times. 
# Also the code is printing two pairs of numbers. There are O(N^2) pairs, so the runtime is O(N^2).


## Example 3

def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        print(n * factorial(n-1))

#factorial(9)

#This is just a straight recursion from n-1 to n-2 down to 1. It will take O(N) time

# Example 4: Fibonacci number

def fib(n):
    """
    Fibonacci number is a series whose each number is the sum of two 
    previous numbers. Ex: 1,1,2,3,5,8,13,21,34,55...
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#fib(3)

#Runtime of fibonnaci is O(2^n) because it is a recursive function. 
#Generally speaking, when you see an algorithm with multiple recursive calls, you are looking at 
# At exponential runtime. 

## Example 5: Fibonacci series

def allfib(n):
    """
    This function will print all the fibonacci numbers up to n
    """
    for i in range(n):
        print(fib(i))
#allfib(5)
#runtime: O(2^N)...The total steps are 2^(N+1)
 
## Example 6: Product of two numbers

def productab(a,b):
    """
    This function will return the product of two numbers
    """
    sum = 0
    for i in range(b):
        sum += a
    return print(sum)
#productab(4,8)

##Runtime: O(b) because the loop runs b times. 

## Example 7: Power of number(a^b)

def power(a,b):
    """
    This function will return the power of a number
    """
    sum = 1
    for i in range(b):
        sum *= a
    return print(sum)
#power(4,3)

#recursive approach

def power(a,b):
    """
    This function will return the power of a number
    """
    if b == 0:
        return 1
    elif b < 0:
        return 0
    else:
        return a * power(a,b-1)
#power(3,4)
        
# Runtime: 0(b).The recursive code iterates through b calls, since it subrtacts one at each level. 

## Example 8: Modular of A % B
from operator import floordiv
def modular(a,b):

    if b <= 0:
        return -1
    #div = floordiv(a,b) only leaves the quotient...no decimal places...
    div = a // b
    return print(a - div * b)

#modular(10,3)
# runtime: O(1): IT DOES A CONSTANT AMOUNT OF WORK. 


## The runtime of a binary search is Olog(N)
## If the binary tree is not balanced, the runtime is O(n), where n is the number of nodes in the tree. 
## The runtime for looking in the specific value in the binary tree is O(N), but the tree is not a binary search tree. 

## Example 10: Sum of digits

def sumdigits(n):
    """
    This function will return the sum of all the digits in a number
    """
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10 #floor division, 123/10 = 12
    return print(sum)

#sumdigits(10002)
# The runtime is O(log(N)). The runtime will be the number of digits in the number. 
# A number with d digits can have a value up to 10^d, then d = log n. 