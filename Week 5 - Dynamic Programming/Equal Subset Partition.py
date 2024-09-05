'''
Similar to LeetCode 
https://leetcode.com/problems/partition-equal-subset-sum/

However, this version allows negative numbers, and asks you for an actual
partitioning
in the form of an array of the same length as nums, where each number
is a 1 or a 0, representing which partition that number is a part of.

Example
"s": [10, -3, 7, 2, 1, 3]

Output:
[1, 1, 0, 0, 0, 1]

This output represents this partitioning:
[10, -3, 3] and [7, 2, 1]
'''

from functools import lru_cache
def equal_subset_sum_partition(nums):
    length = len(nums)
    if length == 1:
        return []
    
    # Get the sum we are looking for for each subset, which is the total sum // 2
    # If the total sum is not even, then there is no answer
    total = sum(nums)
    target, is_odd = divmod(total, 2)
    if is_odd: return []
    
    current_indices = []
    
    def explore_subsets(amount_left, curr_idx, inc_or_exc):  # (DFS style search)
        # Base cases
        # "curr_idx >= 1" prevents empty subset when target == 0
        if amount_left == 0 and curr_idx >= 1 and len(current_indices) < length:
            # Found a subset that sums exactly to the target
            # print(current_indices)
            return True
        elif curr_idx == length:
            # If no more numbers left to add, then this was not a valid subset
            return False

        # First, attempt to search all the subsets that include the current number
        current_indices.append(curr_idx)
        include_curr = explore_subsets(amount_left - nums[curr_idx], curr_idx+1, True)
        
        # Stop any further searching if we found an answer
        if include_curr:
            return True
            
        # If no answer is found, then search all subsets that exclude the current number
        current_indices.pop()
        exclude_curr = explore_subsets(amount_left, curr_idx+1, False)
        return exclude_curr
    
    # Only memoize if target is not 0. Otherwise, memoization produces incorrect result.
    if target != 0:
        explore_subsets = lru_cache(None)(explore_subsets)
    
    # Search all subsets for one that has a sum of target (total // 2)
    explore_subsets(target, 0, True)
    
    # If no indices found, there is no possible solution
    if not current_indices:
        return []
    
    # Convert the indices we gathered into array of 1s and 0s
    answer = [False] * length
    for idx in current_indices:
        answer[idx] = True
    
    return answer
