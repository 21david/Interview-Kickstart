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
    O(N^2) approach:
    First sort all the numbers (O(NlogN)).
    Put a pointer on the second and last numbers.
    Loop over every number in the array from left to right:
    Sum the first, second and last numbers.
    If this sum is greater than or equal to the target, then
    we must use smaller numbers. Move the right pointer to the left
    to get the second biggest number. When the numbers in the two
    pointers plus the current number sum to less than the target,
    then we found a triplet, and replacing the right pointer with
    every number to its left (until reaching the left pointer) will 
    also be a triplet, so we can calculate all those triplets
    with just one subtraction (index of right ptr - index of left ptr).
    Then, we move the left pointer to the right and repeat until there
    are no more triplets. Once that is the case, the first number is done
    (we've found all triplets that include that number), and we can move
    to the next number. Each number will do a O(N) search, so altogether,
    it is O(N^2). This only uses constant extra memory space, so the
    space complexity is O(1).
    """
    numbers.sort()
    ct = 0
    N = len(numbers)
    for i in range(N):
        left, right = i+1, N-1
        while left < right:
            total = numbers[i] + numbers[left] + numbers[right]
            if total < target:
                ct += right - left
                left += 1
            else:
                right -= 1
    
    return ct


"""
The inner while loop:
 Pairs less than 4?
 -1, 0, 2, 3, 5
  ^        ^
  0  1  2  3  4

-1 and 3 sum to less than 4, and so will
-1 and every number between index 0 and 3.
So we can quickly count that there are 3
pairs here that sum to less than 4.
(3 - 0)

Then, we move the left pointer to the right to find more pairs.
 -1, 0, 2, 3, 5
     ^     ^
  0  1  2  3  4
0 + 3 add to less than 4, so we can calculate that there are
2 more pairs (3 - 1)

The sum is still less than 4, so we move the left pointer to the right
to find more pairs again.
 -1, 0, 2, 3, 5
        ^  ^
  0  1  2  3  4
This sums to greater than 4, so we would normally more the right pointer
to the left to see if the sum is less than 4, but in this case, the
pointers would touch, so there are no more pairs.


Pairs that summ to less than 4:
-1, 3
-1, 2
-1, 0
0, 3
0, 2

"""


def count_triplets_2(target, numbers):
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
