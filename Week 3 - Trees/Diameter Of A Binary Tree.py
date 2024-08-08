'''
This problem is equivalent to LeetCode 543. Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree
'''

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def binary_tree_diameter(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    '''
    For every node, we must know the sum of the height of its left and right subtrees. 
    If we know that for every node, the greatest of them is the diameter for the whole tree.
    '''
    max_dia = 0
    
    def dfs(node, d):
        nonlocal max_dia
        
        if not node:
            return 0
        
        left = dfs(node.left, d+1)
        right = dfs(node.right, d+1)
        
        max_dia = max(max_dia, left + right)
        
        return 1 + max(left, right)
    
    dfs(root, 0)
    return max_dia
