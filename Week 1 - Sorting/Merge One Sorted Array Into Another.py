"""
Example input:
{
"first": [1, 3, 5],
"second": [2, 4, 6, 0, 0, 0]
}

Expected output:
[1, 2, 3, 4, 5, 6]
"""

def merge_one_into_another(first, second):
    """
    Args:
     first(list_int32)
     second(list_int32)
    Returns:
     list_int32
    """
    # Since the second half of the second array is filled with 0s, 
    # we can start from the end of that array, adding in
    # the greatest elements from right to left. 
    
    i = len(second) - 1
    f = i // 2
    s = f
    
    while f >= 0 and s >= 0:
        if first[f] > second[s]:
            second[i] = first[f]
            f -= 1
        else:
            second[i] = second[s]
            s -= 1
            
        i -= 1
        
    while f >= 0:
        second[i] = first[f]
        f -= 1
        i -= 1
    
    while s >= 0:
        second[i] = second[s]
        s -= 1
        i -= 1
        
    return second
