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
