'''
This problem gives you a binary tree and asks you to find the lowest common ancestor (LCA)
of two nodes in the tree. The LCA of two nodes is the lowest node in the tree that is an
ancestor of both, and a node can be an ancestor of itself.
'''

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
'''
This is a bottom-up approach that traverses the whole tree one time, and for each node
(and for each recursive call), it creates a left and a right variable, which stores
either one of the input nodes, if found, the LCA, if found, or None otherwise.
The logic is that if both of these variables have a node in them, then that means that 
either p or q (one of the input nodes) was found in the left subtree, and the other 
one was found in the right subtree, so the current node is the LCA and that gets returned 
up the recursive call chain. Or, if the current node is one of the nodes, and either of these
variables has the other node, then the current node is also the LCA (because a node can be
an ancestor/descendant of itself). In this case, the current node also gets returned up the
recursive call chain. In the end, the LCA bubbles up to the original call and is returned
as the final answer.
Time complexity is O(N) because it visits each node at most once and does a constant amount
of work for each one. The space complexity is O(N) because the call stack might reach a 
height of N if the tree is completely skewed, and it creates a constant amount of space 
for each call.
'''
def lca(root, a, b):
    """
    Args:
     root(BinaryTreeNode_int32)
     a(BinaryTreeNode_int32)
     b(BinaryTreeNode_int32)
    Returns:
     int32
    """
    return helper(root, a, b).value

  
def helper(root, p, q):
    if not root:
        return None

    found_node = root.value == p.value or root.value == q.value

    if found_node:
        return root
    
    left = helper(root.left, p, q)
    
    if left and left.value != p.value and left.value != q.value:
        # We found the LCA, no need to continue DFS
        return left
    
    right = helper(root.right, p, q)

    if (left and right) or (found_node and (left or right)):
        # The LCA is found
        return root
    elif left or right:
        return left or right
