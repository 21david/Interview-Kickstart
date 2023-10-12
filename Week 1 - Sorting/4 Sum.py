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
    
    # [-1, 0, 0, 1, 2, 3]
    
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
