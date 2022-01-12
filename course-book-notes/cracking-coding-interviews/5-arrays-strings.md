### Arrays and Strings

* A hash table is a data structure that maps keys to values for efficient lookup. 
* The worst case scenario of inserting or retrieving value-pair from the key in hashtable is O(N), where n is the number of keys. A good implementation takes runtime of O(1). 
* We can implement the hashtable with a balanced search tree. It gives us an O(log N) loopup time and it uses less space. 


Some important notes for runtime complexity: 

* If your algorithm is in the form "do this, then, when you are all done, do that" then you add the runtime.
* If your algorithm is in the form "do this for each time you do that" then you multiply the runtime. 
* No matter how many time you loop indepedently in same array, the runtime is O(N). 
