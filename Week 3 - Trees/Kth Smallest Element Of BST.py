"""
This problem gives you a BST (binary search tree) and an integer k, and asks you to return the
kth smallest element in the BST.

Example:
  2
 / \
1   3

k = 3

Output:
3
(3 is the 3rd smallest element)

"""

"""
Solution 1
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
    Since it is a BST, an in-order traversal will traverse the tree
    in order from least to greatest. So a brute-force solution is to
    turn the tree into a sorted array, and then return the element at
    index k-1. (First smallest number is at 0, second smallest is at 1,
    etc.)

    Time complexity: O(N), where N is the number of nodes in the tree, 
    because it has to traverse the entire tree first.

    Space complexity: O(N), because it has to create an array of size N
    """
    arr = []
    def traverse(root):
        if not root:
            return
        
        traverse(root.left)
        arr.append(root.value)
        traverse(root.right)
        
    traverse(root)
    
    return arr[k-1]



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

    The optimization is that this algorithm doesn't have to traverse every single node to find
    the answer. If k = 1, it will find the smallest element and stop there. And the 'nodes'
    dictionary will stop growing as soon as it finds the answer.

    Time complexity:
    In the worst case, k = N, and the tree is more like a linked list on its left side, so
    the algorithm would travel down to the leaf node, then work its way back to the root node.
    This would be O(N).
    In the best case, k = 1 and the tree is like a linked-list on its right side, so the algorithm
    would already be at the smallest element and return the answer right away. O(1).
    In the case where the tree is balanced, finding the smallest element would be O(logN). Then, 
    finding the next smallest element can be either O(1) or O(logN). Since that happens k times,
    the time complexity should be O(k * logN)

    Space complexity:
    In the worst case, all nodes are added to the dictionary. O(N).
    In the best case, only the root is added to the dictionary. O(1).
    In the cases where the tree is balanced, the space complexity is the same as the time complexity
    because every node that is visited is added to the dictionary. O(N).
    """
    # Key is a pointer to the node
    # Value is a tuple. First element says whether it's a left child, root node, or right child
    # Second element is a pointer to its parent
    nodes = {root: ('root', None)}

    # Move to the smallest element
    parent = None
    temp = root
    while temp.left:
        parent = temp
        temp = temp.left
        nodes[temp] = ('L', parent)
            
    # temp is at the 1st smallest node at this point
    
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
    
    # Return the final position of temp, which is the kth smallest value
    return temp.value
