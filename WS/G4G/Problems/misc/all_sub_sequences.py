"""
amzn

http://introcs.cs.princeton.edu/java/23recursion/Subsequence.java.html
"""


def print_sub(prefix, remaining, k):
    if k == 0:
        print prefix
        return

    if len(remaining) == 0:
        return

    print_sub(prefix + remaining[0], remaining[1:], k - 1)
    print_sub(prefix, remaining[1:], k)


def print_subs_of_length_k(string, k):
    print_sub('', string, k)


def print_all_sub_sequences(string):
    print string

    i = len(string) - 1
    while i > 0:
        print_subs_of_length_k(string, i)
        i -= 1


if __name__ == '__main__':
    print_all_sub_sequences('abcd')