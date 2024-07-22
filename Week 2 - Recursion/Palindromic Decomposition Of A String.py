"""
This problem gives you a string (between 1 and 20 characters long) and asks you to find all
the 'palindromic decompositions' of it, which is a way of breaking the string into multiple
substrings, such that each one is a palindrome of at least length 1.

Example:
"abracadabra"

Output
["a|b|r|a|c|ada|b|r|a", "a|b|r|aca|d|a|b|r|a", "a|b|r|a|c|a|d|a|b|r|a"]
"""

def generate_palindromic_decompositions(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    """
    If we consider the space between every pair of two consecutive letters, we can
    either concatenate the two letters, or partition them. If we do both for every
    pair, a binary tree will be formed, and the leaves of this binary tree will
    represent every possible way to split the string into substrings. Out of all of 
    these, most likely, only some will be valid palindromic decompositions and most 
    others won't be.

    Approach 1: We can build this tree completely and keep only the decompositions 
    (leaves of the tree) that are valid.

    Approach 2: We can build this tree, but as we build it, if we get to a point 
    where we've created a non-palindromic partition, we can optimize by skipping 
    that and moving on to partitions that are or may become palindromes. This is 
    a backtracking approach where we 'prune' the branches of the tree that can't 
    lead to a solution. This solution will focus on this approach.
    """
    helper(s, 1, [])
    ans = []
    
    # convert lists of lines into human-readable partitions like 'a|b|r|aca'
    for list in partition_placements:
        if not list:
            ans.append(s)
            continue
        temp = ''
        a = 0
        l = 0
        while a < len(s):
            temp += s[a]
            if list[l]-1 == a:
                temp += '|'
                l += 1
            if l == len(list):
                temp += s[a+1:]
                break
            a += 1
        ans.append(temp)
    
    return ans

# list of lists. each inner list contains indices for the partitions, and represents one palindromic partition
partition_placements = []

# s - the string
# l - the index of the current letter that is being considered
# lines - a list of lines that separate the string 
#         a line at index 1 represents a line between indices 0 and 1
def helper(s, p, lines):
    if p == len(s):  # reached the end of the string
        if partition_is_palindrome(s, lines + [len(s)]):
            partition_placements.append(lines) 
        return
    
    # concatenate current letter
    helper(s, p+1, lines)
    
    # start new partition at current letter
    if partition_is_palindrome(s, lines + [p]): # this 'if' is the pruning part
        helper(s, p+1, lines + [p])
    
# Check only if the last partition is a palindrome
def partition_is_palindrome(s, lines):
    if len(lines) == 1:
        return is_palindrome(s, 0, lines[-1])
    else:
        return is_palindrome(s, lines[-2], lines[-1])

def is_palindrome(s, l, r):
    if l - r == 1:
        return True
    r = r - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True
