'''
This problem gives you a BST (not guaranteed to be balanced) and
asks you to find the kth smallest element.

The tree nodes are represented with this class:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

The tree will always have at least one node. 
K will always be in the valid range.
'''

'''
Brute force approach is to turn the BST into an
array, and return the element at index k-1.
We can use an in order traversal to turn it into
an array.
'''
def kth_smallest_element(root, k):
    """
    Args:
     root(BinaryTreeNode_int32)
     k(int32)
    Returns:
     int32
    """
    array = []
    
    def to_array(root):
        if root is None:
            return
        to_array(root.left)
        array.append(root.value)
        to_array(root.right)
        
    to_array(root)
    
    return array[k-1]
