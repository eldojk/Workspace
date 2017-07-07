"""
amzn

http://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/

Given two strings string1 and string2, find the smallest substring in string1
containing all characters of string2 efficiently.
For Example:

Input :  string = "this is a test string"
         pattern = "tist"
Output :  Minimum window is "t stri"
Explanation: "t stri" contains all the characters
              of pattern.

Input :  string = "geeksforgeeks"
         pattern = "ork"
Output :  Minimum window is "ksfor"
"""


from sys import maxint


def get_char_counts(string):
    counts = [0 for i in range(256)]

    for c in string:
        idx = ord(c)
        counts[idx] += 1

    return counts


def is_counts_satisfied(required, actual):
    for i in xrange(256):
        if actual[i] < required[i]:
            return False

    return True


def find_min_window(string1, string2):
    if len(string2) > len(string1):
        return 'Not Possible'

    if len(string2) == 0:
        return ''

    required_count = get_char_counts(string2)
    min_size = maxint
    min_i = 0
    min_j = 0
    actual_count = [0 for i in range(256)]

    start = 0
    end = -1

    while end < len(string1) - 1:

        if not is_counts_satisfied(required_count, actual_count):
            end += 1
            char = string1[end]
            idx = ord(char)
            actual_count[idx] += 1

        else:
            size = end - start + 1
            if size < min_size:
                min_size = size
                min_i = start
                min_j = end

            start += 1
            char = string1[start - 1]
            idx = ord(char)
            actual_count[idx] -= 1

    char = string1[end]
    idx = ord(char)
    actual_count[idx] += 1

    if is_counts_satisfied(required_count, actual_count):
        size = end - start + 1
        if size < min_size:
            min_size = size
            min_i = start
            min_j = end

    if min_size == maxint:
        return 'Not possible'

    return string1[min_i: (min_j + 1)]


if __name__ == '__main__':
    print find_min_window('this is a test string', 'tist')
    print find_min_window('geeksforgeek', 'ork')
