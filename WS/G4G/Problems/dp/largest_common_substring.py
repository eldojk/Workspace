"""
http://algorithms.tutorialhorizon.com/dynamic-programming-longest-common-substring/#attachment_1507

Largest common substring
"""


def largest_common_substring(str1, str2):
    lcs_arr = [0] + [0 for i in range(len(str1))]

    for i in range(len(str2)):
        for j in range(len(str1)):
            c2 = str2[i]
            c1 = str1[j]

            if c1 == c2:
                lcs_arr[j + 1] = lcs_arr[j] + 1

    return max(lcs_arr)
