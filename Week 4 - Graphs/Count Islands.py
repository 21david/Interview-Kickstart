'''
Very similar to LeetCode 200. Number of Islands
https://leetcode.com/problems/number-of-islands
'''

def count_islands(matrix):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     int32
    """
    def flood_fill(r, c):
        def in_bounds():
            return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])
            
        if not in_bounds() or not matrix[r][c]:
            return
        
        matrix[r][c] -= 1
            
        up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)
        up_left, up_right, down_left, down_right = (-1,-1), (-1,1), (1,-1), (1,1)
        
        for dr, dc in (up, down, left, right, up_left, up_right, down_left, down_right):
            flood_fill(r + dr, c + dc)
    
    count = 0
    
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c]:
                count += 1
                flood_fill(r, c)
    
    return count
