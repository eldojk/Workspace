"""
amzn

http://introcs.cs.princeton.edu/java/23recursion/Subsequence.java.html
"""


def print_sub(arr, string, i, n):
    """
    every character can either be in the sub sequence or
    not be in it.
    so we are including and excluding every char

    :param arr:
    :param string:
    :param i:
    :param n:
    :return:
    """
    if i == n:
        print ''.join(arr)
        return

    arr.append(string[i])
    print_sub(arr, string, i + 1, n)
    arr.pop()

    print_sub(arr, string, i + 1, n)


if __name__ == '__main__':
    print_sub([], 'abcd', 0, 4)
