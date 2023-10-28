'''
This problem asks to find the height of a binary tree.
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
This is a bottom-up approach. It travels to the leaf nodes,
and starts traveling back up, keeping track of the depth found.
The parent nodes return the maximum height of its two children,
and thus the root node returns the maximum height of the tree.
The time complexity is O(N) because each node must be visited
once. The space complexity is O(N) because the tree may be 
a chain of left or right children in the worst case, so the 
stack call would reach a height of N.
'''
def height_of_binary_tree(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    if root is None:
        return 0
    
    return 1 + max(height_of_binary_tree(root.left), height_of_binary_tree(root.right))
