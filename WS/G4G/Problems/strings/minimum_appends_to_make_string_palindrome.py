"""
amzn

http://www.geeksforgeeks.org/minimum-number-appends-needed-make-string-palindrome/
"""


def is_pal(li, s, e):
    while s <= e:
        if li[s] != li[e]:
            return False

        s += 1
        e -= 1

    return True


def min_appends(string):
    li = list(string)

    for i in range(len(li)):
        if is_pal(li, i, len(string) - 1):
            return i

    return len(string) - 1


if __name__ == '__main__':
    print min_appends('abede')