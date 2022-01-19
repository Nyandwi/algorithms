## Big O: Measuring program effiency

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
# Output: num_sum = 55, time: 34000ns
# Time changes at every run!! Scary :(