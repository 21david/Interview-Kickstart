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

TC: O(N)
SC: O(N)
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


'''
This version does it in place, modifying the original 
array to save space and avoid using additional memory.

TC: O(N)
SC: O(1)
'''
def find_maximum_profit(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     int32
    """
    max_v = arr[-1]
    max_p = 0
    
    for i in range(len(arr)-1, -1, -1):
        max_v = max(max_v, arr[i])
        arr[i] = max_v - arr[i]
        max_p = max(max_p, arr[i])
    
    return max_p or -1


'''
One line solution just for fun
TC: O(N)
SC: O(1)
'''
def find_maximum_profit(arr):
    return max((max_v := max(max_v, arr[i+1]) if i < len(arr)-1 else arr[-1]) - arr[i] for i in range(len(arr)-1, -1, -1)) or -1
