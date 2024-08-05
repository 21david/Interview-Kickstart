'''
This problem gives you a binary tree, and asks for a count of how many trees within the whole tree
are "uni-value" trees, which are trees where every node has the same value.

For example:
      2
    /   \
  2       2
 / \     / \
2   2   3   2

The answer for this tree is 5.
All leaf nodes count as uni-value trees because technically, they consist of only
one value. So our total up to this point is 4. The only other tree that is uni-value
is    2    because all nodes have the same value. That makes it 5 uni-value subtrees.
     / \
    2   2
The tree starting at the root node is not uni-value because of the 3, and neither is
the subtree on the right, for the same reason.

Another way to think of the question is: How many subtrees (including single-value trees)
can you draw a circle around (parent + any children it has) that consist of only one value?

Equivalent to LeetCode problem:
250. Count Univalue Subtrees (premium)
https://leetcode.com/problems/count-univalue-subtrees
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
Solution 1: DFS traversal with a global count variable.

A leaf node is always a uni-val tree.
An internal node is a uni-val tree if:
    1) its children (whether there's 1 or 2) are uni-val trees and
    2) it and all of its children have the same value
    
We could do a DFS traversal, and from the bottom to the top,
figure out which trees are unival using the logic above. We would
create a global variable to keep track of how many we find, and return
that at the end.

TC would be O(N) because every node would have to be visited once,
for all types of input.

SC would be:
      Best case: O(logN) in the case where the tree is a complete binary tree, 
      because the call stack would reach the height of the tree (logN) at the most,
      and each call in the stack would use O(1) space.
      
      Worst case: O(N) in the case where the tree has only one node per level, 
      because the call stack would reach the number of nodes at the most in this
      case.

I think this could also be written with booleans. Instead of returning
a value for each call, we could return True if the tree was a uni-value
tree or False otherwise. If a subtree is a uni-value tree, then we can
just access its value and use it to compare with the current node's and 
the other child's value. This is a slight optimization. The next solution
implements it this way.
'''
def find_single_value_trees(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    if not root:
        return 0
    
    count = 0
    
    def dfs(node):
        nonlocal count
        
        # Leaf node case
        if not (node.left or node.right):
            count += 1
            return node.value
            
        # These variables will receive the uni-value IF they are uni-value subtrees
        # Otherwise, they will receive None from the dfs call.
        left = dfs(node.left) if node.left else None
        right = dfs(node.right) if node.right else None
        
        # If this node is the root of a uni-val tree, add 1 to count
        if node.left and node.right:  # case where it has two children
            if left == right == node.value:
                count += 1
                return node.value
        # Case where it only has one child
        elif (node.left and left == node.value) or (node.right and right == node.value):
            count += 1
            return node.value
        
    dfs(root)

    return count



'''
Solution 2: DFS
This solution is very similar to the one above, but written different. It doesn't use a
global variable, it bubbles up the number of trees found as its doing the traversal and 
computes the total uni-value trees at each node.

The return type of the inner DFS function contains two values:
1 - A boolean representing if the subtree is a uni-value tree or not
2 - the total amount of uni-value subtrees within the given tree

The counts increment as they go from the leaf nodes up to the root node in the DFS traversal, 
and the root node computes and returns the total uni-value subtrees found.

TC is O(N) because every node has to be visited once, in every type of input.

SC is O(N) because we must keep track of the total uni-value subtrees found
for every node, and a boolean. This would also happen in every type of input.
'''
def find_single_value_trees(root):
    if not root:
        return 0
    
    def dfs(node):
        # DFS traversal
        left_is_unival, left_count = dfs(node.left) if node.left else (False, 0)
        right_is_unival, right_count = dfs(node.right) if node.right else (False, 0)
        
        # If it has both children
        if node.left and node.right:
            # If it is a uni-value tree, return True and the total count plus 1
            if (left_is_unival and right_is_unival) and (node.value == node.left.value == node.right.value):
                return True, left_count + right_count + 1
            # Else, return False and the total count
            # This will cause all trees above to also not count as uni-value trees
            else:
                return False, left_count + right_count
        # Same logic as above but for nodes with 1 child
        elif node.left:
            if left_is_unival and (node.value == node.left.value):
                return True, left_count + 1
            else:
                return False, left_count
        elif node.right:
            if right_is_unival and (node.value == node.right.value):
                return True, right_count + 1
            else:
                return False, right_count
        # Leaf nodes are uni-value trees, so return True and 1 for the count
        else:
            return True, 1
    
    # Return only the total count
    return dfs(root)[1]
