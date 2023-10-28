'''
This problem gives you a binary tree and asks you to return
all paths from the root node to each leaf node.
'''

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
'''
This approaches traverses the tree DFS style, keeping
a list of all the elements it has visited so far. When
it reaches a leaf node, it adds a copy of the list to
the final array, which then gets passed back at the end.
It uses the same list to keep track of all the elements
in a path as it traverses the tree to prevent extra
space from being allocated. It does this by adding 
the current element to the list before each recursive
call, and then deleting it right after.
The time complexity of this is O(N), because it 
visits each node once. The space complexity is
O(N log N) because in the worst case, the tree is
completely balanced and has approximately N/2
leaf nodes. So there would be a path of length 
log N (the height of the tree) for each of the leaf
nodes, resulting in an output of approximately size
(N/2) * log N.
'''
def all_paths_of_a_binary_tree(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    if not root:
        return []
    
    return dfs(root, [], [])

def dfs(root, curr_path, paths):
    if root.left is None and root.right is None:
        curr_path.append(root.value)
        paths.append(curr_path.copy())
        curr_path.pop()
        return paths
    
    curr_path.append(root.value)    
    if root.left:
        dfs(root.left, curr_path, paths)
    if root.right:
        dfs(root.right, curr_path, paths)
    curr_path.pop()
    
    return paths
