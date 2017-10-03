"""
amzn

http://www.geeksforgeeks.org/check-if-an-array-can-be-divided-into-pairs-whose-sum-is-divisible-by-k/
"""


def count_remainder_freq(array, k):
    freq = [0 for i in range(k)]

    for el in array:
        freq[el % k] += 1

    return freq


def can_be_divided(array, k):
    freq = count_remainder_freq(array, k)

    for el in array:
        rem = el % k

        if 2 * rem == k or rem == 0:
            if freq[rem] % 2 != 0:  # there should be even occurrences
                return False

        elif freq[rem] != freq[k - rem]:
            return False

    return True


if __name__ == '__main__':
    print can_be_divided([9, 7, 5, 3], 6)
    print can_be_divided([92, 75, 65, 48, 45, 35], 10)
    print can_be_divided([91, 74, 66, 48], 10)
