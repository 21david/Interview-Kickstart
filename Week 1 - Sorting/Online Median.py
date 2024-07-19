"""
The problem gives you an array of integers. It asks you to calculate the median
of all the integers as they are added to an empty list one by one. So, for each 
integer, it must be added to all the previous integers, and a median of all those
integers must be calculated. The expected return value is a list of all the medians
that were calculated as they were added to a 'stream'.

Example:
{
"stream": [3, 8, 5, 2]
}

Output:
[3, 5, 5, 4]

Iteration	  Stream	      Sorted Stream	  Median
1             [3]             [3]             3
2             [3, 8]          [3, 8]          (3 + 8) // 2 => 5
3             [3, 8, 5]       [3, 5, 8]       5
4             [3, 8, 5, 2]    [2, 3, 5, 8]    (3 + 5) // 2 => 4
"""
from heapq import heappush as push, heappop as pop

class MinHeap:
    def __init__(self, *nums):
        self.arr = []
        for n in nums:
            self.arr.append(n)
    
    def push(self, num):
        push(self.arr, num)
        
    def pop(self):
        return pop(self.arr)
        
    def peek(self):
        return self.arr[0]
        
    def size(self):
        return len(self.arr)
        
class MaxHeap:
    def __init__(self, *nums):
        self.arr = []
        for n in nums:
            self.arr.append(-n)
    
    def push(self, num):
        push(self.arr, -num)
        
    def pop(self):
        return -pop(self.arr)
        
    def peek(self):
        return -self.arr[0]
        
    def size(self):
        return len(self.arr)

def online_median(stream):
    """
    Args:
     stream(list_int32)
    Returns:
     list_int32
    """
    """
    Optimized approach:
    Use a max-heap for numbers less than or equal to the median, and 
    a min-heap for numbers greater than the median. The median will
    always either be the greatest element in the max-heap (when there
    is an odd number of total elements in both), or the floored average
    of the first element in both heaps (when there is an even number of
    total elements in both).
    Adding a number will be O(log n) with this approach, instead of O(n)
    if we kept a sorted sub-array and inserted each new number into it.
    So the total time complexity is O(n log n).
    The auxiliary space complexity is O(n) because we store each 
    number into a heap.
    The output space complexity is O(n) for all the medians.
    """
    max = MaxHeap(stream[0])  # store numbers that are < median
    min = MinHeap()  # store numbers that are >= median
    ans = [stream[0]]  # store the final answer
    nums_added = 1
    cur_median = stream[0]
    
    for n in stream[1:]:
        # Add number to the correct heap
        nums_added += 1
        if n > cur_median:
            min.push(n)
        else:
            max.push(n)
            
        # Maintain as close to equal lengths as possible
        # and when there is an odd number of elements, make
        # sure that the max heap has the extra element
        if min.size() >= max.size() + 1:
            max.push(min.pop())
        elif max.size() == min.size() + 2:
            min.push(max.pop())
            
        # Calculate median
        if nums_added % 2 == 0:
            # Even number: calculate average
            cur_median = (min.peek() + max.peek()) // 2
        else:
            cur_median = max.peek()
            
        ans.append(cur_median)
    
    return ans


"""
Solution 2:
This is the same as above, but uses negation to turn a min-heap
into a max-heap. It is shorter but harder to understand.
"""
from heapq import heappush as push, heappop as pop

def online_median_2(stream):
    """
    Args:
     stream(list_int32)
    Returns:
     list_int32
    """
    """
    Optimized approach:
    Use a max-heap for numbers less than or equal to the median, and 
    a min-heap for numbers greater than the median. The median will
    always either be the greatest element in the max-heap (when there
    is an odd number of total elements in both), or the floored average
    of the first element in both heaps (when there is an even number of
    total elements in both).
    Adding a number will be O(log n) with this approach, instead of O(n)
    if we kept a sorted sub-array and inserted each new number into it.
    So the total time complexity should be O(n log n).
    The auxiliary space complexity should be O(n) because we store each 
    number into a heap.
    The output space complexity is O(n) for all the medians.
    Note that a workaround is used for the max-heap. All numbers are negated
    when added (so that larger numbers have the highest priority) and 
    negated again when removed.
    """
    max = [-stream[0]]  # store numbers that are < median
    min = []  # store numbers that are >= median
    ans = [stream[0]]  # store the final answer
    nums_added = 1
    cur_median = stream[0]
    
    for n in stream[1:]:
        # Add number to the correct heap
        nums_added += 1
        if n > cur_median:
            push(min, n)
        else:
            push(max, -n)
            
        # Maintain as close to equal lengths as possible
        # and when there is an odd number of elements, make
        # sure that the max-heap has the extra element
        if len(min) >= len(max) + 1:
            push(max, -pop(min))
        elif len(max) == len(min) + 2:
            push(min, -pop(max))
            
        # Calculate median
        if nums_added % 2 == 0:
            # Even number: calculate average
            cur_median = (min[0] - max[0]) // 2
        else:
            cur_median = -max[0]
            
        ans.append(cur_median)
    
    return ans
