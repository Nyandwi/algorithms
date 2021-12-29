### Lecture 4 - Hashing

[Video](https://www.youtube.com/watch?v=Nu8YGneFCWE&list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY&index=5&t=1948s)
[Notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2020/lecture-notes/MIT6_006S20_lec4.pdf)

* Comparison model meaning: Given a key and item, is the this key bigger than other? Just comparing the keys. =, <=, >=, !=, <,>. It's like graphs of the keys with nodes. 
* Comparison has a constant branching factor. Its run time is log(number of leaves).
* Set: Direct access array.

* Division hash function: h(k) = k mod m. 
* Universal hash function: h(k) = (((ak+b) mod p) mod m).
  
### A Simple video for a hash tables and hash functions:
[Video](https://www.youtube.com/watch?v=KyUTuwz_b7Q)

* A hash table is a data structure that facilitate easy access of data not matter how much data there is. Used in database, error checking, and programming. 
* Hash tables store key-value pairs.
* Hashing algorithm: calculation applied to a key transform into an address. There are many hashing algorithms.