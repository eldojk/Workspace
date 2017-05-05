"""
amzn

http://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence/

This problem is recursive and can be broken in sub-problems. We start from end of the given digit sequence. We
initialize the total count of decodings as 0. We recur for two subproblems.
1) If the last digit is non-zero, recur for remaining (n-1) digits and add the result to total count.
2) If the last two digits form a valid character (or smaller than 27), recur for remaining (n-2) digits and add the
result to total count.
"""


def num_decodings(string, n):
    if n == 0 or n == 1:
        return 1

    count = 0

    if int(string[n - 1]) > 0:
        count += num_decodings(string, n - 1)
    if 0 < int(string[n - 2:n]) < 27:
        count += num_decodings(string, n - 2)

    return count


if __name__ == '__main__':
    print num_decodings('1234', 4)


"""
DYNAMIC PROGRAMMING
"""


def num_decodings_dp(string):
    decodings = [0 for i in range(len(string) + 1)]
    decodings[0] = 1
    decodings[1] = 1

    for i in range(2, len(string) + 1):

        if int(string[i - 1]) > 0:
            decodings[i] += decodings[i - 1]

        if 0 < int(string[i - 2:i]) < 27:
            decodings[i] += decodings[i - 2]

    return decodings[len(string)]


if __name__ == '__main__':
    print ''
    print num_decodings_dp('1234')
