"""
This problem gives you an array of numbers (may contain duplicates) and asks you to return an array of the 
k most frequent elements in that array. If there are multiple solutions, any one is valid.

Example
{
"arr": [1, 2, 3, 2, 4, 3, 1],
"k": 2
}

Output:
[3, 1]
"""

"""
Solution 1
Quick select approach
"""
def find_top_k_frequent_elements(arr, k):
    """
    Args:
     arr(list_int32)
     k(int32)
    Returns:
     list_int32
    """
    """
    Since it is asking for the k most frequent elements in whatever order,
    quick select can be used. First, we count the frequencies of
    each element and store that in a multiset. Then, we use quick select, 
    using the frequencies, to get the k most frequent elements.
    The average time complexity of this entire operation should be O(N).
    The auxiliary space complexity will be O(N) for the multiset.
    """
    # Count frequencies
    freqs = {}
    for n in arr:
        if n in freqs:
            freqs[n] += 1
        else:
            freqs[n] = 1
            
    # Converting to list for easier use
    nums = []
    for item in freqs.items():
        nums.append(item)
    # nums is an array of tuples (number, frequency))
    
    quick_select(nums, k, 0, len(nums)-1)
    
    ans = []
    for i in range(k):
        ans.append(nums[i][0])
    
    return ans
    
# Sorting in decending order
def quick_select(nums, t, s, e):
    if s >= e:
        return
    
    pos = partition(nums, t, s, e)
    
    if pos == t:
        return
    elif pos < t:
        quick_select(nums, t, pos+1, e)
    else:
        quick_select(nums, t, s, pos-1)
    
def partition(nums, t, s, e):
    if s >= e:
        return
    
    # Quick select using frequencies
    # Pick random pivot to reduce likelihood of worst case scenario
    i = random.randint(s, e)
    nums[i], nums[s] = nums[s], nums[i]
    
    # Lomuto partition
    a = s
    for b in range(s, e+1):
        if nums[b][1] > nums[s][1]:
            a += 1
            nums[b], nums[a] = nums[a], nums[b]
            
    # Swap partition to end of greater list, putting it into final position
    nums[s], nums[a] = nums[a], nums[s]
            
    # a is the index of the pivot's final position
    # which can be used for the next quick select iteration
    return a



"""
Solution 2
Counting sort approach
"""
def find_top_k_frequent_elements_2(arr, k):
    """
    Args:
     arr(list_int32)
     k(int32)
    Returns:
     list_int32
    """
    """
    Counting sort approach:
    
    Create an array where each index represents a frequency. This array
    will be length len(arr)+1 because in the worst case where the array
    consists of all the same number, the frequency will be len(arr)+1
    and that number will be stored at that index.
    
    Travesrsing this list from end to start will give the most frequent
    numbers in order from greatest to least.
    
    First, we need to count the frequencies of each number and store in 
    a map.
    
    Then, we use the frequencies to fill the frequencies array.
    
    Finally, we need to traverse that array backwards, put the most frequent
    element in a final array, and repeat k times until we have the k most
    frequent elements in that final array.
    
    Data structures needed:
    freq_dict (dictionary)
    freq_arr (array)
    ans (array, for the final answer)

    Time complexity: O(N) because we only make linear passes over the data structures,
    which have at most length N+1. Auxiliary space complexity: O(N) for the data structures.
    """
    freq_dict = {}
    for n in arr:
        freq_dict[n] = freq_dict.get(n, 0) + 1
        
    freq_arr = [[] for _ in range(len(arr) + 1)]
    
    for num, freq in freq_dict.items():
        freq_arr[freq].append(num)
    
    p = len(arr)
    ans = []
    
    while k > 0:
        if freq_arr[p]:
            while k > 0 and freq_arr[p]:
                ans.append(freq_arr[p][-1])
                freq_arr[p].pop()
                k -= 1
            if k == 0:
                return ans
        p -= 1
    
    return ans
