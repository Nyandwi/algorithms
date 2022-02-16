## Stacks and Queues

* Stacks and queues are container type data structures. Container data structures store data and allow retrieval of items or elements independent of content but the `order` they received the data.
* Stacks and queues are dynamic sets in which the element removed from the set by the `delete` operation is prespecified.
* The opposite to container data structure is a dictionary which store and retrieve items based on their key values or content.
  
### Stacks

* Stack supports data retrieval in `LIFO`(last-in, first-out) order.
* The element that is deleted from the set is the one that was lastly inserted.
* Stacks are most preferred when the retrieval order doesn't matter. 
* Example: Passengers in a subways typically exit in LIFO manner: those who entered last get out first. Another example is the stacks of plates used in cafeteria. The closer plates (those inserted recently) are accessed first.
* Stacks have two main operations that are `push()` and `pop()`:
    * `Push(S,x)`: Insert item x at the top of stack S.
    * `Pop(S)`: Return (and remove) the last item of stack S. Pop doesn't take argument.

* Algorithmic speaking, `LIFO` tends to take place when running a recursive algorithm.

Below is a pseudocode for stack: `Empty stack`, `push` element to stack, and `pop` element to a stack.

```python
def stack_empty(S):
    """
    When S.top == 0, stack is empty. 
    If we pop item in empty stack, it underflows. 
    If S.top exceeds n or S.length, stack overflows.
    """

    if S.top == 0:
        return True
    else:
        return False
```
```python
def push(S, x):
    """
    Given stack S and item X, insert X at the top of stack by shifting the top index of S 
    ...by 1 and insert x at current top index.
    """

    S.top = S.top + 1 #S.top is index of top item, shift the item that were at top
    S[S.top] = x
```

```python
def pop(S):
    if stack_empty(S):
        error: underflow
    else:
        S.top = S.top - 1
        return S[S.top - 1]
```

### Queues

* Queues supports data retrieval in `FIFO` manner: first in, first out.
* Queues are used in waiting services or telecommunication phone calls service networks. You want the customer who came first to be served first. You want the subscriber who made the call first to be switched to people they called first(call services are now automatic, but back in days when someone has to manualy connect two people calling each other, delay was inevitable due to queued calls).
* The customer who comes last are placed on the end of the line and they are shifted to ward the front as new customer comes in and older customer get served. First in, first out.
* Queue has `head` and `tail`.
* Like stacks, queues has two main operations that are `enqueue()` and `dequeue()`.
  * `Enqueue(Q, x)`: Insert item x at the back of the queue Q. It's like stack insert operation. Enqueue inserts elements at the last of queue just like new customer are placed on the end of the waiting line.
  * `Dequeue(Q)`: Return and remove the front item from the queue Q. Just like stack pop, it also doesn't take argument. Get the first item...Serve that one customer who is in front of the waiting line, one who came first....First in, first out...
  
Below is a pseudocode for enqueue and queue:

```python
def enqueue(Q, x):
    """
    Insert x at the tail of Q
    Q.tail: index of tail
    """
    Q[Q.tail] = x
    if Q.tail == Q.length:
        Q.tail = 1 
    else:
    Q.tail = Q.tail + 1
```

```python
def dequeue(Q):
    x = Q[Q.head] #Q.head: index of head
    if Q.head == Q.length:
        Q.head = 1
    else Q.head = Q.head + 1
    return x
```


### Implementing Stack and Queues

* Stack and queues can be implemented with lists and arrays. 
* Stack can simply be implemented in Python list, where push operation is append() method, and pop stack operation is pop().
* Queue can also be implemented as a list, where the first element can be retrieved first(FIFO), but it's not efficient for that purpose. Inserting and poping(stack) from the end of the list are fast, but doing the same thing at the front of the list are super slow because you have to shift every element by 1 to be able to insert & pop. 
* Fortunately, Python has a [dequeue](https://docs.python.org/3/library/collections.html#collections.deque) in collections that you can use to insert & pop elements to the front & back of the list.


### References

- Introduction to Algorithms MIT book
- Algorithms Design Manual, Steven Skienna
- Data stuctures, Python [doc](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues)
