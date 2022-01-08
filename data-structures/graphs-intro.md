## Introduction to Graphs

* Graphs are one of the most important data structure in computer science. They are everywhere. 
* Graphs are abstract representation that describes the organisation of transportation systems, human interactions, social networks, electronic circuits, and computer networks....
* A graph `G=(V,E)` consists of vertics V(also called nodes or points) together with vertices pair or edges E(also called links or lines). The vertices pairs can be ordered or unordered. 
* Graphs are so powerful that they can be used to represent any kind of relationship. That is to say that most computational problems can be solved with graphs. Example: electronic circuits can be modelled as graphs, with junctions as vertices and components as edges. Also neural networks can be represented as graphs, where the neurons are edges and the layers(?) as vertices.
* If we analyze a computer program as graphs, the vertices can be lines of codes, with an edge connecting lines x and y if y is the next statement executed after x. 
* Also, a network of roads can be modelled as graphs, where cities are vertices and road between cities are edges. 
* Thus, most algorithmic problems can be solved as graphs. 
* It is extremely difficult to design novel algorithms. The secret sauce of designing new and efficient graphs algorithm is to understand the existing ones and learn from there. Being familiar with many different graph problems is very important than mastering one particular graph algorithm. 
  
* Let's see types of graphs.

#### Types of Graphs

* Undirected vs directed: A grapg G is undirected if edge E (x,y) implies that (y,x) is also in E. Otherwise, the graph is directed. 