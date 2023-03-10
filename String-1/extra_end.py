# Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length
# will be at least 2.
#
#
# extra_end('Hello') → 'lololo'
# extra_end('ab') → 'ababab'
# extra_end('Hi') → 'HiHiHi'

def extra_end(str):
    return "".join(x[-2:] * 3 for x in str.split())
