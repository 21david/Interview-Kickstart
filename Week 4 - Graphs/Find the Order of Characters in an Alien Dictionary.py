
def find_order(words):
    """
    Args:
     words(list_str)
    Returns:
     str
    """
    '''
    If we compare two words, we can almost always get information about the relative order of two letters.
    For example: 'baa' and 'abcd' tells us that b goes before a. So we need to do this until we get enough 
    information to create the sorted order for all the letters. In the worst case, we may need to compare
    every word with every other word. (An optimization is to only compare every adjacent pair of words.)

    The strategy to find out a piece of information from two words is to compare every ith letter of both
    words until they differ. When they differ, we can tell which letter comes before the other.
    
    With each piece of information we get, such as "b comes before a", we can form a graph, where each
    statement like that is an edge. This should form a DAG, directed, acyclic graph. From that, we can
    perform a topological sort to get the sorted order of the letters.
    '''
    if len(words) == 1:
        return words[0][0]
        
    letters = set()
    
    def compare_words(word1, word2):
        for i in range(min(len(word1), len(word2))):
            c1 = word1[i]
            c2 = word2[i]
            
            letters.update({c1, c2})
            
            if c1 != c2:
                return (c1, c2) # c1 comes before c2
                
        return None
        
    edges = set()
    
    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        
        edge = compare_words(word1, word2)
        if edge: edges.add(edge)
    
    order = []
    
    # iterate through edges, removing the node that has no incoming edges
    # repeat this until the last node
    found_more = True
    while found_more:
        # Build a set that counts outgoing and incoming edges for each node
        multiset = {}
        found_more = False
        for c1, c2 in edges:
            if c1 in order:
                continue
            found_more = True
            if c1 not in multiset.keys():
                multiset[c1] = [1, 0]
            else:
                multiset[c1][0] += 1
            if c2 not in multiset.keys():
                multiset[c2] = [0, 1]
            else:
                multiset[c2][1] += 1
        
        # Find the one that has no incoming edges
        for char, lst in multiset.items():
            if lst[1] == 0:
                order.append(char)
                break
            
    # The last letter doesn't get added, so we need to add it
    for c in letters:
        if c not in order:
            order.append(c)
            break
    
    return ''.join(order)
