
'''
Recusrive solution to the towers of hanoi problem.
Time and space complexity are O(2^n).
'''
def tower_of_hanoi(n):
    """
    Args:
     n(int32)
    Returns:
     list_list_int32
    """
    answer = []
    
    def helper(n, src, dst):
        # base case: when there is only one disk
        if n == 1:
            answer.append([src, dst])
            return
            
        aux = 6 - src - dst
        
        # move all n-1 disks from src to aux
        helper(n-1, src, aux)
        
        # move bottom disk to dst
        answer.append([src, dst])
        
        # move all n-1 disks from aux to dst
        helper(n-1, aux, dst)
    
    helper(n, 1, 3)
    return answer
