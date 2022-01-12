These are lecture notes of MIT Intro to Algorithms, Spring 2020.

Playlist: [Youtube](https://www.youtube.com/playlist?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY)

### Lecture 1: Algorithms and Computations

[Video](https://www.youtube.com/watch?v=ZA-tUyM_y7s&list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY)

* The course is about teaching how to solve computational problems, communicating the solutions to others, prove corectness, and being aware that they way you are solving them is efficent.
* The goals in brief: solve computational problems, prove correctness, argue efficiency, and communicating ideas...and hence more writing than coding.
* A computational problem: Given the input and output having a certain kind of relation, can you check if the output is correct? 
* Example of a computational problem: Given an array of numbers, can you find the largest number in the array? Can you find the number at an index 5?
* The class is about general problems that have arbitarily size of inputs. 
* Algorithms: a function that takes input and maps it to output and that output better be correct. The real check of algorithm's correctness is to prove it's correctness by giving a true output. 
* Example of algorithms for birthday problem: 
    * Maintain record 
    * Interview students in same order
        * Check if birthday in record
            * If so, return a pair
        * Add new student to record
    * Return None if there is no output

* Algorithms are the core of computer science. They are the foundation of all the other fields(The whole sentence is suggested by GIthub Copilot and it seems right :)).
* Computer scientists write constant size piece of codes that can take any arbitarily sized input and loop(or recurse, or whatever) through the code in order to read the input and to produce output.
* Inductive hypothesis: If first k students contain a match, algorithm return a match before intervewing k+1 student.
* Meaning of efficiency: How fast does this algorithm run? And how fast does it compare to other possible ways of solving this problem?
* How to check efficiency? Time how long it takes to run the algorithm. Time also depends on size of data and the efficiency of the computer running the algorithm. So, that's not a correct meaning of efficiency.
* Checking efficency: Don't measure time, count operation instead! We expect the performance to depend on the size of the input n.
* A model of computation: 
    * WordRAM: Random access memory...Can randomly access different places in memory in constant time. A memory is a bunch of 1's and 0's.
    * CPU: Central processing unit, can hold and process instructions. 

* A byte: unit of modern computer memory. It's a collection of 8 bits.
* A number of addresses in 32-bit computer = 2 power 32 = 4GB which means in order to read something of 32bit in memory, you need to have a hard disk of at least 4GB.
* It takes a constant amount of time to operate on a constant amount of memory.
* Next lecture: Data structures

![image](images/mit1.png) 

### Lecture 2: Data Structure and Dynamic Arrays

[Video](https://www.youtube.com/watch?v=CHhwJjR0mZA&list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY&index=2)

* There are lots of dat structures and each one is like multiple algorithms.
* The difference between interface (API) and data structures

    * Interface says what you want to do(specifications),  data structure says how you do it. 
    * Interface specify what data you can store,  whereas data structure give actual representation on how to store data (just throw data in a file...)
    * Interface specifies what operations are supported and what they mean, and data structures gives you algorithms on how to support those operations.
    * Interface are like problem statement, where data structures are algorithmic solutions to the problems.

* Two main data structures: set and sequence
* The idea of set is we want to store any arbitarily things(integers, strings) and we care about their values, have them in ordered order, and be able to search their values(keys)
* The idea of sequence is that we want to represent a given numbers in a sequence. Example is a list of numbers in Python, [2,3,4,5]. 
* Two main data structures tools/approaches: 

    * Arrays
    * Pointer/linked based data structures

* Leval of sequence interfaces
    * Static sequence interface: maintain a sequence of fixed size, but actual items might change. Example: Given X0, X1, X2....Xn-1, 
        * build(X) to make new DS for items in X
        * len(X) to get the length of X
        * iter_seq(X) to iterate over X and output X0, X1, Xn, Xn-1 in sequential order. 
        * get_at(i): Return item at index i...The obvious way to implement this is to use a list (or array)
        * set_at(i,X): Set Xi to X
        * get_first/last(): Return first/last item in X
        * get_first/last(X): Return first/last item in X.
* In Python, there are no static arrays. There are only dynamic arrays. 
* * Computation key idea/model: word RAM model of computation. Your memory is an array of w-bit words. And since it's RAM, you can access the items in memory randomly. 
    * Array: a consecutive chunk of memory.
    * array[index i] = memory[address(array) + i]: get item at index in in memory in a constant time from the adress that stored the array. As long as items are stored in memory consecutively, they can be accesses in constant time randomly. 
* Static arrays: get_at(i), build(X) and iter_seq(X)
* Memory allocation model: You can allocate an array of size n in a constant amount of linear time...O(n). Tha advantage of proper memory allocation is that the amount of space you use is less or equal to the amount of time. 
* In real machine, word size(w) is usually 64 bits, or 256 (in bizaree instructions). Real machines has constant size RAM also.
  
* Dynamic Sequences: Be able to insert or delete elements in middle of the sequence. 

  * insert_at(i,X): make X the new Xi, shifting Xi to Xi+1, Xi+2, ..., Xn-1.
  * delete_at(i): Shift Xi+1 to Xi, Xi+2 to Xi+1, ..., Xn-1 to Xn.
  * insert/delete-first/last(X)/last(X): insert/delete X at the beginning/end of the sequence.

*Lecture left at 20:53 due to urgencies of life which I should learn to control....*

* Linked list: We store items in a bunch of nodes. Each node has an item in it. Each node has a pointer to the next node.
* In Python, dynamic arrays are lists. 
* The idea of dynamic arrays: 
  * Relax the constraint/invariant of the size of the array we use equals n(number of elements in a sequence).
  * Enforce that the size of the array is equal to O(n) > n
  * Maintain that the items in array A[i]=Xi
  * Geometric are dictated by the last term. 

### Problem Session Lecture: Asymptotic Behavior of Functions and Double Ended..

This is a problem set session. Watched it. 






