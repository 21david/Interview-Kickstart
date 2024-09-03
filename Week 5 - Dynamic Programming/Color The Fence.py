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


'''
Recursive memoized solution
'''
mod = int(1e9+7)
def number_of_ways(n, k):
    # Memoization dictionary
    memo = {}

    # post = the number of the post we are coloring
    # color_streak = how many times we have picked the same color
    def find_ways(post, color_streak):
        if (post, color_streak) in memo:
            # If we've already computed a similar combination, return the result rather than recompute
            return memo[(post, color_streak)]
        elif color_streak > 2:
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
        answer = (result1 + (k - 1) * result2) % mod
        
        # Memoize and return
        memo[(post, color_streak)] = answer
        return answer
    
    # Since the result is the same no matter which color we start with, 
    # we can calculate the ways for one color (any arbitrary color) 
    # and multiply by the total number of colors
    return (find_ways(1, 1) * k) % mod


'''
Bottom-up tabulated dynamic programming solution.
I arrived at this solution by printing out the memo dictionary in the previous 
solution and then noticing that there was a pattern of multiplication and 
addition between the numbers. So, I mimicked that process using a matrix and 
found that it produced the same exact numbers and final answer.

TC: O(N)
SC: O(N)
'''
mod = int(1e9+7)
def number_of_ways(n, k):
    if n == 1: return k
    
    dp = [[k] + [0] * (n-2)]
    dp += [[k-1] + [0] * (n-2)]

    for i in range(1, n - 1):
        dp[1][i] = (dp[0][i-1] * (k-1)) % mod
        dp[0][i] = (dp[1][i-1] + dp[1][i]) % mod

    return (dp[0][-1] * k) % mod


'''
Space optimized bottom-up tabulated dynamic programming solution.
I arrived at this solution by noticing that in the previous tabulated 
solution, you only need the last two numbers for every calculation.

TC: O(N)
SC: O(1)
'''
mod = int(1e9+7)
def number_of_ways(n, k):
    if n == 1: return k
    
    c1, c2 = k, k - 1
    
    for _ in range(n - 2):
        c1 = c1 * (k-1) + c2
        c2 = c1 - c2
        c1 %= mod
        c2 %= mod
    
    return (c1 * k) % mod


"""
There is another way to solve this problem based on the fact that the outputs 
follow a very similar pattern to the Fibonacci numbers. So, there is an equivalent 
solution to each of the four approaches above that solves it in this manner.
I think my approaches above ask how many ways there are to paint all the rest 
of the posts when you're at a certain post, whereas these other solutions ask how 
many ways there are to paint all the posts up to that certain post. So, it's 
interesting how you can solve this problem from two directions, and 
each one looks different but arrives at the same answer. See Leetcode editorial.
"""

