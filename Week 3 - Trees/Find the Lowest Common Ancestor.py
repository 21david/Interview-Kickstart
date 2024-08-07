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
This solution is based off of this logic:
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

Time complexity:
	Best case: O(1). If both input nodes are the same, OR the first two searched nodes
	are the input nodes, it will stop processing the tree and return the answer.
	
	Worst case: O(N). Each node will be visited at most once. Once a node is found during
	the DFS, the 1 that represents it will travel upwards with the left and right variables,
	and the node will never be visited again.
	In the worst case, if both nodes are on the lowest possible levels and as far right in 
	the tree as possible, every node will be visited one time.
        
Space complexity:
	Input space complexity:
		Every case: O(N) for all the nodes and the two input nodes
	
	Auxiliary space complexity: 
		Best case: O(1), same as time complexity reason. It will only store info for 1-2 nodes.
	
		Worst case: O(N). In the worst case, there will be a left and a right
		variable initialized for each node, and the stack may reach a height equal to N if the
		tree has only one node per level.
	
	Output space complexity: 
		Every case: O(1) for the value of the LCA node.
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


'''
BFS solution 
Modify the tree such that nodes have a reference to their parent and their current 
level. Traverse the tree, modifying each node with this info, and then stop doing
that when both nodes are found (for optimization). Would also work with DFS.

Then, we can start from each input node, and work our way up to find the LCA.
Here are two ways to do this:
1) Create a list that includes the path from each node up to the root. Each
element be a tuple containing a node value and it's level. This will create
two lists with at least one element in common. To find the LCA, assuming we created
the lists in a sorted way, we could set a pointer to the root node element, and
repeatedly check for lower common ancestors until finding the lowest one.

2) Whichever pointer is lower in the tree (has a higher level), move it up until both
pointers are on the same level. Check if they are on the same node. If not, then move
them both up by 1 and repeat. When they both end up on the same node, that is
their LCA node. This approach is more memory efficient than 1) above. 
The solution below implements this approach.

A tradeoff with this approach is that the original tree is modified. See the next solution
for a version of this that doesn't modify the original tree.

Time complexity:
	Best case: O(1). If both nodes are the root node, or one is the root and the other is
 	a direct child, it will always only do work for those nodes.

  	Worst case: O(N). It may visit every node in the tree during the BFS, and then one
	of the nodes may have to climb through almost every node to get to the other node,
 	if the tree is a linear chain of nodes.

Auxilliary space complexity:
	Best case: O(1). Same reason as time complexity.

 	Worst case: O(N). We may store information on every node (reference to parent and level).
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
    nodes_found = 0
    
    root.level = 0
    if root == a or root == b:
        nodes_found += 1
    
    # BFS
    q = deque([root])
    while q:
        node = q.popleft()
        
        if node.left:
            node.left.parent = node
            node.left.level = node.level + 1
            
            # Check for input nodes. If we found both, we
            # can prevent unnecessary future work
            if node.left == a or node.left == b:
                nodes_found += 1
                if nodes_found == 2:
                    break
                
            q.append(node.left)
            
        if node.right:
            node.right.parent = node
            node.right.level = node.level + 1
            
            # Check for input nodes again
            if node.right == a or node.right == b:
                nodes_found += 1
                if nodes_found == 2:
                    break
                
            q.append(node.right)
            
    # We have modified both nodes and all their ancestors
    # Now we can go upwards to find the LCA
    # Steps: Move the lower pointer to the same level as the other pointer
    # then repeatedly check if they have met at their ancestor or move them up
    while a != b:
        if b.level > a.level:
            b = b.parent
        elif a.level > b.level:
            a = a.parent
        else:
            a = a.parent
            b = b.parent
    
    # Return the first node that they meet at
    return a.value



'''
This is the same approach as above, but we store the parent references and levels for each node
in a dictionary instead of on the actual nodes.

Time complexity:
	Best case: O(1). If both nodes are the root node, or one is the root and the other is
 	a direct child, it will always only do work for those nodes.

  	Worst case: O(N). It may visit every node in the tree during the BFS, and then one
	of the nodes may have to climb through almost every node to get to the other node,
 	if the tree is a linear chain of nodes.

Auxilliary space complexity:
	Best case: O(1). Same reason as time complexity.

 	Worst case: O(N). We may store information on every node (reference to parent and level)
  	in the dictionary.
'''
from collections import namedtuple
def lca(root, a, b):
    """
    Args:
     root(BinaryTreeNode_int32)
     a(BinaryTreeNode_int32)
     b(BinaryTreeNode_int32)
    Returns:
     int32
    """
    nodes_found = 0
    
    # Each key in the dictionary represents a node. Its value is a tuple that contains
    # a reference to its parent and its level. Named tuples make this easier to work with.
    Node_info = namedtuple('node_info', ['parent', 'level'])
    root_info = Node_info(None, 0)
    nodes_info = {root: root_info}
    
    if root == a or root == b:
        nodes_found += 1
    
    # BFS
    # We will store the level along with each node. We could also only store the nodes
    # and access their level using nodes_info, but that access has a worst case TC of O(N).
    q = deque([(root, 0)])
    
    while q:
        node, lvl = q.popleft()
        
        if node.left:
            nodes_info[node.left] = Node_info(node, lvl+1)
            
            # Check for input nodes. If we found both, we
            # can prevent unnecessary future work
            if node.left == a or node.left == b:
                nodes_found += 1
                if nodes_found == 2:
                    break
                
            q.append((node.left, lvl+1))
            
        if node.right:
            nodes_info[node.right] = Node_info(node, lvl+1)
            
            # Check for input nodes again
            if node.right == a or node.right == b:
                nodes_found += 1
                if nodes_found == 2:
                    break
                
            q.append((node.right, lvl+1))
            
    # We have modified both nodes and all their ancestors
    # Now we can go upwards to find the LCA
    # Steps: Move the lower pointer to the same level as the other pointer
    # then repeatedly check if they have met at their ancestor or move them up
    while a != b:
        a_info = nodes_info[a]
        b_info = nodes_info[b]
        if a_info.level > b_info.level:
            a = a_info.parent 
        elif b_info.level > a_info.level:
            b = b_info.parent
        else:
            a = a_info.parent
            b = b_info.parent
    
    # Return the value of the first node that they meet at
    return a.value
