'''
This problem gives you a graph, in the form of edges and number of nodes
in the graph, and asks you to check if it forms a valid tree.
The input is an integer, indicating how many nodes there are, and two
arrays, edge_start and edge_end, where edge_start[i] is the origin of 
an edge, and edge_end[i] is the destination of an edge, for all i.
'''
'''
Solution 1:
The number of edges needs to be 1 less than the number of nodes
for there to be a possibility of the graph being a valid tree.
If it is equal to or greater, then there is at least 1 cycle
in the graph. If it is lesser, then the graph consists of more 
than 1 connected component.
So we can first check for that. If it is, then we just need to
check that there are either no cycles in the graph, or that the
graph is 1 connected component. I think it is more optimal to check
for no cycles, because we could traverse the graph with a BFS/DFS, 
and if it ever tries to visit a node that it already visited (other
than the node it just came from), then the algorithm could stop
right away, rather than trying to traverse the whole tree.
'''
def is_it_a_tree(node_count, edge_start, edge_end):
    """
    Args:
     node_count(int32)
     edge_start(list_int32)
     edge_end(list_int32)
    Returns:
     bool
    """
    if len(edge_start) != node_count - 1:
        return False
    
    # Build adjacency list for DFS
    adj_list = [[] for _ in range(node_count)]
    
    for i in range(len(edge_start)):
        u, v = edge_start[i], edge_end[i]
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Do a DFS and look out for a cycle
    visited = set()
    found_cycle = [False]
    def dfs(node, parent):
        if found_cycle[0]:
            # Don't continue DFS if cycle is already found
            return
        visited.add(node)
        for nei in adj_list[node]:
            if nei != parent and nei in visited:
                # Found a cycle
                found_cycle[0] = True
                return
            if nei not in visited:
                dfs(nei, node)
    
    dfs(0, None)
    return len(visited) == node_count and not found_cycle[0]


'''
Solution 2:
Do a BFS, keeping track of how many tree edges are in the
BFS tree, and compare that with the total number of edges.
There should be as many tree edges as total edges. If there
are less tree edges than total edges, then the graph is split
If there are more total edges, then it is nor a valid tree,
because there is a cycle somewhere.

An optimization that can be done is to check if the number of
edges equals 1 less than the number of nodes. If not, the 
answer is already false, because a tree always has 1 less edge
than number of nodes.
'''
def is_it_a_tree(node_count, edge_start, edge_end):
    """
    Args:
     node_count(int32)
     edge_start(list_int32)
     edge_end(list_int32)
    Returns:
     bool
    """
    if len(edge_start) != node_count - 1:
        return False
    
    # Build adjacency list for DFS
    adj_list = [[] for _ in range(node_count)]
    
    for i in range(len(edge_start)):
        u = edge_start[i]
        v = edge_end[i]
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Do a DFS and count tree edges
    visited = [False] * node_count
    tree_edges = [-1]
    def dfs(node):
        tree_edges[0] += 1
        visited[node] = True
        for nei in adj_list[node]:
            if not visited[nei]:
                dfs(nei)
    
    dfs(0)
    
    # The # of tree edges must be the # of total edges
    return tree_edges[0] == len(edge_start)


'''
Solution 3:
Count number of edges and check how many connected components there are.
If there is 1 CC and there are n-1 edges, where n is # of nodes,
then it should be a valid tree. 
'''
def is_it_a_tree(node_count, edge_start, edge_end):
    """
    Args:
     node_count(int32)
     edge_start(list_int32)
     edge_end(list_int32)
    Returns:
     bool
    """
    # Build adjacency list for DFS
    adj_list = [[] for _ in range(node_count)]
    
    for i in range(len(edge_start)):
        u = edge_start[i]
        v = edge_end[i]
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Do a DFS and check if it visited every node
    visited = set()
    def dfs(node):
        visited.add(node)
        for nei in adj_list[node]:
            if nei not in visited:
                dfs(nei)
    
    # Run DFS and check if it visited every node
    # If not, then graph is not 1 component and thus not a valid tree
    dfs(0)
    if len(visited) != node_count:
        return False
    
    # If it is, then it is only a valid tree if the number of edges is n-1
    return len(edge_start) == node_count - 1
