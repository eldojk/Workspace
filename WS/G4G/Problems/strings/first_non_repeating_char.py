"""
amzn

http://www.geeksforgeeks.org/given-a-string-find-its-first-non-repeating-character/
also check find_non_repeating_char_in_stream.py
"""


def find_non_repeating_first_char(string):
    di = {}

    for c in string:
        if di.get(c) is None:
            di[c] = 1
        else:
            di[c] += 1

    for c in string:
        if di[c] == 1:
            return c

    return None


if __name__ == '__main__':
    print find_non_repeating_first_char('geeksforgeeks')
