'''
This problem is equivalent to LeetCode 112. Path Sum
https://leetcode.com/problems/path-sum
'''

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def path_sum(root, k):
    """
    Args:
     root(BinaryTreeNode_int32)
     k(int32)
    Returns:
     bool
    """
    answer = False
  
    def dfs(node, total):
        nonlocal answer
        
        if answer or not node:
            return
        
        if not (node.left or node.right):
            answer = (total + node.value) == k
            return
        
        dfs(node.left, total + node.value)
        dfs(node.right, total + node.value)
    
    dfs(root, 0)
    return answer
