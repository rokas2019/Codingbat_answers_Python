# Given an int array length 2, return True if it contains a 2 or a 3.
#
#
# has23([2, 5]) → True
# has23([4, 3]) → True
# has23([4, 5]) → False

def has23(nums):
    return True if nums[0] == 2 or nums[1] == 2 else nums[0] == 3 or nums[1] == 3
