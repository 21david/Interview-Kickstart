'''
This problem is the equivalent of LeetCode 662. Maximum Width of Binary Tree
https://leetcode.com/problems/maximum-width-of-binary-tree
'''

'''
This solution finds out the position of each node from left to right
and stores the first and last node positions for each level in a list. By knowing
these positions for each level, we can subtract the the rightmost position from the 
leftmost one to get the width of each level, and use determine which level has the 
longest width.

The position of each node is calculated like this:
    left children get twice their parent's position
    right children get twice their parent's position plus one

Time complexity: O(N) because we visit every node once.
Auxiliary space complexity: O(H), where H is the height of the tree.
  level_nodes stores 2 elements for every level, and the call stack
  reaches a size equivalent to the height at its peak.
  If the tree is balanced, we can say the SC is O(logN). If it is
  skewed, we can say the SC is O(N).
  For example, if there is only one node per level, O(N):
     1
    /
   2
    \
     3
    /
   5

or only two nodes per level below the root, O(N / 2):
       1
      / \
     6   3
    /   /
   3   4
  /     \
 3       7
'''
def find_maximum_width(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
     # Table for storing leftmost and rightmost node positions for each level
    level_nodes = []

    def dfs(node, depth, position):
        # Add 1st position for this level if not yet visited
        if depth >= len(level_nodes):
            level_nodes.append([position])
        # Add 2nd position if its the 2nd one visited in this level
        elif len(level_nodes[depth]) == 1:
            level_nodes[depth].append(position)
        # If its the 3rd+ node visited, update rightmost position
        elif len(level_nodes[depth]) == 2:
            level_nodes[depth][1] = position
        
        # Visit non-null children with calculated positions
        if node.left:        
            dfs(node.left, depth + 1, 2 * position)
            
        if node.right:
            dfs(node.right, depth + 1, 2 * position + 1)
        
    # Start dfs. Root is at level 0 and has position 0
    dfs(root, 0, 0)
    
    # Calculate all widths and return the longest one
    return max( (level_arr[-1] - level_arr[0] + 1) for level_arr in level_nodes )
