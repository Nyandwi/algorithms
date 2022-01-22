## Big O: Measuring program effiency

### 1. Adding numbers
import time
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



### 2. Factorial

def factorial(n):
  """
  Given an integer value, 
  return its factorial without using resursive approach
  """

  facto = 1 # Assignment Takes constant time: O(1)
  while n > 1: # This loop will run n times: O(n)> Because the loop has 2 lines to execute, it will be O(2n)
    facto *= n # Takes constant time: O(1)
    n -= 1 # Takes constant time: O(1)
  return facto
print(factorial(3)) #3x2x1
#Output: 6
# The total O time = O(1 + 2n + 1 + 1)
# All constants are neglected, so the resulting runtime is O(n)

### 3. Week Days 

def week_days(week_d):

  days_T = []

  for day in week_d:
    if day[0] == 'T':
      days_T.append(day)
    
  return days_T

week_d = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
week_days(week_d)
#['Tuesday', 'Thursday']