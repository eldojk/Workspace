"""
http://www.geeksforgeeks.org/find-four-elements-a-b-c-and-d-in-an-array-such-that-ab-cd/

Using hash table
"""


def get_pairs_with_equal_sum(array):
    sum_dict = {}

    for i in range(len(array)):
        for j in range(i, len(array)):
            num1 = array[i]
            num2 = array[j]
            _sum = num1 + num2

            if sum_dict.get(_sum):
                pairs = [(num1, num2)]
                pairs.append(sum_dict[_sum])
                return pairs
            else:
                sum_dict[_sum] = (num1, num2)

    return None

# print get_pairs_with_equal_sum([3, 4, 7, 1, 2, 9, 8])
# print get_pairs_with_equal_sum([3, 4, 7, 1, 12, 9])
# print get_pairs_with_equal_sum([65, 30, 7, 90, 1, 9, 8])
