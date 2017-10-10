"""
msft

http://www.geeksforgeeks.org/multiply-large-numbers-represented-as-strings/

The idea is based on school mathematics.
"""


def copy(array):
    return [i for i in array]


def compute_product(array, num):
    carry = 0
    i = len(array) - 1

    while i >= 0:
        n = array[i]
        prod = carry + (n * num)
        val = prod % 10
        carry = prod // 10

        array[i] = val

        i -= 1

    if carry > 0:
        array = [carry] + array

    return array


def multiply(number, num, pos):
    suffix = [0 for i in xrange(pos)]

    result = compute_product(number, num)
    result += suffix

    return result


def add(array1, array2):
    diff = len(array1) - len(array2)

    if diff > 0:
        array2 = [0 for i in xrange(diff)] + array2

    carry = 0
    i = len(array1) - 1
    while i >= 0:
        sm = array1[i] + array2[i] + carry
        val = sm % 10
        array1[i] = val
        carry = sm // 10

        i -= 1

    if carry > 0:
        array1 = [carry] + array1

    return array1


def multiply_large_numbers(smaller_number, larger_number):
    result = []
    i = len(smaller_number) - 1
    pos = 0

    while i >= 0:
        num = smaller_number[i]
        number = copy(larger_number)
        product = multiply(number, num, pos)
        result = add(product, result)

        pos += 1
        i -= 1

    return result


def multiply_numbers(num1, num2):
    a = num1
    b = num2

    if len(num1) < len(num2):
        a = num2
        b = num1

    a = map(int, list(a))
    b = map(int, list(b))

    result = multiply_large_numbers(b, a)
    result = map(str, result)

    return ''.join(result)


if __name__ == '__main__':
    print multiply_numbers('4154', '51454')
    print multiply_numbers('654154154151454545415415454', '63516561563156316545145146514654')
