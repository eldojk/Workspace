"""
Longest increasing sub sequence is a non contiguous sub sequence which is in ascending order and of maximum possible
length in an array.
We will consider an lci array, where lci[i] is the longest increasing sub sequence sum with i as the ending element.
Since the longest increasing sub sequence has to end with some element, all we have to do is find the sums with all
possible elements and find the maximum of them
The recurrence is that, to find lci[i] can be computed by adding the ith element to any lci sequences from 0 to i-1 if
array[i] is larger than largest element in any of these lcis. Adding array[i] to an increasing sub sequence will not
break the increasing order if array[i[ is greater than the last element of the sequence
"""


def longest_common_sub_sequence_length(array):
    if len(array) <= 1:
        return len(array)

    lci = [1 for element in array]  # initialize with one as 1 is the least possible lci length

    for i in range(1, len(array)):
        for j in range(i):
            if array[j] < array[i]:
                lci[i] = max(lci[j] + 1, lci[i])

    return max(lci)
