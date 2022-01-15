# Implementation of Stack and Queues

# Stack: LIFO, last in first out. Insert at the end of list, pop the element at the back of the list. 
# Stack: New entrance goes to the back. Who leaves first is who entered last.
# Queue: FIFO, first in first out. Insert at the back of list, pop the element at the front of the list. 
# Queue: New arrivals goes to the last
# Queue: Who leaves first is who came first.

### STACK

S = [1, 2, 3, 4]

def insert_stack(S, x):
    S.append(x)
    return S

stack = insert_stack(S, 5)
print(stack)
#Output: [1, 2, 3, 4, 5]

def pop_stack(S):
    x = S.pop() #by default, pop returns the last element
    return x, S
last_item, new_stack = pop_stack(S)
print(f"Popped item: {last_item}, Remaining Stack:{new_stack}")
#Output: Popped item: 5, Remaining Stack:[1, 2, 3, 4]


### QUEUE

from collections import deque

arrival_queue = deque(['Jean', 'Ras', 'Sun', 'Prit'])

# Adding new arrivals to the the arrival line

def enqueue(Q, x):
    Q.append(x)
    return Q

# Michael(my brother) arrives, add him to the last line of the queue
arrival_queue = enqueue(arrival_queue, 'Michael')
print(arrival_queue)
#Output: deque(['Jean', 'Ras', 'Sun', 'Prit', 'Michael'])

# Rose(my sister) arrives too, add her to the last line
arrival_queue = enqueue(arrival_queue, 'Rose')
print(arrival_queue)
#Output: deque(['Jean', 'Ras', 'Sun', 'Prit', 'Michael', 'Rose'])

# Leaving the arrival queue

def dequeue(Q):
   left = Q.popleft()
   return left, Q

# Now the first arrival is leaving

leaving, arrival_queue = dequeue(arrival_queue)
print(f"Arrival leaving: {leaving}, Remaining arrivals:{arrival_queue}")
#Output: Arrival leaving: Jean, Remaining arrivals:deque(['Ras', 'Sun', 'Prit', 'Michael', 'Rose'])

# Now the second arrival is leaving too
leaving_2, arrival_queue = dequeue(arrival_queue)
print(f"Arrival leaving: {leaving_2}, Remaining arrivals:{arrival_queue}")
#Output: Arrival leaving: Ras, Remaining arrivals:deque(['Sun', 'Prit', 'Michael', 'Rose'])

# Now the third arrival is leaving
leaving_3, arrival_queue = dequeue(arrival_queue)
print(f"Arrival leaving: {leaving_3}, Remaining arrivals:{arrival_queue}")
#Output: Arrival leaving: Sun, Remaining arrivals:deque(['Prit', 'Michael', 'Rose'])



# More about dequeue here: https://docs.python.org/3/library/collections.html#collections.deque



