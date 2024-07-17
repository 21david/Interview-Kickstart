"""
This problem gives you a list of sorted linked lists and asks you to merge them into
one big sorted linked list. Some linked lists may be empty, and there may be
duplicates.

Example:
{
"lists": [
[1, 3, 5],
[3, 4],
[7]
]
}

Output:
[1, 3, 3, 4, 5, 7]

"""

"""
For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
"""
def merge_k_lists(lists):
    """
    Args:
     lists(list_LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    """
    This solution will draw inspiration from the merging part
    of merge sort. It will find the smallest element from all k
    lists, add that to the new linked list, and repeat, until all
    are added to the new linked list.
    """
    k = len(lists)
    if k == 0:
        return None
        
    # Delete empty lists
    lists = [l for l in lists if l]
            
    # If all lists were empty, then there were no numbers
    if not lists:
        return None
    
    # Create pointers for each linked list
    pointers = [l for l in lists]
    
    ans = None  # the final linked list to be returned ("answer")
    t = None  # temporary pointer to traverse as new nodes get added
    
    while lists:
        smallest = find_smallest(lists, pointers)
        if not ans:
            ans = LinkedListNode(smallest)
            t = ans
        else:
            t.next = LinkedListNode(smallest)
            t = t.next
            
    return ans

# Out of all the linked lists, find the smallest element
def find_smallest(lists, pointers):
    smallest = None
    list_with_smallest = 0
    for i, linked_list in enumerate(lists):
        if smallest == None:
            smallest = pointers[i].value
            list_with_smallest = i
            continue
        elif pointers[i].value < smallest:
            smallest = pointers[i].value
            list_with_smallest = i
    
    # Move the pointer so that the smallest element gets left behind
    pointers[list_with_smallest] = pointers[list_with_smallest].next 
    
    # If this list went through all of its numbers already, delete it
    if not pointers[list_with_smallest]:
        del pointers[list_with_smallest]
        del lists[list_with_smallest]
        
    return smallest


"""
Solution 2:
Use a min heap to sort all the elements.
"""
"""
For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
"""
# import heapq
from heapq import heappush, heappop

# Monkey patch this function in to the LinkedListNode
# class for the min_heap to be able to sort by value
def __lt__(self, other):
    return self.value < other.value
    
LinkedListNode.__lt__ = __lt__

def merge_k_lists_2(lists):
    """
    Args:
     lists(list_LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    
    # Remove empty lists
    lists = [l for l in lists if l]
    
    # If there are no numbers, return None
    if not lists:
        return None
        
    # Add all numbers to the min heap
    min_heap = []
    for l in lists:
        a = l
        while a:
            heappush(min_heap, a)
            a = a.next

    # Create the final sorted linked list using the min heap
    head = heappop(min_heap)
    t = head
    
    while min_heap:
        smallest = heappop(min_heap)
        t.next = smallest
        t = t.next
    
    # If the last node was pointing to another node, remove pointer
    # to prevent loops
    t.next = None
        
    return head



"""
Solution 3
This approach also uses a min-heap, but it only stores the left-most element
of each linked list at a time. It builds the final sorted linked list one by
one with the min-heap, until all elements are added.
"""
"""
For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
"""
from heapq import heappush as push, heappop as pop

def merge_k_lists_3(lists):
    """
    Args:
     lists(list_LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    """
    Create a min-heap that stores the first element of each sorted
    linked list. We will repeatedly use this to get the next
    smallest element and build our final sorted linked list one
    by one.
    The items in this min heap will have to be pairs: the value
    of the element, and the index of the list that it came from.
    This will allow us to get the next element from that list so that
    we continually have the left-most element of each linked list.
    """
    # Construct heap
    heap = []
    for i, l in enumerate(lists):
        if l:
            push(heap, (l.value, i))
    
    # If there were no numbers, return None
    if not heap:
        return None
    
    # Dummy node to append the rest of the nodes
    dummy = LinkedListNode(None)
    t = dummy # temp pointer to traverse the list as we add nodes
        
    # One by one, extract the minimum element from one of the linked lists
    while heap:
        smallest_val, list_idx = pop(heap)
        t.next = lists[list_idx]
        t = t.next
        lists[list_idx] = lists[list_idx].next
        if lists[list_idx]:
            push(heap, (lists[list_idx].value, list_idx))
    
    # Discard dummy node and return the final sorted linked list
    return dummy.next
