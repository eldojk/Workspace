"""
Longest increasing sub sequence is a non contiguous sub sequence which is in ascending order and of maximum possible
length in an array.
We will consider an lci array, where lci[i] is the longest increasing sub sequence sum with i as the ending element.
Since the longest increasing sub sequence has to end with some element, all we have to do is find the sums with all
possible elements and find the maximum of them
The recurrence is that, lci[i] = lci[j] + 1 if for some j < i, array[j] < array[i] or
                        lci[i] = 1 if no such j exists
"""


def longest_common_sub_sequence_length(array):
    if len(array) <= 1:
        return len(array)

    lci = [1 for element in array]  # initialize with one as 1 is the least possible lci length

    # start from second element
    for i in range(1, len(array)):
        for j in range(i):  # all j such that j < i :)

            if array[j] < array[i] and \
                            lci[i] < lci[j] + 1:  # take the maximum found so far
                lci[i] = max(lci[j] + 1, 1)

    return max(lci)


if __name__ == '__main__':
    print longest_common_sub_sequence_length([10, 22, 9, 33, 21, 50, 41, 60, 80])
