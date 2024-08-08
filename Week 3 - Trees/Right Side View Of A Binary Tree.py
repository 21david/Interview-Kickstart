'''
This problem is equivalent to LeetCode 199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view
'''

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def right_view(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    last_in_level = []
    
    def dfs(node, depth):
        if not depth < len(last_in_level):
            last_in_level.append(node.value)
        else:
            last_in_level[depth] = node.value
            
        if node.left:
            dfs(node.left, depth + 1)
        
        if node.right:
            dfs(node.right, depth + 1)
        
    dfs(root, 0)
    
    return last_in_level
