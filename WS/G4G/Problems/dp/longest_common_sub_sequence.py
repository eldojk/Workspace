"""
Length of LCS of array1[i, j] and array2[i, k] is abc lets say,
then if we add the next character (say 'd') to array2 (i.e. array2[1, k+1],
Now the LCS will be if 'd' occurs after the last previous common char
LCS of abcd , ac = 2 ->
we arrive by first looking from beggining
LCS(a, a) = 1
LCS(ab, a) = 1
LCS(abc, a) = 1
LCS(abcd, a) = 1 # first iteration over
LCS(a, ac) = 1
LCS(ab, ac) = 1
LCS(abc, ac) = 2
LCS(abcd, ac) = 2
"""


def lcs_length(array1, array2):
    lcs_len = [0 for i in range(len(array1))]

    for i in range(len(array2)):
        for j in range(len(array1)):
            c2 = array2[i]
            c1 = array1[j]

            if c2 == c1:
                if lcs_len[j] < j + 1:
                    lcs_len[j] += 1
            else:
                if j > 0 and lcs_len[j - 1]:
                    lcs_len[j] = lcs_len[j - 1]

    return lcs_len[len(array1) - 1]
