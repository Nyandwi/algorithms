## Linked List Implementation

### Reference: 
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2020/lecture-notes/MIT6_006S20_r02.pdf

class Linked_List_Node:
    def __init__(self, x):         #O(1)
        self.item = x
        self.next = None
    
    def later_node(self, i):          #O(i)
        if i == 0: 
            return self

        assert self.next
        return self.next.later_node(i - 1)



class Linked_List_Seq:
    def __init__(self):         #O(1)
        self.head = None
        self.size = 0

    def __len__(self):         #O(1)
        return self.size
    
    def __iter__(self):         #O(n) iter_seq
        node = self.head
        while node:
            yield node.item
            node = node.next

    def build(self, X):         #O(n)
        for a in reversed(X):
            self.insert_first(a)
    
    def get_at(self, i):        #O(i)
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):        #O(i)
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):        #O(1)
        new_node = Linked_List_Node(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete_first(self):        #O(1)
        x = self.head.item
        self.head = self.head.next
        self.size -= 1
        return x 

    def insert_at(self, i):        #O(i)
        if i == 0:
            self.insert_first(x)
            return 
        new_node = Linked_List_Node(x)
        node = self.head.later_node(i - 1)
        new_node.next = node.next
        node.next = new_node
        self.size += 1
    
    def delete_at(self, i):        #O(i)
        if i == 0:
            return self.delete_first()
        node = self.head.later_node(i - 1)
        x = node.next.item
        node.next = node.next.next
        self.size -= 1
        return x
    
    def insert_last(self, x):        #O(n)
        self.insert_at(len(self), x)
    def delete_last(self):         #O(n)
        return self.delete_at(len(self) - 1)