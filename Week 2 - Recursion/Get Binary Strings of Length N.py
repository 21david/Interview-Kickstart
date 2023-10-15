'''
The problem states that, given a number N, generate all
possible binary strings of length N. For example, for N = 3,
the answer would be:
["000", "001", "010", "011", "100", "101", "110", "111"]

These solutions are similar to the solutions in
https://github.com/21david/Interview-Kickstart/blob/main/Week%202%20-%20Recursion/Generate%20All%20Subsets.py
If we want a binary number of length N, then for each 
number from 1 to N, we create a string with a 0 appended
and one with a 1 appended. The last set of strings
we make is all 2^N binary strings.
'''

'''
O(2^N) recursive solution.
'''
def get_binary_strings(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """
    answer = []
    helper(n, '', answer)
    return answer
    
    
def helper(n, temp, answer):
    if n == 0:
        answer += [temp]
        return
    
    helper(n-1, temp + '0', answer)
    helper(n-1, temp + '1', answer)



'''
Iterative solution. 
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
        for i in range(len(temp) - 1):
            cur_binary = temp[i]
            temp += [cur_binary + '0']
            temp += [cur_binary + '1']
            
    answer = temp[-(2**n) : ]
            
    return answer
