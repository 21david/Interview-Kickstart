'''
The problem asks:
Given an array of unique numbers, return in any order all its permutations.
'''

'''
O(N!) solution
'''
def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    
    answer = []
    helper(arr, [], answer)
    
    return answer
    
def helper(arr, temp, answer):
    if len(arr) == 0:
        answer += [temp]
        return
        
    for i in range(len(arr)):
        helper(arr[:i] + arr[i+1:], temp + [arr[i]], answer)
