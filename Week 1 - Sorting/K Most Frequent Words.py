"""
Problem: Given a list of strings and an integer K, return the K most frequent words in order of most frequent to least frequent.
Words with equal frequency should be sorted lexicographically.

Example
{
"k": 4,
"words": ["car", "bus", "taxi", "car", "driver", "candy", "race", "car", "driver", "fare", "taxi"]
}

Output:
["car", "driver", "taxi", "bus"]

"""

def k_most_frequent(k, words):
    """
    Args:
     k(int32)
     words(list_str)
    Returns:
     list_str
    """
    '''
    Create a hashmap/hash dictionary that stores the word
    as the key and its count as the value. (O(N))
    Then sort the items primarily by their count and secondarily by 
    their letters. (O(NlogN))
    Then get the first K words in this sorted list. (O(K))
    '''
    
    # Populate hash dictionary O(N)
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    # Sort by frequency and lexicographically (O(NlogN))
    sorted_by_count = {word: count for word, count in sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))}
    
    # Get the K most frequent words
    ans = []
    for word in sorted_by_count.keys():
        if k == 0:
            break
        ans.append(word)
        k -= 1
    
    return ans
