# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the
# sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
#
#
# lucky_sum(1, 2, 3) → 6
# lucky_sum(1, 2, 13) → 3
# lucky_sum(1, 13, 3) → 1

def lucky_sum(a, b, c):
    list_1 = [a, b, c]
    sum_1 = 0
    range_to = None

    for i in list_1:
        if i == 13:
            range_to = list_1.index(i)

    for y in list_1[0:range_to]:
        sum_1 += y

    return sum_1


def lucky_sum_2(a, b, c):
    total = 0

    for n in (a, b, c):
        if n != 13:
            total += n
        else:
            break

    return total
