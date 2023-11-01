'''
This problem gives you a binary tree and asks you to flip it upside down.
The binary tree has specific rules. Each node can only have 0 or 2 children,
and each right node is a leaf node.

It is equivalent to LeetCode problem 156.
https://leetcode.com/problems/binary-tree-upside-down
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
In this approach, I created 3 lists using the tree's values.
In the first list, I stored all the parent values. In the second list,
I stored the parent of each node in list 1. In the third list, I
stored the right brother of each node in list 1. With these values,
I constructed a flipped version of the binary tree.
'''
def flip_upside_down(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    '''
    Example tree:
            1
          /   \
         2     3
        / \
       4   5
      / \
     6   7
    '''
  
    # [1, 2, 4, 6]. - nodes /  nodes
    # [N, 1, 2, 4]. - parent nodes / right nodes
    # [N, 3, 5, 7] - brother nodes / left nodes
    
    if not root:
        return None
    
    list1, list2, list3 = [], [], []
    stack = [root]
    parent = None
    
    while len(stack) > 0:
        cur_node = stack.pop()
        if not cur_node:
            break
        list1.append(cur_node.value)
        list2.append(parent.value if parent else None)
        list3.append(parent.right.value if parent else None)
        
        parent = cur_node
        stack.append(cur_node.left)

    # Construct the tree
    root = BinaryTreeNode(list1[-1])
    cur_node = root
    
    i = len(list1) - 1
    while i >= 1:
        cur_node.right = BinaryTreeNode(list2[i])
        cur_node.left = BinaryTreeNode(list3[i])
        
        cur_node = cur_node.right
        i -= 1
    
    return root



'''
In this approach, I traversed the tree with a recursive DFS, and once I reached
the bottom node, I started rewiring the left and right children.
'''

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def flip_upside_down(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    
    if not root:
        return None
    
    def helper(node, parent):
        if node.left and node.right:
            helper(node.left, node)
        else:
            nonlocal root
            root = node
        
        if parent: 
            node.left = parent.right
            node.right = parent
        else: 
            node.left = None
            node.right = None
            
    helper(root, None)
    
    return root
