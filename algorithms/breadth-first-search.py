### Implementation of breadth-first search algorithm

### See notes about BFS in the same repository: markdown file. 

### Implementation 1: 
# Reference: MIT Intro to algorithms: 
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2020/lecture-notes/MIT6_006S20_r09.pdf

def bfs(Adj, s):
    """
    Adj: Adjacency list of graph
    s: starting vertex
    """

    parent = [None for v in Adj]
    parent[s] = s
    level = [[s]]

    while 0 < len(level[-1]):
        level.append([])
        for u in level[-2]:
            for v in Adj[u]:
                if parent[v] is None:
                    parent[v] = u
                    level[-1].append(v)
    return parent


### Implementation 2: Suggested by Copilot
### It is slightly understandable

def breadth_first_search(graph, start):
    """
    Breadth-first search algorithm
    """
    queue = [start]
    visited = set()
    visited.add(start)
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited