# Given a string, return a new string where the first and last chars have been exchanged.
#
#
# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(str):
    return "".join(str[-1:] + str[1:-1] + str[0:1] if len(str) > 1 else str)
