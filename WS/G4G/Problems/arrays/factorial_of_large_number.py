"""
msft

http://www.geeksforgeeks.org/factorial-large-number/
"""


def multiply(array, x, n):
    carry = 0

    for i in range(n):
        result = array[i] * x + carry

        last_digit = result % 10
        carry = result // 10

        array[i] = last_digit

    while carry > 0:
        digit = carry % 10
        carry //= 10
        array[n] = digit
        n += 1

    return n


def to_string(array, size):
    res = []
    i = 0

    while size > 0:
        res.append(str(array[i]))
        i += 1
        size -= 1

    res.reverse()
    return ''.join(res)


def factorial(n):
    array = [0 for j in range(300)]
    array[0] = 1
    size = 1

    for i in range(2, n + 1):
        size = multiply(array, i, size)

    return to_string(array, size)


if __name__ == '__main__':
    print factorial(100)