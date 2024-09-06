'''
Similar to LeetCode:
https://leetcode.com/problems/longest-common-subsequence

But it asks for the actual longest common subsequence.
If there are multiple, any of them counts as the correct answer.
'''

'''
Recursive solution
'''
def lcs(stringA, stringB) -> str:
    
    # a = index pointer for string A
    # b = index pointer for string B
    def solve_subproblem(a, b) -> str:
        if a == len(stringA) or b == len(stringB):
            return ''
        
        if stringA[a] == stringB[b]:
            '''
            Draw a line between the two current letters and figure out what's the maximum 
            number of lines you can draw for the rest of the letters in each string.
            '''
            return stringA[a] + solve_subproblem(a + 1, b + 1)
        else:
            '''
            At this point, we want to find the maximum number of lines that we can draw with the
            rest of the strings. By skipping a letter in each word, we allow it to consider lines
            that normally wouldn't be able to be drawn because another line would have been crossing
            it. So for every possible subproblem (which is just all different suffixes of each
            string being compared to each other), we find the maximum number of lines we can draw,
            then compare it with the other possibility and take the maximum each time.
            '''
            subseq1 = solve_subproblem(a + 1, b)
            subseq2 = solve_subproblem(a, b + 1)

            '''
            Return the result that had the most lines drawn,
            AKA the longer subsequence between the two.
            '''
            if len(subseq1) > len(subseq2):
                return subseq1
            else:
                return subseq2
    
    answer = solve_subproblem(0,0)
    return answer or '-1'



'''
Recursive memoized solution
'''
def lcs(stringA, stringB) -> str:
    memo = {}
    def solve_subproblem(a, b) -> str:
        if a == len(stringA) or b == len(stringB):
            return ''
        elif (a,b) in memo:
            return memo[(a,b)]
        
        if stringA[a] == stringB[b]:
            ans = stringA[a] + solve_subproblem(a + 1, b + 1)
            memo[(a,b)] = ans
            return ans
        else:
            subseq1 = solve_subproblem(a + 1, b)
            subseq2 = solve_subproblem(a, b + 1)

            if len(subseq1) > len(subseq2):
                ans = subseq1
                memo[(a,b)] = ans    
                return ans
            else:
                ans = subseq2
                memo[(a,b)] = ans    
                return ans
    
    answer = solve_subproblem(0,0)
    return answer or '-1'



'''
Recursive memoized solution
with functools.cache
'''
from functools import cache
def lcs(stringA, stringB) -> str:
    
    @cache
    def solve_subproblem(a, b) -> str:
        if a == len(stringA) or b == len(stringB):
            return ''
        
        if stringA[a] == stringB[b]:
            return stringA[a] + solve_subproblem(a + 1, b + 1)
        else:
            subseq1 = solve_subproblem(a + 1, b)
            subseq2 = solve_subproblem(a, b + 1)

            if len(subseq1) > len(subseq2):
                return subseq1
            else:
                return subseq2
    
    answer = solve_subproblem(0,0)
    return answer or '-1'



'''
Tabulated DP solution

This could be made more readable by adding a padding row and column to the DP table,
so that it doesn't have to worry about out of bounds errors and check if r or c is
zero.

Also, instead of storing the strings inside the DP table, we could store just the
length of the maximum LCS at each subproblem. Once we've solved the entire table, we
can derive one of the different possible LCSs by traversing through it and finding
which letters matched and caused the LCS to grow by one. This would save space and
allow us to take either one of the LCSs or as many as we want in the case that there
are multiple.
'''
def lcs(a, b):
    """
    Args:
     a(str)
     b(str)
    Returns:
     str
    """
    n = len(a)
    m = len(b)
    
    dp = [[None] * n for _ in range(m)]
        
    if a[0] == b[0]:
        dp[0][0] = a[0]
    else:
        dp[0][0] = ''
    
    for r in range(m):
        for c in range(n):
            if (r,c) == (0,0): continue
            if a[c] != b[r]:
                if r == 0:
                    dp[r][c] = dp[r][c-1]
                elif c == 0:
                    dp[r][c] = dp[r-1][c]
                else:
                    if len(dp[r-1][c]) > len(dp[r][c-1]):
                        dp[r][c] = dp[r-1][c]
                    else:
                        dp[r][c] = dp[r][c-1]
            else:
                if r == 0 or c == 0:
                    dp[r][c] = a[c]
                else:
                    dp[r][c] = dp[r-1][c-1] + a[c]

    # print(str(dp).replace('], ',']\n '))
    return dp[-1][-1] or '-1'
