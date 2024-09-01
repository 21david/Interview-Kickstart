'''
Equivalent to leetcode problem:
https://leetcode.com/problems/pascals-triangle
'''

'''
Top down recursive approach
TC: O(N^2)
Auxiliary SC: O(N) for the call stack
'''
mod = int(1e9+7)
def find_pascal_triangle(n):
    if n == 1:
        return [[1]]

    # Get the last row to compute the next row
    smaller_ans = find_pascal_triangle(n-1)
    last_arr = smaller_ans[-1]
    
    # Create the next row
    new_arr = [1]
    for i in range(1, len(last_arr)):
        new_arr.append( (last_arr[i] + last_arr[i-1]) % mod )
    new_arr.append(1)

    # Concatenate to the triangle
    return smaller_ans + [new_arr]


'''
Bottom up approach
TC: O(N^2)
Auxiliary SC: O(1)
'''
mod = int(1e9+7)
def find_pascal_triangle(n):
    ans = [[1]]
    
    for i in range(1,n):
        # Get the last row to compute the next row
        last_arr = ans[-1]
      
        # Create the next row
        new_arr = [1]
        for j in range(1, len(last_arr)):
            new_arr.append( (last_arr[j] + last_arr[j-1]) % mod )
        new_arr.append(1)

        # Concatenate to the triangle
        ans.append(new_arr)
    
    return ans
