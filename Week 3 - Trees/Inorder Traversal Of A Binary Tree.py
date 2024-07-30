"""
This problem gives you the root of a binary tree and asks you to return
its in-order traversal as an array.

Example:
    0
   / \
  1   2
 / \
3   4

Output:
[3, 1, 4, 0, 2]
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def inorder(root):
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
        ans.append(root.value)
        traverse(root.right)
        
    traverse(root)
    
    return ans
