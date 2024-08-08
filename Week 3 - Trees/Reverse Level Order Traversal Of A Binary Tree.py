'''
This problem is equivalent to LeetCode 107. Binary Tree Level Order Traversal II
https://leetcode.com/problems/binary-tree-level-order-traversal-ii
'''

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def reverse_level_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    ans = []
    q = deque([root])
    
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.value)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        ans.insert(0, level)
    
    return ans
