'''
This problem is equivalent to LeetCode 429. N-ary Tree Level Order Traversal
https://leetcode.com/problems/n-ary-tree-level-order-traversal
'''

"""
For your reference:
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
"""
def level_order(root):
    """
    Args:
     root(TreeNode_int32)
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
            
            for child in node.children:
                q.append(child)
        
        ans.append(level)
    
    return ans
