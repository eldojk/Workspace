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

    temp = power(x, y / 2)
    if y % 2 == 0:
        return temp * temp

    else:
        return x * temp * temp


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


"""
msft

convert to binary
"""


def binary_repr(num, arr):
    if num > 1:
        binary_repr(num // 2, arr)

    arr.append(num % 2)
    return arr


if __name__ == '__main__':
    print ''
    print ''
    print 'binary repr'
    print binary_repr(8, [])


"""
msft

https://www.careercup.com/question?id=11903257
"""


def is_multiple_of_n(number, multiple):
    number = map(int, number)
    rem = number[0] % multiple

    for i in range(1, len(number)):
        num = number[i]
        rem = (rem * 10 + num) % multiple  # for binary use 2 here instead of 10

    return rem == 0


if __name__ == '__main__':
    print ''
    print 'is divisible'
    print is_multiple_of_n('1281', 3)


"""
msft
validate ip address

http://www.geeksforgeeks.org/program-to-validate-an-ip-address/
"""


def is_valid_ip(string):
    arr = string.split('.')

    if len(arr) != 4:
        return False  # ip should have four terms

    for s in arr:
        i = int(s)
        if i > 255 or i < 0:  # numbers should be in range(0, 256)
            return False

    return True


if __name__ == '__main__':
    print ''
    print 'is valid ip address'
    print is_valid_ip('128.0.0.1')
    print is_valid_ip('125.16.100.1')
    print is_valid_ip('125.512.100.1')
    print is_valid_ip('125.512.100.abc')