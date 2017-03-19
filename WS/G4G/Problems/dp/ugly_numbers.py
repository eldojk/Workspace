"""
http://www.geeksforgeeks.org/ugly-numbers/
"""


def print_ugly_numbers(num):
    ugly = [1]

    i2 = 0
    i3 = 0
    i5 = 0

    # Because ugly numbers are multiples of 2, 3, and 5 only
    # we are taking such multiples in order
    # we are multiplying 2, 3, and 5 with present ugly numbers in
    # ascending order
    n2 = ugly[i2]*2
    n3 = ugly[i3]*3
    n5 = ugly[i5]*5

    while True:
        next_ugly_num = min(n2, n3, n5)

        if next_ugly_num > num:
            break

        ugly.append(next_ugly_num)

        if next_ugly_num == n2:
            i2 += 1
            n2 = ugly[i2] * 2

        if next_ugly_num == n3:
            i3 += 1
            n3 = ugly[i3] * 3

        if next_ugly_num == n5:
            i5 += 1
            n5 = ugly[i5] * 5

    print ugly


if __name__ == '__main__':
    print_ugly_numbers(150)