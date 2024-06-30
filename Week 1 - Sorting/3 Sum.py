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


#############################################
# Another solution:
def find_zero_sum_2(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_str
    """
    
    '''
    O(N^2) approach:
    For each element, perform a O(N) Two Sum algorithm on the
    rest of the elements (the two numbers must add to the current
    number times -1). If we sort the algorithm, we can perform
    the Two Sum algorithm with two pointers, which avoids
    using extra memory.
    Optimization: for there to be three numbers that add to 0,
    There must be negative numbers and positive numbers, OR
    they must all be 0s. So we can check the first and last elements
    to see what the array looks like. If they are either both
    negative or positive, then there wont be an answer and we can 
    return an empty array. If they are both 0s, we can return 
    [[0,0,0]]
    '''
    
    arr.sort()
    
    if len(arr) <= 2 or arr[0] < 0 and arr[-1] < 0 or arr[0] > 0 and arr[-1] > 0:
           return []
    elif arr[0] == 0 and arr[-1] == 0:
        return ['0,0,0']
    
    triplets = set()
    
    for i in range(len(arr)-2):
        target = -arr[i]
        
        if target < 0:
            # if current number is positive
            # there will not be any solutions
            break
        
        # two sum algorithm on the rest of the elements
        k = len(arr)-1
        j = i + 1
        while j < k:
            sum = arr[j] + arr[k]
            
            if sum == target:  # found a triplet
                triplets.add(f'{arr[i]},{arr[j]},{arr[k]}')
                j += 1
                k -= 1
            elif sum > target:
                k -= 1
            else:
                j += 1
            
    return list(triplets)
