"""
https://www.youtube.com/watch?v=_nCsPn7_OgI&index=9&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr
"""


def longest_palindromic_sub_sequence_length(string):
    len_mtrx = [[0 for i in range(len(string))] for j in range(len(string))]

    for i in range(len(string)):
        len_mtrx[i][i] = 1

    max_index = len(string) - 1
    for l in range(1, len(string)):
        for i in range(len(string)):
            j = i + l

            if j <= max_index:
                if string[i] == string[j]:
                    len_mtrx[i][j] = 2 + len_mtrx[i + 1][j - 1]
                else:
                    len_mtrx[i][j] = max(len_mtrx[i][j - 1], len_mtrx[i + 1][j])

    return len_mtrx[0][len(string) - 1]
