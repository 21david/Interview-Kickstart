'''
This problem gives a tree and asks you to find the
height of the tree, which is equivalent to the longest 
path from the root to a leaf node.

The nodes are represented with this class:
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

All trees contain at least one node.
'''

'''
Approach 1: A DFS top-down approach
We can travel all the way to the bottom with
recursive calls, keeping track of the depth 
of each path. Once we reach a leaf node,
we can compare the current depth to a global
variable, which will store the maximum
depth found. Once we traverse all the nodes
in the tree, we just return that variable.
The time complexity and space complexities are
O(N). Each node is visited once. If the tree
is completely unbalanced and is just a linear
chain, the call stack would be of size N, 
which makes it O(N) space complexity.
'''
def find_height(root):
    """
    Args:
     root(TreeNode_int32)
    Returns:
     int32
    """
    max = 0
    
    def helper(root, depth):
        nonlocal max 
        if len(root.children) == 0:  # leaf node
            max = depth if depth > max else max
            return
        
        for child in root.children:
            helper(child, depth + 1)
            
    helper(root, 0)
    
    return max



'''
Approach 2: BFS
Another approach is a BFS approach. We can do a
BFS through the tree using a queue. Every time we
reach a new level, we add 1 to a counter, which
keeps track of levels we've visited. Then, we can
return that counter at the end.
The time and space complexity will be O(N). We
need to visit every node in the tree one time,
and store them in a queue, which could potentially
store most of the nodes at once.
'''
def find_height(root):
    """
    Args:
     root(TreeNode_int32)
    Returns:
     int32
    """
    queue = deque([root])
    count = -1
    
    while len(queue) > 0:
        curr_length = len(queue)
        for i in range(curr_length):
            node = queue.popleft()
            queue.extend(node.children)
        
        count += 1
    
    return count



'''
Approach 3: DFS bottom-up
This approach is similar to the first one, but
it doesn't have any global variables. The max
depth is stored in a variable that gets returned
after every recursive call, incrementing by 1
for every level. The calls on the parent nodes
take the maximum height found within its 
children nodes, and the final answer is returned
by the first call (the root node).
The time and space complexity is O(N). Each node
is visited once. If the tree is completely 
unbalanced and is just a linear chain, the call 
stack would be of size N, which makes it O(N) 
space complexity.
'''
def find_height(root):
    """
    Args:
     root(TreeNode_int32)
    Returns:
     int32
    """
    if root is None:
        return -1
        
    max = -1
    for child in root.children:
        child_height = find_height(child)
        if child_height > max:
            max = child_height
        
    return 1 + max
