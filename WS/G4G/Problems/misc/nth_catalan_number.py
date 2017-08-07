"""
amzn

http://www.geeksforgeeks.org/program-nth-catalan-number/

c0 = 1
c(n + 1) = sum ( c(i) * c (n - i) ) for i in range(n + 1)
"""


def nth_catalan_number(n):
    if n <= 1:
        return 1

    cat = [0 for i in range(n + 1)]

    cat[0] = cat[1] = 1

    for i in range(2, n + 1):
        for j in range(i):
            cat[i] += (cat[j] * cat[i - j - 1])

    return cat[n]


if __name__ == '__main__':
    print nth_catalan_number(6)
