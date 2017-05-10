"""
amzn

power

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