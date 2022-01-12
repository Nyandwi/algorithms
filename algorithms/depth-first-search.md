## Depth-First Search(DFS)

* Previously, we learned about breath-first search or BFS. In BFS, we explore all vertices that are reachable from the source vertex and all discovered vertices are stored in queue data structure and are processed in order of FIFO(first in, first out).
* Depth-First Search and Breadth-First Search are all primary searching algorithms. For most problems, it doesn't matter which you use, but for few, it matters.
* Both DFS and BFS provides a search mechanism to visit each edge and vertex of the graph. The difference between them is the order in which they explore vertices, and such order depends on the container data structure that is used to store `discovered` vertices that are yet to be `processed`. Those data structure are queue and stack. Below is the difference between them.
* ***Queue***: Discovered vertices are stored in FIFO queue. The vertices that were discovered first are processed first. The discovering or exploring journey starts from slowly from the source vertex, discovering all reachable vertices from it(the source vertex). This is in fact the mechanism of breadth-first search. Width first.
* ***Stack***: Vertices are stored in LIFO(last in, first out) stack. We explore or discover all outgoing edges of the most recently discovered vertex v that still has undiscovered edges leaving it. Once all of v's edges have been explored, the search "backtracks" to explore edges leaving the vertex from which v was discovered. Such process continues until we have discovered all the vertices that are reachable from orginal source vertex. If any undiscovered vertices remains, then the depth first search selects one of them as a new source, and it repeats the search from that source. DFS repeats this entire process until it has discovered every vertex. 
* DFS in simple words: Explore the outgoing edges of a given vertex v, finish them, go back to explore all other edges leaving the vertex from which v was discovered, continue until all edges from source vertex are explored...So, depth first, go deep first, come back and go deep. and again, and again. 
* DFS is a recursive graph traversal approach. 
* Below is the pseudocode of depth-first search. 

```
# Reference: Algorithm Design Manual, Skienna
DFS(G,u):
    state[u] = "discovered"
    process vertex u if desired
    entry[u] = time
    time = time + 1
    for each v in Adj(u):
        process edge (u,v) if desired
        if state[v] = "undiscovered" then
            p[v] = u
            DFS(G,v)
    state[u] = "processed"
    exit[u] = time
    time = time + 1
```

* Time is an important factor in DFS tree. If x is an ancestor or parent of y in DFS tree, it means we must traverse through x before y(just as a child can not be born before his/her parent). Also, we must exit y before we exit x, because the mechanics of DFS ensure we can not exit x until after we have backed up from the search of all its descendants.
* Also, the number of descendants/neighbors of a vertex v in DFS tree is equivalent to the difference between the exit and entry times of v.

### DFS Runtime

* A recursive DFS call is performed only when a vertex has not a parent pointer, and is given parent pointer immediately before the recursive call. 
* A recursive call is called on each vertex at most once. 
* The amount of work done by each recursive call search from vertex v is proportional to the number of outgoing edges of v, so it's O(E). 
* As the parent array has a length of V, the total runtime of DFS is O(V+E) time. 

### Full Graph Exploration

* In a graph, all vertices may not be reachable from the source vertex s.
* To search all vertices in a graph, one can use depth-first search(or breadth-first search) to discover each connected component in the graph by searching each vertex that has not been discovered yet by the search.

### Topological Sort

* Depth-first search can be used to perform topological sort on directed acyclic graph(DAG).
* DAG is a graph that doesn't contain directed cycle. 
* A topological sort of directed acyclic graph G = (V,E) is a linear ordering of the vertices such that for each edge(u,v) in E, vertex u appears before vertex v in the ordering.
* Reversing the order returned by DFS on acyclic graph will result in topological sort. 

* **A challenge**: A high school contains many student organization, each with its own hierarchical structure. For example, the school’s newspaper has an editor-in-chief who oversees all students contributing to the newspaper, including a food-editor who oversees only students writing about school food. The high school’s principal needs to line students up to receive diplomas at graduation, and wants to recognize student leaders by giving a diploma to student a before student b whenever a oversees b in any student organization. Help the principal determine an order to give out diplomas that respects student organization hierarchy, or prove to the principal that no such order exists.

* **Solution**: *Construct a graph with one vertex per student, and a directed edge from student a to b if student a oversees student b in some student organization. If this graph contains a cycle, the princi- pal is out of luck. Otherwise, a topological sort of the students according to this graph will satisfy theprincipal’srequest.RunDFSonthegraph(exploringthewholegraphasingraph explore) to obtain an order of DFS vertex finishing times in O(|V | + |E|) time. While performing the DFS, keep track of the ancestors of each vertex in the DFS tree, and evaluate if each new edge processed is a back edge. If a back edge is found from vertex u to v, follow parent pointers back to v from u to obtain a directed cycle in the graph to prove to the principal that no such order exists. Otherwise, if no cycle is found, the graph is acyclic and the order returned by DFS is the reverse of a topological sort, which may then be returned to the principal.*

Source: MIT Intro to Algorithms

### Summary of DFS
* Depth-first search is like breadth-first search but instead of using the queue(FIFO), it uses the stack(LIFO). The difference is the order in which they both explore vertices.
* A breadth-first search `discovers` vertices reachable from a queried vertex s `level-by-level` outward from s.
* A depth-first search also finds all vertices reachable from s, but does so by searching undiscovered vertices as deep as possible before exploring other branches.
* Instead of exploring all neighbors of s one after another as in a BFS, DFS searches as far as possible from the first neighbor of s before searching any other neighbor of s.
* Just as with breadth-first search, depth-first search returns a set of parent pointers for vertices reachable from s in the order the search discovered them, together forming a DFS tree.
* BFS tree represents shortest path, DFS does not.

Here is a great [demo of DFS](https://codepen.io/mit6006/pen/dgeKEN) by MIT Intro to Algorithms.

### References
* Algorithm Design Manual by Steven S.Skienna
* Introduction to Algorithms by Thoman H. Cormen
* [MIT Introduction to Algorithms](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2020/lecture-notes/), Lecture 10, DFS revised and [recitation](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2020/lecture-notes/MIT6_006S20_r10.pdf) notes.


```
FUNFACT
Vertex: nodes or points
Edge: links or lines

I keep confusing them.
```