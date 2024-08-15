'''
Mostly equivalent to https://leetcode.com/problems/maximal-square
'''

from itertools import product
def largest_sub_square_matrix(n, m, mat):
    """
    Args:
     n(int32)
     m(int32)
     mat(list_list_int32)
    Returns:
     int32
    """
    
    dp = [[0] * m for _ in range(n)]
    max_len = 0
    
    for r, c in product(range(n), range(m)):
       if mat[r][c]:
            try:
                sq1 = dp[r-1][c]
                sq2 = dp[r-1][c-1]
                sq3 = dp[r][c-1]
            except IndexError:
                sq1 = 0
            
            dp[r][c] = min(sq1, sq2, sq3) + 1
            max_len = max(max_len, dp[r][c])
            
    return max_len
