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
Time complexity should be O(N). Traversing the
tree to create an array would visit each node once,
doing constant work every time (adding the value to
the end of the array). Returning the element at
index k-1 would be constant time.
The auxilliary space complexity should be O(N), 
because we create an array with every element
in the tree. Also, if the tree is completely
unbalanced, and the height is the number of nodes,
then the call stack would reach N, so the space
used by the call stack is also O(N).
The space complexity of the input is O(N), where N
is the number of elements in the tree.
The space complexity of the output is O(1) because
it just returns the kth smallest value (1 integer).
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



'''
The best approach is to do an in-order traversal, 
keeping track of how many elements you've traversed.
When you reach the kth element, you can set that
value to a global variable, and stop all further
recursive calls. This approach only visits the
first k nodes (in order), and only uses constant
extra space. The time complexity is O(k) because
we visit the first k nodes, and then return.
The space complexity is also O(k) because in the 
worst case, the call stack could reach a height
of k.
'''
def kth_smallest_element(root, k):
    """
    Args:
     root(BinaryTreeNode_int32)
     k(int32)
    Returns:
     int32
    """
    ''' 
    The first value will act as our counter, starting
    at k and ending at 0. The second element will store
    the kth value when it's found, and it will be
    returned at the end.
    '''
    vals = [k, 0]
    
    def inorder(root):
        # If kth element already reached
        if vals[0] == 0:  
            return
        
        if root is None:
            return
        
        inorder(root.left)
        
        vals[0] -= 1

        # If we just reached the kth element
        if vals[0] == 0:
            vals[1] = root.value
            return
        
        inorder(root.right)
        
    inorder(root)
    
    return vals[1]
