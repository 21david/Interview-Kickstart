'''
This problem gives you a sorted array and asks you
to build a balanced BST from it.

This is the given code for a tree node:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

The list will always have at least one node.
'''

'''
To build a balanced search tree using a sorted
array, then we can take the middle element, make
that one the root, and then call a helper function
(the current function in a recursive way)
to build BSTs from all the elements to the left 
and to the right, which will be the left and right
children.
'''
def build_balanced_bst(a):
    """
    Args:
     a(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    length = len(a)
    
    if length == 0:
        return None
    
    middle_index = len(a) // 2
    root_element = a[middle_index]
    root = BinaryTreeNode(root_element)
    
    root.left = build_balanced_bst(a[:middle_index])
    root.right = build_balanced_bst(a[middle_index+1:])
    
    return root



'''
An optimization to the previous solution is to 
use the original array for each recursive call 
along with start and end pointers that indicate 
the subset of the array to build a BST from. 
This reduces the auxilliary space used by about
half.
'''
def build_balanced_bst(a):
    """
    Args:
     a(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    
    def helper(arr, start, end):
        length = end - start + 1
        
        if length == 0:
            return None
        
        middle_index = start + (length) // 2
        root_element = arr[middle_index]
        root = BinaryTreeNode(root_element)
        
        root.left = helper(arr, start, middle_index-1)
        root.right = helper(arr, middle_index+1, end)
        
        return root
    
    return helper(a, 0, len(a)-1)
