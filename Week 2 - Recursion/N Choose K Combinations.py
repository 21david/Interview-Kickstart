'''
The problem asks:
Given two integers n and k, find all the possible unique combinations of k numbers in range 1 to n.
'''

'''
This solution generates all C(n, k) sets
for n and k.
'''
def find_combinations(n, k):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """
    answer = []
    helper(n, k, 1, [], answer)
    return answer

def helper(n, k, i, temp, answer):
    if k == 0:
        answer += [temp]
        return
    
    for j in range(i, n+1):
        helper(n, k-1, j+1, temp + [j], answer)
