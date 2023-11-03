'''
This problem gives you an edge list, like:
[
[0, 1],
[1, 4],
[1, 2],
[1, 3],
[3, 4]
]
along with the number of nodes in the graph, and asks you to 
turn it into an adjacency matrix.
'''

def convert_edge_list_to_adjacency_matrix(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_list_bool
    """
    
    matrix = [ [False] * n for _ in range(n)]
    
    for u, v in edges:
        matrix[u][v] = True
        matrix[v][u] = True
    
    return matrix
