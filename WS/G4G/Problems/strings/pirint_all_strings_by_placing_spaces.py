"""
amzn

http://www.geeksforgeeks.org/print-possible-strings-can-made-placing-spaces/
"""


def print_pattern(string, prefix, i, n):
    if i == n:
        print prefix
        return

    ch = string[i]

    # join without space
    print_pattern(string, prefix + ch, i + 1, n)

    # join with space
    print_pattern(string, prefix + ' ' + ch, i + 1, n)


def print_all_patterns(string):
    print_pattern(string, string[0], 1, len(string))


if __name__ == '__main__':
    print_all_patterns('ABCD')