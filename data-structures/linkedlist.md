## LinkedList Data Structure

* Data structure is a way to store data, with algorithms that support operations on the data. 
* Data structure is an important part of a program. Using a data structure that suits a particular data can make a program faster.
* Just as it is better to be born with a good heart than to have a replacement later, it is also important to choose the right data structure for the application in the first place. 
* Data structures can be classified into either contiguous or linked depending on whether they are based on pointers or arrays. 
  * *Contiguously-allocated structures* are composed of single slabs of memory and include arrays, matrices, heaps and hash tables. 
  * *Linked data structures* are made of distinct chunks of memory bound together by pointers and include lists, trees, and graphs adjacency lists. 
* We will revisit most important elementary data structures: linkedlist, stack and queues, arrays, binary trees, heaps, and hashtables. Starting with LinkedList...

### LinkedList

* A linked list is a special data structure that arranges objects in a linear order. 
* In arrays, a linear order is determined by the array indices. In a linked list, the linear order is determined by a pointer in each object. Thus, a linked list is a pointer data structure.
* Pointers are the connections that hold the pieces of linked structures together. They represent the address of a location in a memory. Skienna pointer analogy: a cell-phone number can be thought of as a pointer to its owner as they move about the planet.
* Linked list is a simple and an efficient representation of dynamic sets. Dynamic sets are collections of items that can be changed, shrinked or simply manipulated by algorithms.
* a linked list supports 3 main operations: searching, insertion, and deletion. 
* A linked list has an attribute `key` and two other pointer attributes: `next` and `prev`...This is doubly linked list.
* Each item(key) is stored in a node which contains a pointer to the next node in a sequence. Each node has two fields: `node.item`, and `node.next`..This is singly linked list.
* Given an element x in a linkedlist A, x.next points to its `successor` in the list, and x.prev points to its `predecessor`.
* If `x.prev == NULL`, the element x has no predecessor and it is the first element in a list, a.k.a `head`. 
* If `x.next == NULL`, the element x has no successor and it is thus the last element in a list, a.k.a `tail`. 
* An attribute `L.head` points to the first element in a list. If `L.head == NULL`, the list is empty. 
* A list can take different forms. It can be sorted or unsorted, singly linked or doubly linked, circular or not. 
* If a list is sorted, the linear order of the list corresponds to the linear order of keys stored in elements of the list. The minimum element of a sorted list is the `head`, and the maximum element is the `tail`. 
* If a list is not sorted, its element can be in any order.
* If a list is singly linked, we omit the prev pointer in each element. If a list is doubly linked, each node points to both its predecessor and successor element.
* To add an item after another item in  the list, we simply have to change some addresses or relink pointers.
* Adding a new item at the front(head) takes O(1) time!!! Same for deleting the first item in the list.
* Inserting or deleting the item at the tail of a list takes O(n) time.
* The only way to get or find the ith element in the list is to step through the items one by one, which leads to worst-case linear time for `get_at(i)` and `set_at(i,x)` operations. They take `O(n)` runtime.
* Python builtin list is different from linked list. Read more about (linked list in Python](https://realpython.com/linked-lists-python/).

* Next: Pseudocode for searching, inserting, and deleting item in the list.

#### Searching a linked list

* Searching an item k in a list L can be done by performing a simple linear search, returning a pointer to such an item.
* It can be done iteratively or recursively. 
* If there is no item in the list, the search returns NIL. 

Below is the pseudocode for iterative approach.

```python
def linked_list_search(L, k):
  x = L.head #first element
  while x != NILL and x.key != k:
    x = x.next
  return x #return x when it is equal to k per while condition.
  ```

The runtime for the above search is O(n) since it may have to search the whole list in worst case scenario.

  A recursive approach:

  ```python
  def linked_search(L, k):
    """
    Given a list, find item k...
    Edge case: if L is null, return null

    >> if k is the first element, return the first element. Else, recurse through the rest part of the list (removing the first element)
    """

    if L == NULL:
      return NULL
  
    if L.head == k:
      return L.head

    else:
      return(linked_search(L.next,k))

```

#### Inserting 

* Given a list whose key attribute has already been set, the insert_list procedures "splices" x into the front of the linked list.

```python
insert_list(L, x):
  x.next = L.head
  if L.head != NILL:
    L.head.prev = x
  L.head = x
  x.prev = NIL
```

The runtime for inserting item on the front of the list is O(1) time. For inserting the item at back of the list, it is O(n).

#### Deleting

* To delete the item in a list, we must provide its pointer to the delete function so that it can splice the item out of the list and update pointers. Simply put, to delete the element of the list, we must first call `list-search` to retrieve a pointer to the element.

```python
def delete_list(L, x):
  if x.prev != NIL:
    x.prev.next = x.next
  else L.head = x.next
  if x.next != NIL:
    x.next.prev = x.prev
```

If we ignore boundary condition:
```python
def delete_list(L, x):
  x.prev.next = x.next
  x.next.prev = x.prev
```

List delete takes O(1) for deleting the first element, but it takes O(n) for deleting the last element in the list.

The boundary conditions for tail and head can also be applied on the list search and insert.

### References

* MIT Introduction to Algorithms
* Intruction to Algorithms MIT book
* Algorithms Design Manual by Steven Skienna