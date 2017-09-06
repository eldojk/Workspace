"""
amzn

http://www.geeksforgeeks.org/minimum-number-of-bracket-reversals-needed-to-make-an-expression-balanced/

read comments to understand
"""
from G4G.Problems.stacks.stack import Stack


def get_balanced_stack(string):
    s = Stack()

    for c in string:
        if c == '{' or s.is_empty():
            s.push(c)

        else:
            if s.peek() == '{':
                s.pop()

            else:
                s.push(c)

    return s


def get_open_and_closed_count(s):
    m = 0
    n = 0

    while not s.is_empty():
        c = s.pop()

        if c == '{':
            m += 1

        else:
            n += 1

    return m, n


def ceil(m):
    floor = int(m)

    if floor == m:
        return floor

    return floor + 1


def min_brackets_to_rev(s):
    stack = get_balanced_stack(s)
    m, n = get_open_and_closed_count(stack)

    if (m + n) % 2 != 0:
        return -1

    return ceil(m / 2.0) + ceil(n / 2.0)


if __name__ == '__main__':
    print min_brackets_to_rev('}{')
    print min_brackets_to_rev('{{{')
    print min_brackets_to_rev('{{{{')
    print min_brackets_to_rev('{{{{}}')
    print min_brackets_to_rev('}{{}}{{{')
