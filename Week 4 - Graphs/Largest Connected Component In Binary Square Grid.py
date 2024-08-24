'''
This problem is equivalent to https://leetcode.com/problems/making-a-large-island
'''

def largest_connected_component(grid):
    """
    Args:
     grid(list_list_int32)
    Returns:
     int32
    """
    R = len(grid)
    C = len(grid[0])
    max_size = 0
    in_bounds = lambda r, c: (0 <= r < R) and (0 <= c < C)
    directions = [(1,0), (-1,0), (0,1), (0,-1)] 
    
    def dfs(r, c, value):
        if not (in_bounds(r,c) and grid[r][c]) or grid[r][c] == value: 
            return 0
        
        grid[r][c] = value
        
        size = 1
        for dr, dc in directions:
            size += dfs(r + dr, c + dc, value)
            
        return size
    
    # Explore islands, find sizes, and mark them with their IDs and sizes
    island_count = 0  # Serves as an ID for each island
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                island_count += 1
                size = dfs(r, c, -1)
                max_size = max(max_size, size)
                # Fill island with its size
                dfs(r, c, (size, island_count))
            
    # Find which spot will create the largest size
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:
                neighboring_islands = []  
                neighboring_islands_set = set()  
                for dr, dc in directions:
                    if not in_bounds(r + dr, c + dc):
                        continue
                    neighbor_location = grid[r + dr][c + dc] 
                    if neighbor_location == 0:
                        continue
                    neighboring_islands += [grid[r + dr][c + dc][0]] if neighbor_location[1] not in neighboring_islands_set else [0]
                    neighboring_islands_set.add(neighbor_location[1])
                
                max_size = max(max_size, sum(neighboring_islands) + 1)
                
    return max_size


'''
"grid": [
[1,1,1,0,1,0],
[1,0,1,0,1,1],
[1,0,0,0,0,1],
[0,0,0,1,0,0],
[1,1,0,0,0,0]
]
=> 11
'''
