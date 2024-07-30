"""
This problem gives you the root of a binary tree and asks you to return
its post-order traversal as an array.

Example:
    0
   / \
  1   2
 / \
3   4

Output:
[3, 4, 1, 2, 0]
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def postorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    ans = []
    
    def traverse(root):
        if not root:
            return
        
        traverse(root.left)
        traverse(root.right)
        ans.append(root.value)
        
    traverse(root)
    
    return ans
