## Lecture 9: Breadth-First Search

* [Video](https://www.youtube.com/watch?v=oFVYVzlvk9c&list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY&index=14)
* [Notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2020/lecture-notes/MIT6_006S20_lec9.pdf)
* [Recitation(indepth notes)](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2020/lecture-notes/MIT6_006S20_r09.pdf):

Summary of the lecture:

* Graphs are everywhere: road network, social networks, computer nets, neural networks, etc...
* A simple graph is a graph that has no self loop. 
* Non simple graphs have self-loop. Non simple graphs are very complicated.
* We mostly deal with simple graphs
* The runtime of directed and undirected graphs: O(|V^2).
* Graphs are used to used to solve shortest path problems. 
* A shortest path is the length of the path that has fewest number of edges between any pair of vertices.
* The distance from the source vertex to itself is 0. 
* The runtime of breadth-first search algorithm is O(V^2 + E^2).