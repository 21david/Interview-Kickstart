"""
This problem gives you an integer N and asks you to create all possible strings
that have N open parenthesis '(' and N closing parenthesis ')' that are correctly placed.

Example:
"n": 3

Output:
[
"((()))",
"(()())",
"(())()",
"()(())",
"()()()"
]

Based off of LeetCode problem 22: Generate Parentheses.
"""

def find_all_well_formed_brackets(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """
    '''
    Couple of things:
    1. Answers will always start with '('
    2. Can never add a ')' if t there are already as many '('s as ')'s
    3. We need to add exactly n '('s and n ')'s
    '''
    ans = []
    
    def helper(s, l, r):
        if len(s) == n * 2:
            ans.append(''.join(s))
            return
            
        # Add left if possible
        if l < n: # if we still have remaining '('s
            s.append('(')
            helper(s, l + 1, r)
            s.pop()
        
        # Add right if possible
        if r < n and l > r: # if we still have remaining ')'s and they won't unbalance the brackets
            s.append(')')
            helper(s, l, r + 1)
            s.pop()

    helper(['('], 1, 0)
    
    return ans
    
