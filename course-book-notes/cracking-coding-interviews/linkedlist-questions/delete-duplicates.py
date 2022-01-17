## Delete duplicated in a linked list

# Question: Write a code to remove the duplicated from unsorted linked list.
# Follow up: How would you solve this problem if a temporary buffer is not allowed?

# Solution: Iterate through the list, if the current node's data is equal to the next node's data, 
# Then delete the next node. 
# If the current node's data is not equal to the next node's data, then move to the next node.

def delete_duplicates(head):
    if head is None:
        return None
    
    current = head
    while current.next is not None: #stop the iteration when the current node is the last node...last.node.next = NULL
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

# The runtime complexity of this algorithm is O(n)
# But we are assuming sorted linkedlist in the above case.
# Since the list is not sorted one might use a hash table to store the dat and delete duplicates by iterating though the list

def dele_duplicates(head):
    if head is None:
        return None
    
    current = head
    hash_table = {}

    while current is not None:
        if current.data in hash_table:
            current.next = current.next.next #remove it if it's already in hash table
        else:
            hash_table[current.key] = current.data
            current = current.next

    return head

# Time complexity: O(n)


# If the temporary buffer is not allowed, 
# We can iterate through two pointers:  
# current which iterates through the linked list, and runner which checks all subsequent nodes for duplicates.

def delete_duplicates_without_buffer(head):
    if head is None:
        return None

    current = head

    while current is not None:
        runner = current
        while runner.next is not None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

# The runtime complexity of this algorithm is O(1) but the space complexity is O(n^2)