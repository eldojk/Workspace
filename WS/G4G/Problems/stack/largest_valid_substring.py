"""
Given a string of only brackets, find the largest valid substring

In string while getting '(', push index to the stack.
If ')' is encountered, pop once
A valid substring is between the last popped index and its corresponding ')'
match. The difference between this last popped index and its corresponding ')'
is its length. Keep track of this length and thereby get the largest valid
substring
"""
from G4G.Problems.stack.stack import Stack


def largest_valid_substring(string):
    stack = Stack()

    l_index = None
    r_index = None

    min_index = None
    max_index = None

    max_diff = 0

    for i in range(len(string)):
        if string[i] == '(':
            stack.push(i)
        elif string[i] == ')':
            try:
                l_index = stack.pop()
                r_index = i
            except Exception:
                pass

        if None not in [l_index, r_index]:
            diff = r_index - l_index
            if diff > max_diff:
                max_diff = diff
                min_index = l_index
                max_index = r_index

    if None in [l_index, r_index]:
        return None
    else:
        return string[min_index: max_index + 1]
