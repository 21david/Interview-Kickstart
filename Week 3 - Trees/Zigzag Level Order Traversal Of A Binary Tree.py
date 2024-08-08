'''
This problem is equivalent to LeetCode 103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
'''

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def zigzag_level_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    ans = []
    odd_level = True
    q = deque([root])
    
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            
            if odd_level:
                level.append(node.value)
            else:
                level.insert(0, node.value)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        odd_level = not odd_level
        ans.append(level)
    
    return ans
