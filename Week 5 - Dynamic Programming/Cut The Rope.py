'''
This problem gives you an integer N, which represents a rope length, which has to be "cut"
at least once. It asks you to find the highest product possible of its cut lengths.
For exampe, if N is 4, then the highest product of its cut lenghts is 2 * 2 = 4, because
the rope is cut into two pieces of length 2.
'''

def max_product_from_cut_pieces(N):
    """
    Args:
     n(int32)
    Returns:
     int64
    """
    '''
    We can make an array that will store the solution to f(n) for all n
    which will let us work our way to n, starting from 1. This is a form
    of bottom-up dynamic programming.

    f(length) = max( cut * (length - cut) , cut * f(length - cut) )
    where cut is checked for the range [1, length-1]

    'cut * (length - cut)' represents just the two lengths, which may be the
    maximum in some cases.

    'cut * f(length - cut)' represents the current cut plus at least one more
    cut. The memo array helps us prevent repeated recursive calls by storing
    the answer the first time we calculate it.

    The time complexity is O(N^2) because the outer loop runs from 3 to N + 1, 
    and the inner loop runs from 2 to the current value of the outer loop.
    The space complexity is O(N) because of the memo array, which creates an
    array of length N + 1.
    '''
    
    memo = [0] * (N+1)
    memo[1] = 1
    memo[2] = 1
    
    for n in range(3, N+1):
        # try all different cut lengths starting from 2
        max_prod = 0
        for cut in range(2, n):
            rest = n - cut
            max_prod = max(max_prod, cut * rest, cut * memo[rest])
            
        memo[n] = max_prod
            
    return memo[N]
