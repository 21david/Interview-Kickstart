'''
Equivalent to LeetCode 1022. Sum of Root To Leaf Binary Numbers
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers
'''

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def sum_root_to_leaf_numbers(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    total = 0
    
    def dfs(node, num_slate):
        nonlocal total
        
        if not (node.left or node.right):
            num_slate.append(str(node.value))
            total += int(''.join(num_slate), 2)
            num_slate.pop()
            return
            
        num_slate.append(str(node.value))
        if node.left:
            dfs(node.left, num_slate)
        if node.right:
            dfs(node.right, num_slate)
        num_slate.pop()
        
    dfs(root, [])
    return total


'''
More space efficient solution
using bitwise operators and math.
Same approach as above.
'''
def sum_root_to_leaf_numbers(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    total = 0
    
    def dfs(node, num):
        nonlocal total
        if not (node.left or node.right):
            num <<= 1
            num += node.value
            total += num
            num >>= 1
            return
            
        num <<= 1
        num += node.value
        if node.left:
            dfs(node.left, num)
        if node.right:
            dfs(node.right, num)
        num >>= 1
        
    dfs(root, 0)
    return total
