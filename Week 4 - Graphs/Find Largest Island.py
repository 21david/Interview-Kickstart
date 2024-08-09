'''
Equivalent to 695. Max Area of Island
https://leetcode.com/problems/max-area-of-island
'''

def max_island_size(grid):
    """
    Args:
     grid(list_list_int32)
    Returns:
     int32
    """
    
    def flood_fill(r, c):
        nonlocal size
        def in_bounds():
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
            
        if not in_bounds() or not grid[r][c]:
            return
        
        size += 1
        grid[r][c] -= 1
            
        up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)
        
        for dr, dc in (up, down, left, right):
            flood_fill(r + dr, c + dc)
    
    size = 0
    max_size = 0
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c]:
                size = 0
                flood_fill(r, c)
                max_size = max(max_size, size)
    
    return max_size
