'''
This problem gives you a binary tree and asks you to find the lowest common ancestor (LCA)
of two nodes in the tree. The LCA of two nodes is the lowest node in the tree that is an
ancestor of both, and a node can be an ancestor of itself.

For example:

       1
     /    \
    /      \
   2        3
 /   \     /  \
4     5   6    8
     / \
    8   9

LCA(8, 9) = 5
The lowest common ancestor of nodes 8 and 9 is 5

LCA(2, 5) = 2
LCA(2, 3) = 1
LCA(2, 8) = 1
LCA(8, 8) = 8
LCA(1, 1) = 1
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
This is a bottom-up approach that traverses the whole tree one time, and for each node
(and for each recursive call), it creates a left and a right variable, which stores
either one of the input nodes, if found, the LCA, if found, or None otherwise.
The logic is that if both of these variables have a node in them, then that means that 
either p or q (one of the input nodes) was found in the left subtree, and the other 
one was found in the right subtree, so the current node is the LCA and that gets returned 
up the recursive call chain. Or, if the current node is one of the nodes, and either of these
variables has the other node, then the current node is also the LCA (because a node can be
an ancestor/descendant of itself). In this case, the current node also gets returned up the
recursive call chain. In the end, the LCA bubbles up to the original call and is returned
as the final answer.
Time complexity is O(N) because it visits each node at most once and does a constant amount
of work for each one. The space complexity is O(N) because the call stack might reach a 
height of N if the tree is completely skewed, and it creates a constant amount of space 
for each call.
'''
def lca(root, a, b):
    """
    Args:
     root(BinaryTreeNode_int32)
     a(BinaryTreeNode_int32)
     b(BinaryTreeNode_int32)
    Returns:
     int32
    """
    return helper(root, a, b).value

  
def helper(root, p, q):
    if not root:
        return None

    # This becomes true if the current node is one of the two input nodes
    found_node = root.value == p.value or root.value == q.value

    if found_node:
        return root
    
    left = helper(root.left, p, q)
    
    if left and left.value != p.value and left.value != q.value:
        # We found the LCA, no need to continue DFS
        return left
    
    right = helper(root.right, p, q)

    if (left and right) or (found_node and (left or right)):
        # The LCA is found
        return root
    elif left or right:
        return left or right



'''
This approach uses a nested DFS function and a global variable that
holds the LCA node when it is found. When it is found, it stops
serching and returns the answer.

We can do one pass through the whole tree, keeping track of 3 things:
1. Is the current node either p or q
2. How many nodes (p and/or q) we found on the left subtree
3. How many nodes we found on the right subtree

If the current node is either p or q, then there are 2 possible cases:
1. If the other node is somewhere on the left or right subtrees, then
   the current node is the LCA
2. If the other node isn't somwhere on the left or right subtree, then
   the current node is not the LCA

If the current node is not either p or q, then there are 2 cases:
1. One node is on the left subtree and the other one is in the right subtree.
   If this is the case, then the current node is the LCA.
2. Both nodes are either on the left subtree or on the right subtree. If so,
   we continue the traversal on both sides. 

After doing one pass, we should have found the answer. An optimization is,
as soon as we find the LCA, we can stop the traversal from continuing.

Also, if a and b are the same, then they are their own LCA, so we can return 
without doing any searching.

Time time complexity of this is O(N) because we visit each node once.
The space complexity is O(N) because if the tree is a linear chain of nodes,
the recursion stack call may reach a height of N.
'''
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def lca(root, a, b):
    """
    Args:
     root(BinaryTreeNode_int32)
     a(BinaryTreeNode_int32)
     b(BinaryTreeNode_int32)
    Returns:
     int32
    """
    
    if a.value == b.value:
        return a.value
    
    lca = [None]
    
    def dfs(node):
        if lca[0] or not node:
            return 0
    
        left = dfs(node.left)
        right = dfs(node.right)
    
        found = node.value == a.value or node.value == b.value
        if found:
            if left == 1 or right == 1:
                # current node is LCA
                lca[0] = node
                return 0
            else:
                return left | right | found
                
        else:
            if left == 1 and right == 1:
                lca[0] = node
                return 0
            else:  
                return left | right
    
    dfs(root)
    return lca[0].value



