
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104


-- Example 1 --
[7,1,5,3,6,4]
 7 6 6 6 6 4

Max difference = 5 (6 - 1)
'''

'''
TC = O(N)
SC = O(1)
'''
def max_profit(prices):
    maxes = [0] * len(prices)
    n = len(prices)
    ans = 0
    
    curr_max = prices[-1]
    for i in range(n-2, -1, -1):
        curr_max = max(curr_max, prices[i])
        ans = max(ans, curr_max - prices[i])
        
    return ans
    
print(max_profit([7,1,5,3,6,4]))


'''
TC = SC = O(N)
'''
def max_profit(prices):
    maxes = [0] * len(prices)
    n = len(prices)
    
    curr_max = prices[-1]
    maxes[-1] = curr_max
    for i in range(n-2, -1, -1):
        maxes[i] = max(prices[i], maxes[i+1])
        
    #print(maxes)
    
    ans = 0
    for i in range(n):
        ans = max(ans, maxes[i] - prices[i])
        
    return ans
    
print(max_profit([7,1,5,3,6,4]))
