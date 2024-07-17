"""
This problem gives you three sorted arrays, and asks you to return a list of 
all the elements that are in all three arrays. Duplicates may be in each array,
and duplicates are expected if they are also in all three arrays.

Example
{
"arr1": [1, 2, 2, 2, 9],
"arr2": [1, 1, 2, 2, 4, 8],
"arr3": [1, 1, 1, 2, 2, 2, 3, 5, 10, 20]
}

Output:
[1, 2, 2]


"""
def find_intersection(arr1, arr2, arr3):
    """
    Args:
     arr1(list_int32)
     arr2(list_int32)
     arr3(list_int32)
    Returns:
     list_int32
    """
    """
    Use three pointers. Push lesser pointers to the right until
    they all have the same number. Once they do, add that to the
    final array and push each pointer to the right by 1.
    Once at least one pointer is out of bounds, terminate.
    
    Time complexity: O(min(n1, n2, n3))
    Auxililary space complexity: O(1) for the pointers and max_val
    Output space complexity: O(min(n1, n2, n3))
    """
    p1, p2, p3 = 0, 0, 0
    ans = []
    
    while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
        if arr1[p1] == arr2[p2] == arr3[p3]:
            ans.append(arr1[p1])
            p1 += 1
            p2 += 1
            p3 += 1
            continue
        max_val = max(arr1[p1], arr2[p2], arr3[p3])
        if arr1[p1] < max_val:
            p1 += 1
        if arr2[p2] < max_val:
            p2 += 1
        if arr3[p3] < max_val:
            p3 += 1
    
    return ans if ans else [-1]
