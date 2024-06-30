def find_zero_sum(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_str
    """
    """
    For each number in the array, we run the 2-sum algorithm on all the
    other numbers. 
    2-sum algorithm: Create a hashmap (multiset) of all the numbers and their count.
    Then, we can pass the array again, and for each number, we can compute the
    required number to get the target sum, and we can use the hash to check if
    we have that number (searching the hash is O(1), so this pass over the array
    would be O(N)). When we find a pair, we should reduce both counts by 1 in the 
    hash to prevent a duplicate. By the end, we should have all the 2-sum pairs.
    """
    
    ans = set()
    
    for i in range(len(arr)):
        temp = arr[i]
        arr[i] = None
        pairs = two_sum(arr, -temp)
        arr[i] = temp

        for tup in pairs:
            a, b = tup
            new_ans = None
            if temp < a:
                new_ans = f"{temp},{a},{b}"
            elif temp >= a and temp < b:
                new_ans = f"{a},{temp},{b}"
            else:
                new_ans = f"{a},{b},{temp}"
            
            ans.add(new_ans)
    
    return list(ans)
    
"""
Returns all the pairs in arr that sum to the target
"""
def two_sum(arr, target):
    # Populate the hash dictionary
    ele_count = {}
    for item in arr:
        if item == None:
            continue
        if item in ele_count:
            ele_count[item] += 1
        else:
            ele_count[item] = 1
    
    # Find all pairs
    ans = set()
    for key, value in ele_count.items():
        complement_num = target - key
        
        # edge case where complement_num == key (current num)
        if key == complement_num and value >= 2:
            ans.add((key, key))
            
        if complement_num in ele_count and key != complement_num:
            if key < complement_num: # keep sorted to avoid duplicates in set
                ans.add((key, complement_num))
            else:
                ans.add((complement_num, key))
                
    return ans
