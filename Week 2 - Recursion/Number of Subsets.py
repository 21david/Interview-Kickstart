'''
O(1) solution
'''

def count_all_subsets(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    return 2 ** n

'''
O(log N) solution
'''
def count_all_subsets(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    
    if n == 0:
        return 1
    
    temp = count_all_subsets(n // 2)
    
    if n % 2 == 1:
        return 2 * temp * temp
    else:
        return temp * temp


'''
O(N) solution
'''
def count_all_subsets(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    if n == 0:
        return 1
    
    return 2 * count_all_subsets(n-1)

'''
O(2^N) solution
'''
def count_all_subsets(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    if n == 0:
        return 1
    
    return count_all_subsets(n-1) + count_all_subsets(n-1)
