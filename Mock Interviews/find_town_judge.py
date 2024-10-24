'''
Oct 24, 2024

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
'''

'''
Notes:
The input can be represented as a graph.
The town judge should have 0 outgoing edges and n-1 incoming edges.
There has to be at least n-1 edges.

-- Example 2 --
Input: n = 3, trust = [[1,3],[2,3],[1,2]]
Output: 3

person: [outgoing edges, incoming edges] # array of arrays
1: [2, 0]
2: [1, 1]
3: [0, 2]

We're checking for [0, n-1]

-- Example 3 --
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

1: [1, 1]
2: [1, 0]
3: [1, 2]
'''

def find_town_judge(n, trust):
    if n == 1:
        return 1
    elif len(trust) < n - 1:
        return -1
      
    info = [[0] * 2 for _ in range(n+1)]
    
    for ai, bi in trust:
        info[ai][0] += 1
        info[bi][1] += 1
        
    # print(str(info).replace('], ', '],\n '))
    
    person = 1
    for out, inc in info:
        if out == 0 and inc == n-1:
            return person - 1
        person += 1
    
    return -1
            
print(find_town_judge(2, [[1,2]]))
print(find_town_judge(3, [[1,3],[2,3],[1,2]]))
print(find_town_judge(3, [[1,3],[2,3],[3,1]]))
