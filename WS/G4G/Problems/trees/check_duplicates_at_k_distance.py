"""
amzn

http://www.geeksforgeeks.org/check-given-array-contains-duplicate-elements-within-k-distance/
"""


def check_duplicates(array, k):
    dict = {}

    for i in range(len(array)):
        if dict.get(array[i]):
            return True
        else:
            dict[array[i]] = True

        if i - k >= 0:
            dict[array[i - k]] = False

    return False


if __name__ == '__main__':
    print check_duplicates([1, 2, 3, 4, 1, 2, 3, 4], 3)
    print check_duplicates([1, 2, 3, 1, 4, 5], 3)
    print check_duplicates([1, 2, 3, 4, 5], 3)
    print check_duplicates([1, 2, 3, 4, 4], 3)
