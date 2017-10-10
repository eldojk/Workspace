"""
amzn

#tricky
here we are doing all possible swaps and figuring out the maximum
(backtracking)
http://www.geeksforgeeks.org/find-maximum-number-possible-by-doing-at-most-k-swaps/
"""


from sys import maxint


MAX = -maxint


def swap(i, j, num):
    tmp = num[i]
    num[i] = num[j]
    num[j] = tmp


def find_max(num, k):
    global MAX

    if k == 0:
        return

    n = len(num)

    for i in range(n - 1):
        for j in range(i + 1, n):

            if int(num[i]) < int(num[j]):
                swap(i, j, num)

                if int(''.join(num)) > MAX:
                    MAX = int(''.join(num))

                find_max(num, k - 1)

                swap(i, j, num)


def find_maximum(num, k):
    global MAX
    MAX = -maxint
    find_max(list(str(num)), k)
    return MAX


if __name__ == '__main__':
    print find_maximum(129814999, 4)
