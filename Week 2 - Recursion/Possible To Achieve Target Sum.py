"""
This problem gives you a list of integers and a target integer. It asks whether any 
subset of the list sums to the target integer. It expects True if there is, or False
if there isn't.

"arr": [2, 4, 8],
"k": 6

Output:
True
"""

def check_if_sum_possible(arr, k):
    """
    Args:
     arr(list_int64)
     k(int64)
    Returns:
     bool
    """
    # Used an array to be able to access and change its value from recursive calls
    found = [False]  # stores whether an answer has been found, used to stop further recursive calls
    
    def subset_sums(arr, total, i):
        if found[0] or (i == len(arr)):
            return
        
        # don't include current element in the total
        subset_sums(arr, total, i+1)
        
        # include current element in the total
        if total + arr[i] == k:
            found[0] = True 
            return
        subset_sums(arr, total + arr[i], i + 1)
        
    subset_sums(arr, 0, 0)
    
    return found[0]
