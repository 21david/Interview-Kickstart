'''
This problem gives a binary tree and asks you if the tree is
symmetric around it's center (the root).
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
We can do a BFS, and for each level, check if that
level is a palindrome (including null nodes).
The time complexity is O(N) because the BFS visits
every node once, and the is_not_palindrome function
accesses every element once.
The space complexity is O(W), where W is the 
width of the tree (the level with the most nodes).
This is because the deque stores one level at a time.
'''
def check_if_symmetric(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     bool
    """
    if not root:
        return True
    
    deque1 = deque([root])
    
    while len(deque1) > 0:
        children = []
        for node in deque1:
            children.append(node.left)
            children.append(node.right)
            
        deque1.clear()
                
        # 'children' has all the nodes in the next level
        # check if they form a palindrome
        if not is_palindrome(children):
            return False
            
        # Set up deque for the next level
        deque1.extend([x for x in children if x is not None])
    
    return True
    
def is_palindrome(arr):
    for i in range(len(arr)//2):
        if arr[i] is None:
            if arr[-(i+1)] is not None:
                return False
        else:
            if arr[i].value != arr[-(i+1)].value:
                return False
    return True
