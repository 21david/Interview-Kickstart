'''
This problem gives you a binary tree and an integer K and asks you to return all root-to-leaf paths
with a sum equal to K.

It is equivalent to LeetCode 113. Path Sum II
https://leetcode.com/problems/path-sum-ii/description/
'''

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def all_paths_sum_k(root, k):
    """
    Args:
     root(BinaryTreeNode_int32)
     k(int32)
    Returns:
     list_list_int32
    """
    
    all_paths = []
    
    def dfs(node, path, total):
        if not (node.left or node.right):  # leaf node
            if total + node.value == k:
                all_paths.append(path + [node.value])
            return
            
        
        path.append(node.value)
        
        if node.left:
            dfs(node.left, path, total + node.value)
            
        if node.right:
            dfs(node.right, path, total + node.value)
        
        path.pop()
    
    dfs(root, [], 0)
    return all_paths if all_paths else [[-1]]
