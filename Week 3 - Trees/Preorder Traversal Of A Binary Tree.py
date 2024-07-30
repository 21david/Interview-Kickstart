"""
This problem gives you the root of a binary tree and asks you to return
its pre-order traversal as an array.

Example:
    0
   / \
  1   2
 / \
3   4

Output:
[0, 1, 3, 4, 2]
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def preorder(root):
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
        
        ans.append(root.value)
        traverse(root.left)
        traverse(root.right)
    
    traverse(root)
    
    return ans
