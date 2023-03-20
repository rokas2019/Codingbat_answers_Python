# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values,
# it does not count towards the sum.
#
#
# lone_sum(1, 2, 3) → 6
# lone_sum(3, 2, 3) → 2
# lone_sum(3, 3, 3) → 0

def lone_sum(a, b, c):
    set_1 = {a, b, c}
    list_1 = [a, b, c]
    sum_1 = sum(set_1) - (sum(list_1) - sum(set_1))
    return sum_1 if sum_1 > 0 else 0


def lone_sum_2(a, b, c):
    if a != b and b != c and c != a:
        return a + b + c
    elif a == b and b == c:
        return 0
    elif a == b:
        return c
    elif b == c:
        return a
    else:
        return b


def lone_sum_3(a, b, c):
    suma = 0
    if a != b and a != c:
        suma += a
    if b != a and b != c:
        suma += b
    if c != a and c != b:
        suma += c
    return suma


