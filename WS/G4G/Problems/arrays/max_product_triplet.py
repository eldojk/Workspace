"""
amzn

http://www.geeksforgeeks.org/find-maximum-product-of-a-triplet-in-array/


Scan the array and compute Maximum, second maximum and third maximum element present in the array.
Scan the array and compute Minimum and second minimum element present in the array.
Return the maximum of product of Maximum, second maximum and third maximum and product of Minimum, second minimum and
Maximum element. (the second case is to consider negatives)
"""
from sys import maxint


def compute_max_product_triplet(array):
    n = len(array)

    if n < 3:
        return None

    max_a = max_b = max_c = -maxint
    min_a = min_b = maxint

    for num in array:

        if num > max_a:
            max_c = max_b
            max_b = max_a
            max_a = num

        elif num > max_b:
            max_c = max_b
            max_b = num

        elif num > max_c:
            max_c = num

        if num < min_a:
            min_b = min_a
            min_a = num

        elif num < min_b:
            min_b = min_a

    return max(
        (max_a * max_b * max_c),
        (min_a * min_b * max_a)
    )


if __name__ == '__main__':
    print compute_max_product_triplet([1, -4, 3, -6, 7, 0])