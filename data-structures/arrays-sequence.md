## Arrays Sequence

* The array is one of the fundamental data structures. Arrays are data structures that has fixed-size(static arrays) that can store elements. The elements in array can be efficiently located by their indices.
* Arrays also possess space efficiency because they only store data of certain type. No other things like links. Arrays are also good for memory allocation tasks. Iterating through the arrays values is pretty fast due to their excellent memory locality.
* Static arrays are great for static operations such as `get_at(i)` and `set_at(i,x)` in `O(1)` constant time. The constant time is due to that each element in array maps directly to its index, so getting the items by their index or memory address position is pretty fast.
* But they are not good for dynamic operations such as `insert_first(x)`, `delete_first()`, `insert_last(x)`, `delete_last()`, `insert_at(i,x)`, `delete_at(i)`. Those operations take `O(n)` linear time.
* The reason these operations takes linear time is that in order to insert or remove the item in array, we have to reallocate the array and shift all items after the modified item.
* To overcome the downside of static arrays such as fixed size and linear time on dynamic operations, we can use dynamic arrays.


### Dynamic Arrays

* Dynamic array is efficient for dynamic operations such as `insert_last(x)`, `delete_last()`. These operations takes constant time(O(1)). For static arrays, they take linear time(O(n)) with respect to the length of the array.
* Python list is a dynamic array.
* The idea of dynamic array is to allocate extra or additional space when you request space for adding a new element in the array faster.
* Inserting an element into a dynamic array is as simple as copying over the new value into the next empty slot.
* The only issue with dynamic array is that everytime you insert an element into array, you reserve additional space which means there is a less space for other parts of the program. Computer memory is a finite resource.
* High level languages like Python provides abstraction for memory management and allocation. Whenever you ask Python to store something, Python makes a request to the operating system behind-the-scenes for a fixed amount of memory in which to store data. So, for inserting element in dynamic array(list in python), Python requests extra space to the OS which can limit the available space for other running operations.
* The allocated space when the array is full is O(n) extra space. 
* Python list doesn't always append in constant time. It sometimes takes O(n) linear time. Only allocating the extra space in the right way can guarrantee that any sequence of n insertions only takes at most O(n) time. So, on `average`, insertion takes O(1) time per insertion. That time is called `amortized constant time` because the cost of the operation is amortized(distributed) across many applications of the operation.
* To achieve an amortized constant running time for insertion into an array, we must allocate extra space in proportion to the size of the array being stored.
* Allocating O(n) additional space ensures that a linear number of insertions must occur before an insertion will overflow the allocation.
* Deleting or popping the item at the back of the array takes O(1) time too. Great!!
* To delete the last item from the array, we simply decrement a stored length of the array. This is what Python does in essence.
* The issue with that is that if a large number of items are removed from the array or large list, the unused additional space could occupy a significant amount of wasted memory that would be useful for other operations.
* To summarize the runtime of dynamic arrays operations:
  * All last operations(`insert_last(x)`, and `delete_last()`) takes `O(1)` constant time.
  * Inserting into a dynamic array takes `O(1)` amortized constant time.
  * Deleting the last element takes O(1) time too, but there is an issue of unused space if many items are removed.
  * Python List `append` and `pop` are amortized `O(1)` time and other operations can be `O(n)`.

