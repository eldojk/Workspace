"""
amzn, msft

power O(lgy) time

http://www.geeksforgeeks.org/write-a-c-program-to-calculate-powxn/
"""


def powr(x, y):
    if y == 0:
        return 1

    elif y == 1:
        return x

    elif y % 2 == 0:
        return powr(x, y/2) * powr(x, y/2)

    else:
        return x * powr(x, y/2) * powr(x, y/2)


def power(x, y):
    if y >= 0:
        return powr(x, y)

    else:
        return 1 / float(power(x, -y))


if __name__ == '__main__':
    print power(2, -3)


"""
amzn

http://www.geeksforgeeks.org/multiply-two-numbers-without-using-multiply-division-bitwise-operators-and-no-loops/
To multiply x and y, recursively add x y times.
"""


def multiply(x, y):
    if y == 0:
        return 0

    if y < 0:
        return -multiply(x, -y)

    return x + multiply(x, y - 1)


if __name__ == '__main__':
    print ''
    print multiply(5, -11)


"""
amzn

http://www.geeksforgeeks.org/print-squares-first-n-natural-numbers-without-using/
x2 = (x-1)2 + x + (x - 1)
"""


def get_square(x):
    if x <= 1:
        return x

    return get_square(x - 1) + x + x - 1


def print_squares(n):
    for i in range(1, n + 1):
        print get_square(i),


if __name__ == '__main__':
    print ''
    print_squares(5)