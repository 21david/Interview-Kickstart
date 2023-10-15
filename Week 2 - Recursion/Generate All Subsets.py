'''

'''
def generate_all_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    '''
    We can start with an empty string and store it in
    an array. Then, we iterate through each letter, 
    and we add it to each string in the array (creating
    copies, not editing the originals) (not including 
    each string that gets added during a pass). This 
    will generate every subset because for each letter, we 
    generate every subset that includes it, and every 
    subset that excludes it.
    The time complexity os O(2^N).
    '''
    arr = ['']
    
    for char in s:
        for i in range(len(arr)):
            cur_string = arr[i]
            arr += [cur_string + char]
    
    return arr




'''
O(2^N) recursive solution.
This does a similar thing to the previous approach,
but it uses recursion. In the first recursive call,
it excludes the current letter. In the second one,
it includes the current letter. It chips away from
s (the string) one at a time, and it reaches the
base case when s becomes empty.
'''
def generate_all_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    arr = []
    
    helper(s, '', arr)
    
    return arr

def helper(s, temp, arr):
    if s == '':
        arr += [temp]
        return 
    
    helper(s[1:], temp, arr)
    helper(s[1:], temp + s[0], arr)
