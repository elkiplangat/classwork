steps = 1  # global variable that we will use to count the number of steps.


def MothraCount(a, b):
    global steps
    if a * b == 1:  # base case when  both a and b == 1
        return steps
    elif b > 1:
        steps += 1
        return MothraCount(a, b - 1)
    elif a > 1 and b == 1:
        steps += 1
        return MothraCount(a - 1, b)
