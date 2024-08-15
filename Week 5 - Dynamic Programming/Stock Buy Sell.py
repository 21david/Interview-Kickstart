'''
This problem is the equivalent of LeetCode 121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
(Minor differences)
'''

'''
To solve the problem, start by iterating through the input array from right to left. 
As you traverse the array, keep track of the maximum value encountered so far. Store 
this maximum value in a separate array of the same length as the input array.

Once you have the array of maximum values, calculate the differences between this 
array and the corresponding elements in the input array. The goal is to find the 
maximum difference, which represents the maximum profit that can be achieved.

If the maximum difference found is zero, it means no profit can be made from the input 
array, so return -1. 
'''
def find_maximum_profit(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     int32
    """
    max_v = arr[-1]
    maxs = [0] * len(arr)
    
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > max_v:
            max_v = arr[i]
            
        maxs[i] = max_v
    
    return max(maxs[i] - arr[i] for i in range(len(arr))) or -1
