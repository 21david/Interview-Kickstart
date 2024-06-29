"""
In one pass, using only constant extra memory, the array must be sorted with all Rs in the beginning, followed by all Gs, then followed by all Bs.

Sample input:
{
"balls": ["G", "B", "G", "G", "R", "B", "R", "G"]
}

Expected output:
["R", "R", "G", "G", "G", "G", "B", "B"]
"""

def dutch_flag_sort(balls):
    """
    Args:
     balls(list_char)
    Returns:
     list_char
    """
    rIdx = 0 # every element behind is an R
    gIdx = 0 # every element behind is a G or an R
    i = 0  # to iterate the array
    
    while i < len(balls):
        if balls[i] == "G":
            balls[i], balls[gIdx] = balls[gIdx], balls[i]
            gIdx += 1
        elif balls[i] == "R":
            balls[i] = balls[gIdx]
            balls[gIdx] = balls[rIdx]
            balls[rIdx] = "R"
            rIdx += 1
            gIdx += 1
            
        i += 1
    
    return balls

"""
Sample input trace:
#[G B G G R B R G] 
#[G B G G R B R G] i=0, g=0, r=0
#[G B G G R B R G] i=1, g=1, r=0
#[G B G G R B R G] i=2, g=1, r=0
#[G G B G R B R G] i=3, g=2, r=0
#[G G G B R B R G] i=4, g=3, r=0
#[R G G G B B R G] i=5, g=4, r=1
#[R R G G G B B G] i=6, g=5, r=2
#[R R G G G G B B] i=7, g=6, r=2
"""
