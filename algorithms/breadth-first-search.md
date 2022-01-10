
## Breadth-First Search


* Before we talk about Breadth-First Search, let's talk about traversing a graph. 

#### Traversing a Graph

* The most important graph problem is to systematically visit every edge and vertex in a graph in a systematic way. 
* Take an example for Maize puzzle which can be represented as a graph, and where each graph vertex denotes a junction of the maze and each graph edge denotes a hallway in the maze. To effectively gets out of the arbitarly maize, our graph traversal algorithm must be powerful enough. For efficiency, we must not get trapped in the maze or visit the same place repeatedly. For correctness, we must traverse the graph in a systematic way to be able to get out of the maize. Our search must takes us through every edge and vertex in the graph. 
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

### Breadth-First Search



