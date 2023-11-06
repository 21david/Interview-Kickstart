'''
This problem gives you a graph which may have multiple components
and asks you to count how many components it has.
The graph is given as an integer that describes how many nodes there
are, and a list of the edges that exist between the nodes.
'''

'''
This approach goes through each node and starts a DFS on it
if it hasn't been already visited. It counts how many DFSs
it starts, and that results in the number of separate 
components found in the graph.
The time complexity is O(N + M) because we traverse the
list of edges to create an adjacency list, we loop once
over each node, and all the DFSs combined visit each node
one time. The DFS also does constant work for each edge in
the graph.
The auxiliary space complexity is O(N + M) because we build
an adjacency list of length N and spread all the edges into
the lists. Also, the 'visited' array is as long as the number
of nodes, and the DFS can reach a call stack of height N in 
the worst case.
'''
def number_of_connected_components(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     int32
    """

    # Build an adjacency list
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # DFS code
    visited = [False] * n
    def dfs(node):
        visited[node] = True
        for nei in graph[node]:
            if not visited[nei]:
                visited[nei] = True
                dfs(nei)

    # Iterate through each node and count how 
    # many DFSs are necessary
    count = 0    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
        
    return count
