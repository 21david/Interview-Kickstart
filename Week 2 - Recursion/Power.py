'''
The question asks to write a function that returns a^b
modulo 1000000007, since the answer may be really big.
'''

'''
This is a recursive solution.
The time and space complexity is O(log b).
'''
def calculate_power(a, b):
    """
    Args:
     a(int64)
     b(int64)
    Returns:
     int32
    """

    return helper(a, b) % 1000000007
    
def helper(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    elif b == 1:
        return a
        
    half_result = calculate_power(a, b // 2)
    
    if b % 2 == 0:
        return half_result * half_result
    else:
        return a * half_result * half_result
