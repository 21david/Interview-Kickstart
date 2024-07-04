"""
Problem: Similar to the 3 Sum problem, we need to return the number of triplets (subsets of size 3) that sum to less than the given target number.
This versions counts triplets with different indices as different triplets, even if the numbers are the same (so some duplicates may be included in the count).

Example:
{
"target": 4,
"numbers": [5, 0, -1, 3, 2]
}
output:
2

"""


def count_triplets(target, numbers):
    """
    Args:
     target(int32)
     numbers(list_int32)
    Returns:
     int32
    """
    """
    Brute force approach:
    Try all combinations of triplets and check if their sum is less than
    the target. If so, count it and return the total count at the end.
    O(N^3) time complexity. O(1) space complexity.
    """
    ct = 0
    N = len(numbers)
    
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if numbers[i] + numbers[j] + numbers[k] < target:
                    ct += 1
    
    return ct
