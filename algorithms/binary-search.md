### Binary Search

* Binary search is one of the fastest algorithms that are used for searching a given key in a sorted array. 
* To search the key `q` in an array of keys `S`, we have to compare q to the middle key `S[n/2]`. 
  * If `q` is in the top half of `S[n/2]`, keep it there and recursively repeat the process. 
  * If the `q` appears to be in bottom half of `S[n/2]`, keep it there and recursively repeat the process. 
* The runtime of locating the key `q` in any half of the array is `Olog(n)`.
* Binary search can be used to count the number of times a given key occurs in a sorted array. 
  * Sorting groups all copies of same element in a sequential block. Thus, you can simply find the index of the right block in O(log n) time. 
  * The difference between the indices of the left and the right boundaries gives the count of occurences of a key being searched.
  * This algorithm can run in `O(log n+s)` time where s is the number of times a particular key appears in the sorted array. 
  * As you can understand, such runtime is bad if there are many identical keys in the array. 
* If we are searching a given key that lies close to our current position in a given array, we can use One-sided binary search.

* Like merge sort and quick sort, binary search is also based on the `divide and conquer rule`. 

```
Some important notes about quick sort and merge sort:
- Merge sort: Sort a given array by dividing it between two equal halves. Recursively sort each half and combine the results at the end. The runtime of merge sort is `O(nlogn)`. 
- Quick sort: Sort a given array by picking either a last or first element as pivot. Divide the array into two parts, one part that is less than the pivot and the other part that is greater than the pivot. Recursively sort each part and combine the results. The worst case runtime of quick sort is `O(n^2)`. The average runtime is `O(nlogn)`. If we pick a random value as a pivot in array, it's randomized quick sort. Its runtime is `O(nlogn)`. 
```

Let's talk more about divide and conquer rule. 

#### Divide and Conquer rule

* One of the most effective way of solving problems is to break them into smaller pieces. Solving smaller problems is like icing on cake. Haha, just like this supervised learning...`If intelligence is a cake, the bulk of the cake is unsupervised learning, the icing on the cake is supervised learning, and the cherry on the cake is reinforcement learning”- Yann LeCun` 
* So, when we divide the problem into smaller similar problems, we can resursively solve each problem and combine the result to form a full solution. 
* Divide and conquer also foster parallel processing. Different jobs can be decomposited into many tasks on each task can be processed independently on each processor. With the advent of cluster computers and multicore processors. 
* The above idea is applied in training deep networks. A large network can splitted on multiple GPUs so as to train faster. 
* Divide and conquer is also applied in dynamic computing. More on it later. 
* Whenever it takes smaller time to merge the results of resolved subproblems than solving those subproblems, we get an efficient algorithm. Example is Merge sort. It takes a linear time to merge two sorted lists of n/2 elements, where each element was obtained in `O(nlogn)` time.
* Divide and conquer is an important design technique that is used in sorting(merge sort, quick sort), binary search, [fast fourier transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform), and [strassen's matrix multiplication algorithm](https://en.wikipedia.org/wiki/Strassen_algorithm).
* The runtime of a divide and conquer algorithm is `T(n) = aT(n/b) + f(n)`, where a is a piece of size n/b. f(n) is the time to combine the solutions from all subproblems. Below are examples:
  * Sorting: The runtime of merge sort is `T(n) = 2T(n/2) + O(n)`. The first term is due to that the algorithm divides the data into equal halves, and the second time denotes a linear time of merging the halves after they are sorted. The resulting runtime is `T(n) = O(nlg n)`.
  * Binary search: The runtime of binary search is `T (n) = T (n/2) + O(1)` since at each step we spend constant time to reduce the problem to an instance half its size. The resulting runtime is `T (n) = O(lg n)`. 

The next is the implementation of the binary search using divide and conquer technique. 