'''
This problem seems to be the equivalent of 
https://www.geeksforgeeks.org/cutting-a-rod-dp-13/#

It gives you an array of prices. The value at index i represents the price
of a rod of length (i+1). It asks to find the maximum total profit that can
be made by making as many cuts as needed.

Example:
"price ": [1, 5, 8, 9]

Output:
10

The output is 10 because the maximum profit can be made by cutting the rod
(length 4, the length of the array), into two rods of size 2. A rod of size
2 is worth 5 (price[2-1] = 5), so combined they are worth 10.
'''

'''
I think that for the input number N (length of price), we can try to split it into every pair of two 
non-negative numbers that add to it, starting with (0, N), then (1, N-1), and continue until halfway, 
because afterwards it would just repeat in reverse order. For example for N = 5, we would try:
(0,5)
(1,4)
(2,3)

For each of these, we would repeat the exact same thing on both numbers. We would ideally also memoize 
the result of each attempt to not recalculate the same values multiple times. If we do it like this, 
then I think each of these pairs will collectively represent all the ways to break down a number, all 
the way from adding 1 N times, to adding 2s and 3s, to just adding N.

For example, if we take (1,4) for the first time, then we check f(1), which just checks (0,1), and then 
we check f(4), which checks (0,4), (1,3), and (2,2). 
So the result that we calculate for (1,4) will take into account all possible cuts after cutting it into 
1 and 4: 
    1+(4), 1+(1+3), 1+(2+2) 
and will represent the maxiumum out of those. The same will go for the next possible cut in our original 
problem: (2,3). It will find the maximum for all subproblems (all further cuts): 
    2+(3), 2+(1+2), and so forth. 

So basically, by the end, we just calculate the maximum by finding the maximum of all the sub-maximums.
This should be possible to solve recursively, with memoization, and with tabulation.
'''

'''
Recursive solution
'''
def get_maximum_profit(price):
    """
    Args:
     price(list_int32)
    Returns:
     int32
    """
    
    # find the maximum profit possible for a rod of size n
    def help(n):
        if n == 0:
            return 0
        elif n == 1:
            return price[0]
        
        max_profit = price[n-1]
        
        # try every possible cut for the first cut
        for i in range(1, n//2+1):
            rod1_max = help(i)
            rod2_max = help(n-i)
    
            max_profit = max(max_profit, rod1_max + rod2_max)
            
        return max_profit
    
    return help(len(price))


'''
Recursive solution with memoization
'''
def get_maximum_profit(price):
    # Find the maximum profit possible for a rod of size n
    def help(n, memo={ 0:0, 1:price[0] }):
        if n in memo:
            return memo[n]
        
        max_profit = price[n-1]
        
        # Try every possible cut for the first cut
        for i in range(1, n//2+1):
            rod1_max = help(i)
            rod2_max = help(n-i)
    
            max_profit = max(max_profit, rod1_max + rod2_max)
        
        memo[n] = max_profit
        return max_profit
    
    return help(len(price))


'''
Another recursive solution with memoization,
without using an inner function.
This one makes many copies of subarrays of the price array,
so it is not space optimized.
'''
def get_maximum_profit(price, memo = { 0:0 }):
    n = len(price)
    
    # Base case, rod of size 1 can't be cut anymore
    if n == 1:
        return price[0]
    
    # Check if we've already calculated max for this length
    if n in memo:
        return memo[n]
    
    # Consider the price of not making any cuts
    max_profit = price[-1]
    
    # Try every possible cut for the first cut
    for i in range(1, n//2+1):
        rod1_max = get_maximum_profit(price[:i], memo)
        rod2_max = get_maximum_profit(price[:n-i], memo)

        max_profit = max(max_profit, rod1_max + rod2_max)
    
    # Store max profit for this length and return to parent caller
    memo[n] = max_profit
    return max_profit


'''
Recursive, memoized, and more space optimized than the above.
It uses an integer to keep track of what part of the array to use
instead of making a copy of the array.
'''
def get_maximum_profit(price, n=None, memo = { 0:0 }):
    # Initialize n in the first call, to use it for all recursive calls
    # n represents the current size of the rod/array (subarray starting from index 0)
    if n is None:
        n = len(price)
        
    # Base case, rod of size 1 can't be cut anymore
    if n == 1:
        return price[0]
    
    # Check if we've already calculated max for this length
    if n in memo:
        return memo[n]
    
    # Consider the price of not making any cuts
    max_profit = price[n-1]
    
    # Try every possible cut for the first cut
    for i in range(1, n//2+1):
        rod1_max = get_maximum_profit(price, i, memo)
        rod2_max = get_maximum_profit(price, n-i, memo)

        max_profit = max(max_profit, rod1_max + rod2_max)
    
    # Store max profit for this length and return to parent caller
    memo[n] = max_profit
    return max_profit


'''
Tabulated solution based off of the previous solutions.
It doesn't seem possible to optimize it anymore than this.
'max(dp[i], dp[j] + dp[i-j])' is doing the same thing as
'max_profit = max(max_profit, rod1_max + rod2_max)' in the
solutions above. 
The outer for loop is like the recursive calls, and the
inner for loop corresponds to the for loops above.
TC: O(N^2)
SC: O(N)
'''
def get_maximum_profit(price):
    dp = [0] + [x for x in price]
    
    for i in range(2, len(dp)):
        for j in range(1, i//2+1):
            dp[i] = max(dp[i], dp[j] + dp[i-j])
    
    return dp[-1]
