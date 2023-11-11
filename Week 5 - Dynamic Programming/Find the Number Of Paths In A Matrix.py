'''
This problem gives you an N * M matrix filled with 1s or 0s.
1s represent squares you can step on, and 0s represent squares
you can't step on. The problem asks you to find the number of
paths you can take from the top left corner (row 0 column 0)
to the bottom right corner (row N-1, column M-1), assuming
you can only go to the right or down at any square.

The number has to be modulo'd by (10^9 + 7) because the results
can get very large.
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
