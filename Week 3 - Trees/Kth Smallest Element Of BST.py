"""

"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def kth_smallest_element(root, k):
    """
    Args:
     root(BinaryTreeNode_int32)
     k(int32)
    Returns:
     int32
    """
    """
    Optimal approach:
    Traverse to the smallest element in the BST.
    For (k-1) times, move to the next smallest element
    in the BST. The algorithm for moving to the next 
    smallest element is like this:
    1. If the node is a left child and it doesn't have a right child, move to the parent
    2. If the node has a right child, move to that child, then recursively move to its left-most child 
        (smallest element in that subtree)
    3. If the node is a right child and doesn't have a right child, move up to that node's
       first left child ancestor, then move up to that node's parent (this gets the next
       smallest element, basically leaving the current subtree it's on)
        If there is no grandparent, we've traversed all the nodes already (but k will always
        be in bounds so we don't need to check for this)
                          
    """
    
    # Move to smallest child
    temp = root
    nodes = {root: ('root', None)}
    parent = None
    while temp.left:
        parent = temp
        temp = temp.left
        nodes[temp] = ('L', parent)
            
    # temp is at the 1st smallest node
    
    # Move temp (k-1) times to get to the kth smallest element
    # We move it to the next smallest element each time
    k -= 1
    while k:
        if temp.right: # 2
            parent = temp
            temp = temp.right
            nodes[temp] = ('R', parent)
            while temp.left:
                parent = temp
                temp = temp.left
                nodes[temp] = ('L', parent)
        elif nodes[temp][0] == 'L':  # 1
            temp = nodes[temp][1]  # move to parent
        elif nodes[temp][0] == 'R':  # 3
            while nodes[temp][0] == 'R':
                temp = nodes[temp][1]
            temp = nodes[temp][1]
            
        k -= 1
    
    # return the final position of temp, which is the kth smallest value
    return temp.value
