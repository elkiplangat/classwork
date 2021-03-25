'''


'''


def fibonacci(n):
    if n < 0:  # check for non-negative
        return
    elif n == 0:  # base case
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # recursive part; the function calls itself using new input


def moosonacci(n):
    if n < 0:  # check for negative input
        return
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return moosonacci(n - 1) + moosonacci(n - 2) + moosonacci(n - 3)  # recursive part, calls itself using new input


def substr(c, r, s):
    if not s:  # if the string is empty
        return ""
    elif s[:1] == c:  # if the string starts with c, replace it with r

        return r + substr(c, r, s[1:])
    else:  # else, add this character and go to the next one
        return s[0] + substr(c, r, s[1:])
