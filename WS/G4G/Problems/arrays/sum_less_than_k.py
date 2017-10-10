"""
amzn

http://www.geeksforgeeks.org/count-pairs-array-whose-sum-less-x/
http://www.geeksforgeeks.org/count-triplets-with-sum-smaller-that-a-given-value/
"""


def pair_sum_less_than_k(array, k):
    i = 0
    j = len(array) - 1
    count = 0

    while i < j:
        if array[i] + array[j] < k:
            count += (j - i)
            i += 1

        else:
            j -= 1

    return count


def triplet_with_sum_less_than_num(array, num):
    i = 0
    n = len(array)
    count = 0

    while i < n - 2:
        j = i + 1
        k = n - 1

        while j < k:
            if array[i] + array[j] + array[k] >= num:
                k -= 1
            else:
                count += (k - j)
                j += 1

        i += 1

    return count


if __name__ == '__main__':
    print triplet_with_sum_less_than_num([-2, 0, 1, 3], 2)
    print triplet_with_sum_less_than_num([1, 3, 4, 5, 7], 12)

