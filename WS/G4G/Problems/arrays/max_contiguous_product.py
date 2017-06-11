"""
amzn, msft

http://www.geeksforgeeks.org/maximum-product-subarray/

keep track of max product and min product at every pos
so as to compute the next num
"""
from sys import maxint


def max_product_sub_array(array):
    min_product = [array[0] for i in array]
    max_product = [array[0] for i in array]

    max_val = -maxint

    # these cases take care of everything
    # can also optimise for o(1) space. store only last product values
    # instead of array of values
    for i in range(1, len(array)):
        max_product[i] = max(
            max_product[i - 1] * array[i],
            min_product[i - 1] * array[i],
            array[i]
        )

        min_product[i] = min(
            min_product[i - 1] * array[i],
            max_product[i - 1] * array[i],
            array[i]
        )

        if max_product[i] > max_val:
            max_val = max_product[i]

    return max_val


if __name__ == '__main__':
    print max_product_sub_array([6, -3, -10, 0, 2])
    print max_product_sub_array([-1, -3, -10, 0, 60])
    print max_product_sub_array([-2, -3, 0, -2, -40])