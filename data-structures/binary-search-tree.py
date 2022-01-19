## Binary node implementation

# Reference: MIT Introduction to Algorithms, 6006
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2020/lecture-notes/MIT6_006S20_r06.pdf


class Binary_Node:
    def __init__(A, x):
        A.item = x
        A.left = None
        A.right = None
        A.parent = None

    def subtree_iter(A):
        if A.left:
            yield from A.left.subtree_iter()
        yield A.item
        if A.right:
            yield from A.right.subtree_iter()
        
    def subtree_first(A):
        if A.left:
            return A.left.subtree_first()
        return A
    def subtree_last(A):
        if A.right:
            return A.right.subtree_last()
        return A

    def successor(A):
        if A.right:
            return A.right.subtree_first()
        while A.parent and (A is A.parent.right):
            A = A.parent
        return A.parent

    def predecessor(A):
        if A.left:
            return A.left.subtree_last()
        while A.parent and (A is A.parent.left):
            A = A.parent
        return A.parent

    def subtree_insert_before(A, B):
        if A.left:
            A = A.left.subtree_last()
            A.right, B.parent = B, A
        else:
            A.left, B.parent = B, A

    def subtree_insert_after(A, B):
        if A.right:
            A = A.right.subtree_first()
            A.left, B.parent = B, A
        else:
            A.right, B.parent = B, A

    def subtree_delete(A):
        if A.left or A.right:
            if A.left:
                B = A.predecessor()
            else:
                B = A.successor()
            A.item, B.item = B.item, A.item
            return B.subtree_delete()
        if A.parent:
            if A.parent.left is A:
                A.parent.left = None
            else:
                A.parent.right = None
        return A

# Reference: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2020/lecture-notes/MIT6_006S20_r06.pdf