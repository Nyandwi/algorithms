
## Breadth-First Search

References:
* Introduction to Algorithms - MIT - Book
* MIT Intro to Algorithms - [Notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2020/lecture-notes/MIT6_006S20_r09.pdf)
* Algorithms Design Manual by Skienna

* Before we talk about Breadth-First Search, let's talk about traversing a graph.

#### Traversing a Graph

* The most important graph problem is to systematically visit every edge and vertex in a graph in a systematic way. 
* Take an example for Maize puzzle which can be represented as a graph, and where each graph vertex denotes a junction of the maize and each graph edge denotes a hallway in the maize. To effectively gets out of the arbitarly maize, our graph traversal algorithm must be powerful enough. For efficiency, we must not get trapped in the maze or visit the same place repeatedly. For correctness, we must traverse the graph in a systematic way to be able to get out of the maize. Our search must takes us through every edge and vertex in the graph. 
* When traversing a graph, we must mark each vertex we visited to keep track of vertices that are yet to be visited. 
* In traversing a graph, every vertex will have 3 main states:
  * `Undiscovered`: a vertex in initial state, not discovered yet.
  * `Discovered`: vertex has been found, but have not yet checked out all incident edges. 
  * `Processed`: The vertex after we have visited all its incident edges. 

* A vertex must be `discovered` to be `processed`. So, traversing a graph is a sequential process that goes from `undiscovered` to `discovered`.
* To completely explore a vertex v, we must evaluate all vertices leaving it. If an edge goes to undiscovered vertex x, it is marked x and it must be added to vertices to be explored. We ignore edge that goes to a processed vertex. We also ignore any edge that goes to discovered but not processed vertex because the destination may already exists on the list of vertices to process.  
* Each undirected edge will be considered twice. Directed edges are considered only once when exploring the source vertex. 
* Eventually, every edge and vertex in the graph must be visited. 
* Now let's talk about breadth-first search. 

### Breadth-First Search(BFS)

* Breadth-first search is one of the simplest and important algorithms for searching a graph. It can be used for minimum spanning tree algorithm and Dijkstra's single-source shortest paths problems. 
* Given the graph G = (V,E), and distinguished vertex s, breadth-first search systematically explores the edges of G to `discover` every vertex that is reachable from s. It does that by computing the distance(smallest number of edges) from s to each reachable vertex. 
* It produces a `breadth-first tree` with root s that contains all reachable vertices. With the exception of root, each node in the tree has only one parent node. And that makes breadth-first searches a suitable searching algorithm for shortest path problems.
* Breadth-first search is named so because it expands the frontier between discovered vertices and undiscovered vertices unformly across the breadth of the frontier. Simply put, the algorithm discovers all vertices at distance k from s before discovering any vertices at distance k+1. 
* As we saw above in graph traversal, in order to keep track of progress, BFS colors each vertex white, gray, or black. In the beginning, all vertices are white(undiscovered), but when a given vertex is `discovered` for the first time, it change color to gray and then black...just to track the discovered vertices and vertices that are yet to be discovered. Both gray and black vertices are discovered vertices, but BFS distinguishes between them to ensure that the search proceeds in a breadth-first manner. All gray vertices may have adjacent vertices that are not discovered yet, but all adjacent vertices in black vertex have been discovered and processed. 

How the BFS construct a breadth-first tree:
* The breadth-first tree initially have its only root or source vertex s. 
* Whenever the search `discovers` a white vertex v in the course of scanning the adjacency list of an already discovered vertex u, the vertex v and the edge(u,v) are added to the tree. 
* All discovered vertices are stored in a queue, and they are processed in FIFO(first-in, first-out) manner. The oldest vertices or those that are close to the root are expanded first. 
* u is the `predecessor` or `parent` of v in the breadth-first tree. 
* Since every vertex is discovered at most once, it has only one parent. The `predecessor` and `descendent` relationships in the breadth-first tree are defined relative to the root vertex s.
* If u is on the simple path(no self-loop) in the tree from the root s to vertex v, then u is an ancestor or parent of v and v is a descendant or child of u. 
* The graph `G = (V,E)` is represented using adjacency lists.
* The runtime of BFS is `O(V+E)`, where V are no of vertices and E edges. 

#### BFS Summary:
* In BFS, all vertices are undiscovered in the beginning. 
* All vertices that are reachable from the source vertices are discovered first. In other words, all outgoing vertices of source vertex are discovered first. The outgoing vertices of the vertices being discovered are in state of `undiscovered`. 
* The discovered vertices are stored in queue and they are stored stored in queue, the vertices that were discovered first are processed first in FIFO manner(first-in, first-out).
* Breadth: width...Discover all adjacent vertices first.
* As we will see in depth-first search, the main differences between DFS and BFS is how the discovered vertices are stored. In BFS, they are stored in queue, and in DFS(FIFO), they are stored in stack(LIFO).

Next step:
* Revise the notes and make sure I understand them. 
* Implement the breadth first search
* Watch MIT Lecture 9: BFS