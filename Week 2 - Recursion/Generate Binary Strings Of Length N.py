'''
The problem asks:
Given a number n, generate all possible binary strings of length n.
For example, for n = 3, the answer would be (in any order):
["000", "001", "010", "011", "100", "101", "110", "111"]
'''

'''
Iterative solution 1.
This generates a big array of binary numbers (each from length
1 to n) and filters out the ones that aren't length N at the end.
'''
def get_binary_strings(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """
    answer = ['0','1']
    
    for _ in range(n-1):
        for i in range(len(answer)):
            cur_binary = answer[i]
            answer += [cur_binary + '0']
            answer += [cur_binary + '1']
            
    return [x for x in answer if len(x) == n]



'''
Improved iterative solution. This solution takes
advantage of the fact that the 2^N strings we want
are all at the end, so it just takes those.
'''
def get_binary_strings(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """
    temp = ['0','1']
    answer = []
    
    for _ in range(n-1):
        for i in range(len(temp)):
            cur_binary = temp[i]
            temp += [cur_binary + '0']
            temp += [cur_binary + '1']
            
    answer = temp[-(2**n) : ]
            
    return answer



'''
Improved again iterative solution. This solution creates
an empty array during each new value of n, adds the new
strings to that array, and discards the old one. At the 
end, we have only the binary strings of length N in the
final array.
'''
def get_binary_strings(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """
    temp = ['0','1']
    answer = temp
    
    for _ in range(n-1):
        answer = []
        for i in range(len(temp)):
            cur_binary = temp[i]
            answer += [cur_binary + '0']
            answer += [cur_binary + '1']
        temp = answer
            
    return answer



'''
Recursive BFS solution. This solution takes
an array of binary strings, and for each one,
it creates two new binary strings, one with
a 0 at the end and another one with a 1 at the
end. It works in a BFS fashion, creating all
binary strings of length i (from 1 to N)
one at a time. At the end, it creates the
final answer in one pass.
'''
def get_binary_strings(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """
    if n == 1:
        return ['0', '1']
    
    sub_sol = get_binary_strings(n-1)
    answer = []
    for item in sub_sol:
        answer += [item + '0']
        answer += [item + '1']
        
    return answer



'''
Recursive DFS solution. This one travels
down the recursion tree in a DFS fashion, 
first creating the first binary string of
length N (all 0s) and gradually making each
next binary string. At the end, all the
strings will be in 'answer'.

A similar solution would be to pass
answer into the array instead of having
a nonlocal variable.
'''
def get_binary_strings(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """
    
    def helper(n, temp):
        
        # Give this function access to answer
        nonlocal answer
        
        if n == 0:
            answer += [temp]
            return
        
        # This adds them in sorted order
        helper(n-1, temp + '0')
        helper(n-1, temp + '1')
        
        # To add them in reverse sorted order:
        # helper(n-1, temp + '1')
        # helper(n-1, temp + '0')
        
    answer = []
    helper(n, '')
    return answer
