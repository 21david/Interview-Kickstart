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