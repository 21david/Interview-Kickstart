'''
O(N) solution with a bottom-up approach.
'''
def find_fibonacci(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    if n <= 1:
        return n

    a, b = 1, 1
    
    for _ in range(n-2):
        a, b = b, a + b
        
    return b



'''
O(N) solutioni involving memoization.
'''
def find_fibonacci(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    return helper(n, [None] * (n+1))
    
def helper(n, arr):
    if n == 0 or n == 1:
        arr[n] = n
        return n
    
    if arr[n-1] == None:
        helper(n-1, arr)
    
    if arr[n-2] == None:
        helper(n-2, arr)
        
    arr[n] = arr[n-1] + arr[n-2]
    
    return arr[n]



'''
O(N) solution involving a generic additive sequence function.
'''
def find_fibonacci(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    return add_seq(n, 0, 1)

def add_seq(n, b1, b2):
    if n == 0:
        return b1
    else:
        return add_seq(n-1, b2, b1+b2)



'''
O(2^N) solution with recursion.
The actual tightest upper bound on this is O(ϕ^n), where ϕ is the golden ratio (≈ 1.618),
because the binary tree formed by the recursion calls is not complete.
'''
def find_fibonacci(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    if n == 0 or n == 1:
        return n
    return find_fibonacci(n - 1) + find_fibonacci(n - 2)
