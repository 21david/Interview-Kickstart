'''
Very similar to LeetCode 140. Word Break II
https://leetcode.com/problems/word-break-ii/
'''

def word_break_count(dictionary, txt):
    """
    Args:
     dictionary(list_str)
     txt(str)
    Returns:
     int32
    """
    L = len(txt)
    # Tabulation DP. each index i represents substring from 0 to i and how many ways
    # there are to construct that substring. tab[0] = 1 means there's 1 way to create empty
    # substring (by using no words)
    tab = [0] * (L + 1)
    tab[0] = 1
    
    for i in range(L):
        if tab[i] is not None:
            for word in dictionary:
                # if the word continues the current substring
                if word == txt[i:i+len(word)]:
                    # update new index because we found new ways to make that
                    # substring. update it with number of new ways we found (tab[i])
                    # + number of ways that were already found (tab[i+len(word)]).
                    # i guess the specific ways will not overlap with eachother
                    # bc we're only considering each combination one time.
                    tab[i+len(word)] = tab[i] + tab[i+len(word)]
    
    return tab[L]
