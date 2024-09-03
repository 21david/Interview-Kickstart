'''
Equivalent to LeetCode problem:
https://leetcode.com/problems/paint-fence
'''

'''
Recursive solution
'''
mod = int(1e9+7)
def number_of_ways(n, k):
    # post = the number of the post we are coloring
    # color_streak = how many times we have picked the same color
    def find_ways(post, color_streak):
        if color_streak > 2:
            # If we painted three in a row the same color, backtrack
            # Return 0 because this can't lead to any valid results or combinations
            return 0
        elif post == n:
            # If we painted all the posts successfully, then this is one valid way 
            # to color the fence
            return 1
            
        # Paint the next post the same color as the current post
        result1 = find_ways(post + 1, color_streak + 1)
        
        # Paint the next post a different color
        result2 = find_ways(post + 1, 1)
        
        # Since there are (k - 1) different colors than the current color, 
        # we multiply result2 by (k - 1) and add that to result1
        return (result1 + (k - 1) * result2) % mod
    
    # Since the result is the same no matter which color we start with, 
    # we can calculate the ways for one color (any arbitrary color) 
    # and multiply by the total number of colors
    return (find_ways(1, 1) * k) % mod


