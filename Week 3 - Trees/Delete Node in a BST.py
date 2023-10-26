'''
The problem asks to delete the given nodes of a binary search tree (BST),
where the BST follows the rule where every all nodes in the left subtree
of a node are lesser than it, and all nodes in the right subtree of it
are greater than it. The BST does not have to be balanced.
'''

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def delete_from_bst(root, values_to_be_deleted):
    """
    Args:
     root(BinaryTreeNode_int32)
     values_to_be_deleted(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    
    for val in values_to_be_deleted:
        root = delete_val_from_bst(root, val)
    
    return root
    
def delete_val_from_bst(root, val):
    '''
    To delete from a tree, we must first search for the node,
    keeping track of it's parent. If the node is never found,
    we can just return the root. If it is found, then there
    are three cases to handle:
    1. The node has no children.
        - This is the easiest case because we can just
          set the spot where this node was at to null.
    2. The node has one child (left or right).
        - This is rather simple to handle. We can just set
          the spot where this node was at to it's only child,
          which successfully deletes the node without
          invalidating the BST structure.
    3. The node has two children.
        - For this case, the best way to keep the BST structure
          valid is to replace the node with either it's
          predecessor or its successor, and then delete that
          predecessor or successor (which should be much easier).
          So if we pick the successor route, then we can just search
          for the successor, keeping track of the previous node
          (the parent node), replace the node with it's successor,
          and delete the successor, which would use the same logic
          as in case 1 or 2 (because the successor is guaranteed to
          not have a left child).
    There are also a few edge cases to take care of, like the root
    being the node we want to delete.
    '''
    # Search for the node to be deleted
    prev = None
    curr = root
    while curr is not None and curr.value != val:
        prev = curr
        curr = curr.left if val < curr.value else curr.right
        
    # If curr is None, then the element wasn't in the tree
    if curr is None:
        return root
        
    # Now we have found the node and are sure it exists
    
    # Case 1: The node has no children
    if curr.left is None and curr.right is None:
        # Edge case where the node is the root
        if prev is None:
            return None
            
        if prev.left == curr:
            prev.left = None
        else:  # if prev.right == curr
            prev.right = None
        return root
            
    # Case 2: The node has only a left or right child
    if not (curr.left is not None and curr.right is not None):
        # Edge case where the node is the root
        if prev is None:
            if curr.right is not None:
                return curr.right
            else:
                return curr.left
        
        temp = None
        if curr.right is not None:  # if it only has the right child
            temp = curr.right
        else:  # if it only has the left child
            temp = curr.left
            
        # Replace curr with the temp (its child), which deletes curr
        if prev.left == curr:
            prev.left = temp
        else:
            prev.right = temp
        return root
        
    # Case 3: The node has both children
    '''
    We must find the successor, set the node to be deleted to the
    successor's value, then delete the successor node.
    The successor is guaranteed to not have a left child (because
    if it did, then that child would be the successor)
    '''
    # Search for successor
    succ = curr.right
    prev = curr
    while succ.left is not None:
        prev = succ
        succ = succ.left
    curr.value = succ.value
    # Delete successor
    if prev.left == succ:
        prev.left = succ.right
    else:  # prev.right == succ
        prev.right = succ.right
        
    return root
