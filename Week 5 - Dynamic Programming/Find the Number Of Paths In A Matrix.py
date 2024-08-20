'''
This problem is almost the exact equivalent of
https://leetcode.com/problems/unique-paths-ii/description/

This problem gives you an N * M matrix filled with 1s or 0s.
1s represent squares you can step on, and 0s represent squares
you can't step on. The problem asks you to find the number of
paths you can take from the top left corner (row 0 column 0)
to the bottom right corner (row N-1, column M-1), assuming
you can only go to the right or down at any square.

The number has to be modulo'd by (10^9 + 7) because the results
can get very large.
'''

'''
Solution using a BFS and Dynamic Programming.
It starts at the final position and tries to work its way to the start, or
terminates early if it isn't able to.
It modifies the input directly, but a copy can also be mde to prevent this.
'''
def number_of_paths(matrix):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     int32
    """
    
    n = len(matrix)
    m = len(matrix[0])
    
    if n == 1 and m == 1:
        return matrix[0][0]
    
    # If no ways to get to final position, return 0
    if n == 1 and matrix[0][m-2] == 0:
        return 0
    elif m == 1 and matrix[n-2][0] == 0:
        return 0
    elif matrix[n-1][m-2] == 0 and matrix[n-2][m-1] == 0:
        return 0
    
    def in_bounds(r, c):
        return (0 <= r < n) and (0 <= c < m)
    
    q = deque()
    
    # Start with left and upper neighbors of the final position
    if m > 1:
        q.append((n-1, m-2))
    if n > 1:
        q.append((n-2, m-1))
        
    visited = set()
    
    while q:
        # Current pos
        r, c = q.popleft()
        last_pos = (r, c)
            
        if matrix[r][c] > 0:
            # Calculate value for current pos
            down = matrix[r+1][c] if in_bounds(r+1, c) and matrix[r+1][c] > 0 else 0
            right =  matrix[r][c+1] if in_bounds(r, c+1) and matrix[r][c+1] > 0 else 0
            
            matrix[r][c] = down + right #if (down + right > 0) else 0
        
         # Add left and upper neighbors of pos
        if in_bounds(r, c-1)  and (r,c-1) not in visited:
            visited.add((r, c-1))
            q.append((r, c-1))
        
        if in_bounds(r-1, c) and (r-1, c) not in visited:
            visited.add((r-1, c))
            q.append((r-1, c))
        
    return matrix[0][0] % (10**9 + 7) if last_pos == (0, 0) else 0


'''
Solution using dynamic programming.
It starts at the start and gradually computes all the ways to reach each
square until reaching the end square.
'''
def number_of_paths(matrix):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     int32
    """
    n = len(matrix)
    m = len(matrix[0])
    
    # if start or end block is 0, answer is 0
    if matrix[0][0] == 0 or matrix[-1][-1] == 0:
        return 0
        
    def in_bounds(r, c):
        return 0 <= r < n and 0 <= c < m
        
    for r in range(n):
        for c in range(m):
            if (r, c) == (0, 0) or matrix[r][c] == 0:
                continue
            
            up = matrix[r-1][c] if in_bounds(r-1, c) else 0
            left = matrix[r][c-1] if in_bounds(r, c-1) else 0
            
            matrix[r][c] = up + left
    
    return matrix[-1][-1] % 1000000007


'''
The same solution as above, but it starts at the end square,
and calculates all the ways to get to it until reaching the
start square. Basically the same approach but in reverse order.
'''
mod = int(1e9+7)
def number_of_paths(matrix):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     int32
    """
    R = len(matrix)
    C = len(matrix[0])
    
    if not matrix[-1][-1]:   # could also check matrix[0][0]
        return 0
        
    dp = [[0] * C for _ in range(R)]
    dp[-1][-1] = 1
    
    for r in range(R-1, -1, -1):
        for c in range(C-1, -1, -1):
            if not matrix[r][c]:
                continue
            in_bounds = lambda r1,c1: (0<=r1<R) and (0<=c1<C)
            down = dp[r+1][c] if in_bounds(r+1,c) else 0
            right = dp[r][c+1] if in_bounds(r,c+1) else 0
            dp[r][c] += (down + right) % mod  # there's a math principle that makes this correct
    
    return dp[0][0] 


'''
Recursive solution, starting from the start (0,0), and gradually computing
number of ways to get to each square until reaching the end (N-1, M-1).
'''
mod = int(1e9+7)
def number_of_paths(matrix):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     int32
    """
    R = len(matrix)
    C = len(matrix[0])
    in_bounds = lambda r1,c1: (0<=r1<R) and (0<=c1<C)
    
    def help(r, c):
        if not in_bounds(r,c) or not matrix[r][c]:
            return 0
        
        if r == R-1 and c == C-1:
            return matrix[r][c]
        
        # Figure out ways down and right
        down = help(r+1, c)
        right = help(r, c+1)
        
        return down + right
    
    return help(0,0)


'''
Recursive solution with memoization.
Same approach as above.
'''
mod = int(1e9+7)
def number_of_paths(matrix):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     int32
    """
    R = len(matrix)
    C = len(matrix[0])
    in_bounds = lambda r1,c1: (0<=r1<R) and (0<=c1<C)
    
    def help(r, c, memo={}):
        if not in_bounds(r,c) or not matrix[r][c]:
            return 0
        
        if r == R-1 and c == C-1:
            return matrix[r][c]
            
        if (r,c) in memo:
            return memo[(r,c)]
        
        # Figure out ways down and right
        down = help(r+1, c, memo)
        right = help(r, c+1, memo)
        
        memo[(r,c)] = (down + right) % mod
        return (down + right) % mod  # or return memo[(r,c)]
    
    return help(0,0) 


# Could a space optimized version be written with tabulation? 
