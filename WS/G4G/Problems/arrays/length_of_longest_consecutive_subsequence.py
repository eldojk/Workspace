"""
http://www.geeksforgeeks.org/longest-consecutive-subsequence/
"""


def len_of_longest_consecutive_sub_sequence(array):
    hm = {i: True for i in array}

    longest_len = 0
    for element in array:
        # see if element - 1 is present,
        # if yes, then element can't be the start of a consecutive sub sequence
        if hm.get(element - 1):
            continue

        # other wise start checking for a consecutive sub sequence with element as the
        # starting element
        current_len = 1
        while True:
            element += 1
            if hm.get(element):
                current_len += 1
            else:
                break

        longest_len = max(longest_len, current_len)

    print longest_len


if __name__ == '__main__':
    len_of_longest_consecutive_sub_sequence([1, 9, 3, 10, 4, 20, 2])
    len_of_longest_consecutive_sub_sequence([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42])
