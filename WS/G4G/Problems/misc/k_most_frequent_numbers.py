"""
amzn

http://www.geeksforgeeks.org/find-k-numbers-occurrences-given-array/

Given an array of n numbers and a positive integer k. The problem is to find k numbers with most occurrences, i.e., the
top k numbers having the maximum frequency. If two numbers have same frequency then the larger number should be given
preference. The numbers should be displayed in decreasing order of their frequencies. It is assumed that the array
consists of k numbers with most occurrences.
"""


def cmprtr(n1, n2):
    f1 = n1[1]
    f2 = n2[1]

    if f1 < f2:
        return -1

    elif f1 > f2:
        return 1

    else:
        v1 = n1[0]
        v2 = n2[0]

        if v1 < v2:
            return -1

        elif v1 > v2:
            return 1

        else:
            return 0


def get_count_map(array):
    hm = {}
    for el in array:
        if el in hm:
            hm[el] += 1

        else:
            hm[el] = 1

    return hm


def get_tuples(hm):
    result = []
    for k in hm.keys():
        result.append((k, hm[k]))

    return result


def print_k_most_frequent(array, k):
    hm = get_count_map(array)

    result_array = get_tuples(hm)

    result_array.sort(cmp=cmprtr, reverse=True)

    i = 0
    while i < k:
        if i == len(result_array):
            break

        print result_array[i][0],
        i += 1


if __name__ == '__main__':
    print_k_most_frequent([3, 1, 4, 4, 5, 2, 6, 1], 2)
    print ''
    print_k_most_frequent([7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], 4)