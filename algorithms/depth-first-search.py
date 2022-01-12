## Depth-first search Python implementation

## Reference: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2020/lecture-notes/MIT6_006S20_r10.pdf

def dfs(Adj, s, parent=None, order=None):
    """
    Adj: Adjacent list
    s: starting vertex
    """
    if parent is None:
        parent = [None for v in Adj]
        parent[s] = s
        order = []

    for v in Adj[s]:
        if parent[v] is None:
            parent[v] = s
            dfs(Adj, v, parent, order)
    order.append(s)
    return parent, order

# Runtime: O(V+E)

## Full graph search

def full_dfs(Adj):
    """
    Adj: Adjacent list
    """
    parent = [None for v in Adj]
    order = []

    for v in range(len(Adj)):
        if parent[v] is None:
            parent[v] = v
            dfs(Adj, v, parent, order)
            
    return parent, order