## Big O

Big O time is the language and metric used to describe the efficiency of algorithms. Big O is an important thing to master...Not understanding it thoroughly can really hurt you in developing an algorithm. Master it!

### An Analogy

* Let's say that you have a file of a given size to send to a friend across a country. You need to get the file to your friend as fast as possible. How should you send it?

* At first, most people would say email, FTP (File Transfer Protocol), or other means of electronic transfer. But that's half correct. Why?
* If the file is very big(say 1TB), you can't send it by email. A plane would be faster. Driving would also be fast. 

### Time Complexity

* Big O time or asymptotic runtime. We can define the data transfer runtime as: 
    * Electronic transfer: O(s), where s is the size of the file. This means that the time to transfer the file increase linearly with the size of the file. 
    * Airplane transfer: O(1) with respect to the size of the file. As the size of the file increases, it won't take any longer to get the file to your friend. Time is constant. 

There are many more runtimes such as O(Log N), O(N log N), O(N), O(N^2), and O(2^N). There is no fixed runtime. 

### Best Case, Worst Case, and Expected Case

* Best, worst and expected case describe the big O(or big theta) time for a particular inputs or scenarios. Big O, big omega, and big theta describe the upper, lower, and tight bounds for the runtime. 

Let's think about these 3 cases wrt to quick sort. Quick sort picks a random element as a pivot and then swap values in the array such that the elements less than pivot appear before elements greater than pivot, resulting in a partial sort. Then it recursively sorts the left and right sides using a similar process. 

* best caseL if all elements are equal, then the quick sort will traverse through the array once. This is O(N).
* worst case: if the pivot is repeatedly the biggest element in array, then the quick sort will degenerate to an O(N^2) runtime.

* Expected case: something terrible can happen. sometime the pivot will be very low or high but it won't happen over and over again. 


Best case scanario is not useful concept. 

### Space Complexity

* Time is not the only thing that matters in an algorithm. We might also care about the amount of memory or space required by the algorithm. 
* Space complexity is parallel concept to time complexity. If we need to create an array of size n, this will require O(n) space. If we need a two dimensional array of size nxn, this will require O(n^2) space.
* Big O allows us to express how the runtime scales. We just need to accept that it does not mean that O(N) is always better than O(N^2).

#### Adding vs multiplying algorithms

* If your algorithm is in the form "do this, when you are all done, do that, then you add the runtimes. 
* If your algorithm is in the form "do this for each time you do that, then you multiply the runtimes. 
* It's very easy to mess this up, so be careful!

Add the runtimes O(A + B)
```
for i in iteratorA:
    print(i)
for j in iteratorB:
    print(j)
```

Multiply the runtimes: O(A * B)
```
for i in iteratorA:
    for j in IteratorB:
        print(i + "," + b)
```

#### Amortized Time

* An array list or dynamically resizing array allows you to have the benefits of an array while offering flexbility in size. You won't run out of space since in the ArrayList since its capacity will grow as you insert elements. 
* The amortized time for inserting one element in array is O(1).
* X elements insertions take O(2X)

#### Log N RunTimes

* We use O(log N) in runtimes. Where does it come from? 
* Binary search: we are looking for an example x in an N-element sorted array. We first compare x to the midpoint of the array. If x  == middle, then we return. If x < middle, then we search on the left side of the array. If x > middle, we search on the right side of the array. 
  
```
search 9 within {1,5,8,9,11,13,15,19,21}
    compare 9 to 11 -> smaller.
    search 9 within {1,5,8,9,11}
        compare 9 to 8 -> bigger
        search 9 within {9,11}
            compare 9 to 9
            return
* We start off with an N-element array to search. Then, after a single step, we're down to N/2 elements. One more step, and we're down N/4 elements. We stop when we either find the value or we're down to just one element.
* The total runtime is then a matter of how mahy steps (dividing N by 2 each time) we can take until N becomes 1. 
* When you see a problem where the number of elements in the problem space get halved each time, that will likely be a O(log N) runtime. 
* So, that's why finding an element in a binary search tree is O(log N). With each comparison, we go either left or right. Half the nodes are on each side, so we cut the problem space in half each time. 

* WHen you have a recursive function that makes multiple calls, the runtime will often(but not always) look like (branches^depth), where branches is the number of times each recursive call branches....Giving us O(2^N)

* The space complexity of this algorithm will be O(N). Although we have O(2^N) nodes in the tree total, only O(N) exist at any given time. Thus, we need to have O(N) memory available. 

** Do some exercises!!!