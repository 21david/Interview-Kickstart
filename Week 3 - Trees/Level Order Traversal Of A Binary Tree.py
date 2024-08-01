"""
This problem gives you a binary tree and asks you to create an array of arrays, where each inner array
stores all the nodes of the level at its index.

Example

     2
   /    \
  5      4
 / \    / \
0   1  3   6

Output:
[
  [2],
  [5, 4],
  [0, 1, 3, 6]
]

"""
"""
Solution 1:
A BFS approach using a queue.
"""
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def level_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    '''
    BFS approach. Traverse the tree in a BFS style, attaching the level to the node in the
    queue, so that every node knows which level it's on. This is done by taking the parent node's
    level and adding 1 to it every time a new node goes in the queue. As each node gets processed
    by the BFS, it's value will be placed into an array of arrays, where an array at index i 
    represents the nodes in level i. This will build up the desired output. 
    
    Time complexity: O(N). We have to iterate through the entire tree, processing each node once (O(1)).
    
    Space complexity:
        Input space complexity: O(N) to store the binary tree.
        
        Auxiliary space complexity: O(N). The queue may store up to half of all the nodes in the
        tree at once. This would happen in a full binary tree as it reaches the last level.
        
        Output space complexity: O(N) This is because we are storing all N values across inner arrays. 
        If the height of the tree is H, we make H inner arrays. H will be equal to N in the worst case, 
        and lesser in all other cases, so the real complexity of O(2N) would reduce to O(N).
    '''
    ans = []  # Array to store the final answer
    q = deque([(root, 0)]) # Add root node and its level
    
    # BFS - continue until we've processed all nodes
    while q:
        # Get the next node in the queue and it's level
        node, level = q.popleft()
        
        # If no array exists for this level yet, create it
        if level > (len(ans) - 1):
            ans.append([])
            
        # Add the node's value to the array for that level
        ans[level].append(node.value)
        
        # Add children to queue with their corresponding level
        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))
        
    return ans



"""
Solution 2
This is basically the same approach as above, but it uses a single
array that stores the nodes of a level, instead of a queue that
stores the nodes with their levels. It has the same time and space
complexities.
"""
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def level_order_traversal_2(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    '''
    This is a BFS approach. It stores each level in an array, then repeatedly
    uses that array to get the values for every node and then update itself to
    represent the next level. The final answer is built as each level is processed.
    
    Time complexity: O(N) because each nodes is processed exactly once.
    
    Space complexity:
        Input space complexity: O(N) for the binary tree
        
        Auxiliary space complexity: O(N) for the array that stores the level.
        This array will store references to at most half of the nodes
        in the tree  at one time (which would happen if it reaches the last 
        level of a full binary tree).
        
        Output space complexity: O(N) for the array of array of values.
    '''
    
    curr_level = [root]  # stores each level as we progress through the tree
    ans = [[root.value]] # store the final values
    
    # Loop until we've reached a level that is completely empty
    # (AKA until we've passed the last level in the tree)
    while curr_level:
        new_level = []
        new_level_values = []
        
        # Proces each node in the current level/array and create a new array with the children
        for node in curr_level:
            if node.left:
                new_level.append(node.left)
                new_level_values.append(node.left.value)
            if node.right:
                new_level.append(node.right)
                new_level_values.append(node.right.value)
                
        # Update the array to represent the next level, and build the answer array
        curr_level = new_level
        if new_level_values:
            ans.append(new_level_values)
    
    return ans