'''
This solution are based off of this logic:
A node is the LCA if:
    - It is one of the input nodes, and the other input node is in one of its subtrees
    - It is not one of the input nodes, one input node is in its left subtree, and
    the other input node is in its right subtree
    - Both input nodes are the same

We can do a recursive DFS, which, for every node, finds out how many of the input nodes
are on the left, how many are on the right, and also considers if it is an input node.
When we can verify one of the conditions above happened, we've found the LCA and we can
cancel or prevent all other recursive calls.

This solution is similar to the DFS one above, but slightly more optimal because it prevents 
unnecessary calls earlier.

Time complexity: O(N) because it will only process each node at most once.
(Best case scenario is O(1)).

Auxilliary space complexity: O(N) because we create 3 variables for every node we visit.
(Best case scenario is O(1)).
'''
def lca(root, a, b):
    """
    Args:
     root(BinaryTreeNode_int32)
     a(BinaryTreeNode_int32)
     b(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Edge case where both nodes are the same
    if a == b:
        return a.value
        
    # Keep track of how many nodes are yet to be found
    nodes_left = 2
    lca = None
        
    def dfs(node):
        nonlocal nodes_left, lca
        
        is_input_node = node == a or node == b
        if is_input_node:
            nodes_left -= 1
            
        if nodes_left == 0:
            # Prevent further tree traversal if the answer is found
            return is_input_node
        
        left = dfs(node.left) if node.left else 0
        
        if is_input_node and left:
            # Current node is LCA
            lca = node
            return 2
        
        if nodes_left == 0:
            return left + is_input_node
        
        right = dfs(node.right) if node.right else 0
        
        if is_input_node and right:
            # Current node is LCA
            lca = node
            return 2
        
        if left and right:
            # Current node is LCA
            lca = node
            return 2
 
        return left + right + is_input_node
        
    dfs(root)
        
    return lca.value



'''
This approach is correct, but has a much worse time complexity
of O(N^2), because in the worst case, it starts a DFS at almost every 
node in the tree.

If we start from the root and search the left subtree, then 3 things
can happen:
1. we find only one node (p or q)
2. we find both nodes
3. we find neither node

In case 1, then the root node is the LCA, because the other node
is in the right subtree.
In case 2, there is a lower LCA, so we should start searching
again from the left child.
Case 3 is basically the mirrored version of case 2. There is a lower LCA
somewhere on the right subtree, so we can start searching from the
right child.

The search will check the current node itself, since nodes can be 
descendants/ancestors of themselves.

Our algorithm could start a DFS at the root node, which will be a function 
that searches for both nodes, and returns how many it found.
Based off of that, it will return or repeat the search on the left
or right child until it finds it.
'''
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def lca(root, a, b):
    """
    Args:
     root(BinaryTreeNode_int32)
     a(BinaryTreeNode_int32)
     b(BinaryTreeNode_int32)
    Returns:
     int32
    """
    if a.value == b.value:
        return a.value

    # Count how many input nodes were found in a DFS. Either 0, 1, or 2.
    count = [0]

    def dfs(node):
        if not node or count[0] == 2:
            return
        
        if node.value == a.value or node.value == b.value:
            count[0] += 1
            
        dfs(node.left)
        dfs(node.right)
    

    while root:
        if root.value == a.value or root.value == b.value:
            return root.value

        count[0] = 0
        
        dfs(root.left)

        if count[0] == 1:
            return root.value
        elif count[0] == 0:
            root = root.right
        else:  # result == 2
            root = root.left
            
