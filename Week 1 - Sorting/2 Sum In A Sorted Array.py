"""
This problem gives a sorted array (possibly with duplicates) and asks to find any pair of numbers that sum to the target.
It asks for the indices of these numbers in the array, or [-1,-1] if there is no answer.

Example:
{
"numbers": [1, 2, 3, 5, 10],
"target": 7
}

Output:
[1, 3]
"""

def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    """
    Hash map approach.
    Create a hash map that stores all the numbers and their indices.
    Then, iterate through the array, calculate the number that sums with
    the current number to the target number, and then search for it with
    the hash map. If it is found, we found a pair and can return the indices.
    The indices are needed because if we get to a number that is exactly
    half the target, we need to make sure that there is another one, so
    that we don't use the same number twice as a two-sum pair. So the values
    in the map can be arrays to store as many indices as needed and to quickly
    check how many times that number was found.
    This approach is O(N) time complexity and O(N) auxiliary space complexity,
    because it passes over the array at most twice, and stores all the numbers
    and their indices in the hasp_map.
    """
    hash_map = {}
    
    # Populate array (O(N))
    for i, n in enumerate(numbers):
        if n in hash_map:
            hash_map[n].append(i)
        else:
            hash_map[n] = [i]
    
    # Search for a pair (O(N))
    for n in numbers:
        compliment_number = target - n
        if compliment_number == n:
            if len(hash_map[n]) >= 2:
                return [hash_map[n][0], hash_map[n][1]]
        else:
            if compliment_number in hash_map:
                return [hash_map[n][0], hash_map[compliment_number][0]]
    
    # If none were found
    return [-1,-1]
