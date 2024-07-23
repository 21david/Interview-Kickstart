"""
This problem gives you a number that has between 1 and 13 digits, a target integer number, and 
asks you to find every expression using the numbers, +, and *, that evaluate to the target. The
+ and *s can be added between any two numbers. An empty array is expected if there are no answers.

Example:
"s": "202",
"target": 4

Output:
["2+0+2", "2+02", "2*02"]
"""

last_zero = -1

def generate_all_expressions(s, target):
    """
    Args:
     s(str)
     target(int64)
    Returns:
     list_str
    """
    """
    We can follow a 'fill in the blanks' approach. There is a blank in between each pair 
    of digits in s that we must fill with either join, +, or *. We can try every combination
    of these in all the blanks, and keep only the ones that meet the requirement. 
    
    Optimization: If we passed the last 0, then a join, +, or * is always going to increase the 
    final result. Therefore, if out current result is already greater than the target, we can 
    stop (prune the tree) because we definitely won't reach an answer.

    Examples:
    1074321
    target = 5
    Answer: ["1*0*74+3+2*1", "1*0*7*4+3+2*1"]
    
    9099987893
    target = 25
    Answer: []
    
    050505
    target = 5
    Answer: ["0505*0+5", "050*5*0+5", "05+05*0*5", ... many more ]
    
    Time complexity: 
    O(3^N * N). We make 3 recursive calls for every letter except the first one. When we 
    reach the end of the string, we run O(N) algorithms to evaluate the expressions 
    (about 3^(N-1) total strings to evaluate in the worst case).

    Space complexity: 
    O(3^N * N). In the worst case, we may store and return 3^(N-1) strings with length between 
    N and 2N-1. The stack trace space complexity is O(N) because when it reaches the end of the
    string, there will be one call on the stack for every letter.
    """
    # Find index of last zero for optimization
    global last_zero
    r = len(s) - 1
    while r >= 0:
        if s[r] == '0':
            last_zero = r
            break
        r -= 1
    
    ans = []
    helper(s, s[0], 1, target, ans)
    return ans

# s - the original string
# slate - temporary variable to store the expression as we build it
# l - the index of the current letter we are considering
# target - the target value
# ans - array to store the final answers
def helper(s, slate, l, target, ans):
    global last_zero
    if l == len(s): # reached the end of the string
        # Keep this expression if it evaluates to target
        if eval_sum(eval_mult(slate)) == target:
            ans.append(slate)
        return
    
    # If we're past the last 0, every join, +, or * will only increase the
    # final result. So if we are already past the target, we can stop.
    if (l > last_zero and eval_sum(eval_mult(slate)) > target):
        return
    
    helper(s, slate + s[l], l+1, target, ans)
    helper(s, slate + '+' + s[l], l+1, target, ans)
    helper(s, slate + '*' + s[l], l+1, target, ans)
    
# Solve and remove all multiplication operators
def eval_mult(exp):
    l = 0 # left (start of multiplication expression)
    r = 1 # right (end of multiplication expression)
    m = None # index of multiplication operator
    
    while r < len(exp):
        if exp[r] == '+':
            l = r + 1
        elif exp[r] == '*':
            m = r
            r += 1
            while r < len(exp) and exp[r].isdigit():
                r += 1
            # We know locations of the start of the first number, the multiplication
            # operator, and the end of the last number. With these, we can multiply.
            product = int(exp[l:m]) * int(exp[m+1:r])
            exp = exp[:l] + str(product) + exp[r:]
            r = l # fix index of r after editing 'exp'
        r += 1
        
    return exp

# Solve and remove all sum operators, resulting in one final integer
def eval_sum(exp):
    nums = exp.split('+')
    return sum([int(num) for num in nums])
