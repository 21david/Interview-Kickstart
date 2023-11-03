'''
This problem gives you an edge list, along with how many nodes there are in
the graph, and asks you to turn it into an adjacency list.
'''

def convert_edge_list_to_adjacency_list(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_list_int32
    """
    
    adj_list = [[] for _ in range(n)]
    
    for start, end in edges:
        adj_list[start].append(end)
        adj_list[end].append(start)
        
    for list in adj_list:
        list.sort()
    
    return adj_list
