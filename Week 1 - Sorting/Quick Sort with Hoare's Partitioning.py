import random

def quick_sort(arr):
    helper(arr, 0, len(arr))

def helper(arr, start, end):
    if end - start <= 1:
        return
    
    partitionIdx = hoare_partition(arr, start, end)
    # everything to left of partitionIdx is lesser, everything to right is greater
    helper(arr, start, partitionIdx)
    helper(arr, partitionIdx+1, end)

def hoare_partition(arr, start, end):
    # random pivot
    randIdx = random.randrange(start, end)
    pivot = arr[randIdx]
    arr[start], arr[randIdx] = arr[randIdx], arr[start]

    l = start + 1
    r = end - 1

    while l <= r:
        while l <= r and arr[l] < pivot:
            l += 1
        while l <= r and arr[r] >= pivot:
            r -= 1

        if l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    
    arr[start], arr[r] = arr[r], arr[start]
    return r


arr = [5, 1, 8, 3, 7, 0, 2, 4, -1]
quick_sort(arr)
print(arr)  # [-1, 0, 1, 2, 3, 4, 5, 7, 8]
