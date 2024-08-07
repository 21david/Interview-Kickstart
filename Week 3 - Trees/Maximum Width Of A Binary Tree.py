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
'''
def find_maximum_width(root):
    level_nodes = []
    
    def dfs(node, depth, position):
        if depth >= len(level_nodes):
            level_nodes.append([position])
        elif len(level_nodes[depth]) == 1:
            level_nodes[depth].append(position)
        elif len(level_nodes[depth]) == 2:
            level_nodes[depth][1] = position
            
        if node.left:        
            dfs(node.left, depth + 1, 2 * position)
            
        if node.right:
            dfs(node.right, depth + 1, 2 * position + 1)
            
    dfs(root, 0, 0)
    
    return max(level_arr[-1] - level_arr[0] + 1 for level_arr in level_nodes)
