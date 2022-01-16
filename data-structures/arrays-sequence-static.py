### Static Array Sequence Implementation

# Static array has fixed size and can't grow or shrink.
# Static array has a O(1) constant time for get_at and set_at operations.
# Static array has a O(n) time for insert and delete operations at the back of the array.


# Reference implementation: MIT Introduction to Algorithms
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2020/lecture-notes/MIT6_006S20_r02.pdf


class Array_Seq:
    def __init__(self):         #O(1)
        self.A = []
        self.size = 0

    def __len__self(self):      #O(1)
        return self.size

    def __iter__(self):         #O(n)
        yield from self.A

    def build(self, X):         #O(n), building a static array from iterable
        self.A = [a for a in X]
        self.size = len(X)
    
    def get_at(self, i):       #O(1)
        return self.A[i]
    
    def set_at(self, i, x):    #O(1)
        self.A[i] = x
    
    def _copy_forward(self, i, n, A, j):            #O(n)
        for k in range(n):
            A[j + k] = self.A[i + k]

    def _copy_backward(self, i, n, A, j):           #O(n)
        for k in range(n - 1, -1, -1):
            A[j + k] = self.A[i + k]

    def insert_at(self, i, x):                  #O(n)
        n = len(self)
        A = [None] * (n + 1)
        self._copy_forward(0, i, A, 0)
        A[i] = x
        self._copy_forward(i, n - i, A, i + 1)
        self.build(A)

    def delete_at(self, i):                 #O(n)         
        n = len(self)
        A = [None] * (n - 1)
        self._copy_forward(0, i, A, 0)
        x = self.A[i]
        self._copy_forward(i + 1, n - i - 1, A, i)
        self.build(A)
        return x

    def insert_first(self, x):               #O(n)
        self.insert_at(0, x)

    def delete_first(self):                  #O(n)
        return self.delete_at(0)

    def insert_last(self, x):                #O(n)
        self.insert_at(len(self), x)
    
    def delete_last(self, x):                #O(n)
        return self.delete_at(len(self) - 1)

# Reference implementation: MIT Introduction to Algorithms
#https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2020/lecture-notes/MIT6_006S20_r02.pdf
 

    