# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
#
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def counts_evens(nums):
    even = 0
    for i in nums:
        if i % 2 == 0:
            even += 1
    return even


def one_liner(nums):
    return len(list(filter(lambda x: (x % 2 == 0), nums)))
