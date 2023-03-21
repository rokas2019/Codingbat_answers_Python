# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other
# is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.
#
#
# close_far(1, 2, 10) → True
# close_far(1, 2, 3) → False
# close_far(4, 1, 3) → True

def close_far(a, b, c):
    a_b = abs(a - b)
    b_c = abs(b - c)
    a_c = abs(a - c)
    return(
        (a_b <= 1 and a_c >= 2 and b_c >= 2) !=
        (a_c <= 1 and a_b >= 2 and b_c >= 2)
    )


