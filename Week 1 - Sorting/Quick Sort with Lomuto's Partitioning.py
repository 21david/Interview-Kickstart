import random

def quick_sort(arr):
    helper(arr, 0, len(arr))

def helper(arr, start, end):
    if end - start <= 1:
        return
    
    partitionIdx = lomuto_partition(arr, start, end)
    # everything to left of partitionIdx is lesser, everything to right is greater
    helper(arr, start, partitionIdx)
    helper(arr, partitionIdx+1, end)

def lomuto_partition(arr, start, end):
    # random pivot
    randIdx = random.randint(start, end-1)
    pivot = arr[randIdx]
    arr[start], arr[randIdx] = arr[randIdx], arr[start]

    redPtr = start + 1  # everything to left of this ptr will be lesser

    for i in range(start+1, end):
        if arr[i] < pivot:
            # swap into left list and increment redPtr
            arr[i], arr[redPtr] = arr[redPtr], arr[i]
            redPtr += 1
    
    # swap pivot index into end of left list, which is its final position
    arr[start], arr[redPtr-1] = arr[redPtr-1], arr[start]

    return redPtr - 1


arr = [5, 1, 8, 3, 7, 0, 2, 4, -1]
quick_sort(arr)
print(arr)  # [-1, 0, 1, 2, 3, 4, 5, 7, 8]
