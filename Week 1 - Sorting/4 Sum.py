"""
Problem: Given an unsorted array (of integers) and a target integer number, find all the subsets of size 4 (quadruples) that sum to the target (order does not matter).

Example input:
{
"arr": [5, 2, 3, 4, -1, 1, -12],
"target": 10
}

output: [
    [5, 2, 4, -1],
    [2, 3, 4, 1]
]
"""

def four_sum(arr, target):
    """
    Args:
     arr(list_int32)
     target(int32)
    Returns:
     list_list_int32
    """
    '''
    O(N^3) approach is to run the O(N^2) three sum algorithm on each element.
    The if statements at the beginning of the for loops prevent the algorithm
    from finding the same quadruplets if there are 2+ equal elements in the array.
    The last if statement checks the last added quadruple to make sure it didn't
    find it again. This happens because many elements may repeat. This works because
    since the elements are sorted, it will come across each quadruple in order,
    so it only ever needs to check the last added one.
    So the first two if statements prevent duplicates involving the first two
    numbers of a quadruple, and the last if statement prevents duplicates
    involving the last two numbers of a quadruple.
    '''
    arr.sort()
    quadruples = []
    
    for i in range(len(arr)-3):
        if i > 0 and arr[i] == arr[i-1]:  # prevent duplicates
            continue
        # perform three sum solution on the rest of the array
        for j in range(i+1, len(arr)-2):  
            if j > i + 1 and arr[j] == arr[j-1]:  # prevent duplicates
                continue
            # perform two sum two-pointer solution on the rest
            l = j + 1
            r = len(arr) - 1
            
            while l < r:
                sum = arr[i] + arr[j] + arr[l] + arr[r]
                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
                else:  # found a quadruple
                    # check for duplicate
                    if len(quadruples) == 0 or quadruples[-1] != [arr[i],arr[j],arr[l],arr[r]]:
                        quadruples.append([arr[i],arr[j],arr[l],arr[r]])
                    
                    r -= 1
                    l += 1
                
    return list(quadruples)


####################################
# Another solution:

def four_sum(arr, target):
    """
    Args:
     arr(list_int32)
     target(int32)
    Returns:
     list_list_int32
    """
    """
    This builds on the 2-sum and 3-sum problems. We can re-use the solutions
    for those and build one layer on top of it to solve this one.
    To do that, we iterate through the array, and for each number, we
    run the 3-sum algorithm on all the other numbers (which will run the
    2-sum algorithm multiples times) to get all the quadruplets that sum to
    the target value.
    """

    temp_ans = set()    
    
    for i in range(len(arr)):
        triplets = three_sum(arr[i+1:], target - arr[i])
        for a, b, c in triplets:
            sort = sorted([a, b, c, arr[i]])
            temp_ans.add((sort[0],sort[1],sort[2],sort[3]))
    
    # convert to arrays
    final_ans = []
    for tup in temp_ans:
        final_ans.append(list(tup))
    
    return final_ans

def three_sum(arr, target):
    ans = set()
    
    for i in range(len(arr)):
        pairs = two_sum(arr[i+1:], target - arr[i])
        for a, b in pairs:
            sort = sorted([a, b, arr[i]])
            ans.add((sort[0],sort[1],sort[2]))
            
    return ans
    
def two_sum(arr, target):
    # Create hash dictionary to get each element and its count
    counts = {}
    for num in arr:
        if num == None:
            continue
        elif num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    # Iterate through array and find pairs using the dictionary
    ans = set()
    for num in arr:
        if num == None:
            continue
        complement_num = target - num
        if num != complement_num and complement_num in counts:
            if num < complement_num:
                ans.add((num, complement_num))
            else:
                ans.add((complement_num, num))
        elif num == complement_num and counts[num] >= 2:
            ans.add((num, complement_num))
            
    return ans
