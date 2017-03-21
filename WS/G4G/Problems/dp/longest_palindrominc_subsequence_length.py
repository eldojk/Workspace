"""
https://www.youtube.com/watch?v=_nCsPn7_OgI&index=9&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

http://algorithms.tutorialhorizon.com/longest-palindromic-subsequence/ - explanation of substructure and sub problems

	a	g	b	d	b	a
	0	1	2	3	4	5
0	1	1	1	1	3	5
1		1	1	1	3	3
2			1	1	3	3
3				1	1	1
4					1	1
5						1

fill up palindromic subsequences of length 1 first

This one contains, substring, prefix and suffix as erik said

when first and last char is equal, we are computing the middle substring's value:
i.e. s[i] == s[j] -> 2 + s[i+1, j-1]

and prefix and suffix for unequal case:
i.e., s[i] != s[j] -> MAX(s[i, j-1], s[i+1, j])

recurrence =
lps[0, n-1] = 2 + lps[1, n-2] if s[0] == s[n-1]  if last and first char are equal we can add 2 + whatever
in middle
max(lps[0, n-2], lps[1, n-1]) if s[0] != s[1] else 2 cases, ignoring 1st char and last char

"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def longest_palindromic_sub_sequence_length(string):
    len_mtrx = [[0 for i in range(len(string))] for j in range(len(string))]

    # for strings of length 1
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

    print_matrix(len_mtrx)
    return len_mtrx[0][len(string) - 1]


if __name__ == '__main__':
    print longest_palindromic_sub_sequence_length('agbdba')
