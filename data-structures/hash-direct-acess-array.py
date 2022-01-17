## Direct Access Array

# Idea: Give item a unique integer key k in {0,...u-1}...
# And store item in array at index k..
# Or associate a meaning with index of array

# Reference implementation:

#MIT Introduction to Algorithms, Recitation 4
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2020/lecture-notes/MIT6_006S20_r04.pdf


class DirectAccessArray():
    def __init__(self, u):       #O(u)
        self.A = [None] * u

    def find(self, k):       #O(1)
        return self.A[k]

    def insert(self, x):       #O(1)
        self.A[x.key] = x
    
    def delete(self, k):       #O(1)
        self.A[k] = None

    def find_next(self, k):       #O(u)
        for i in range(k, len(self.A)):
            if A[i] is not None:
                return A[i]

    def find_max(self):       #O(u)
        for i in range(len(self.A) - 1, -1, -1):
            if A[i] is not None:
                return A[i]

    def delete_max(self):       #O(u)
        for i in range(len(self.A) - 1, -1, -1):
            x = A[i]
            if x is not None:
                A[i] = None
                return x


    


