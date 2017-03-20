"""

TUSHAR: https://www.youtube.com/watch?v=We3YDTzNXEk&index=8&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr
The first row and column represent the min number of ops to convert '' (null) to abcdef or azcde

		a	b	c	d	e	f
	0	1	2	3	4	5	6
a	1	0	1	2	3	4	5
z	2	1	1	X	3	4	5
c	3	2	2	1	2	3	4
e	4	3	3	2	2	2	3
d	5	4	4	3	2	3	3

Look at position x to know how to figure this out:

at x -> we are trying to convert abc to az: coordinates = (2, 3)

since z not equal to c:
    we look at 3 possiblities:

    1. (1, 3) -> abc to a can be done in 2 ops, so we can add 'z' after this. Hence 3 ops
    2. (2, 1) -> ab to a can be done in 1 ops, hence adding 'z' gives 1+1 = 2
    3. (2, 2) -> ab to az can be done in 1  ops, hence abc to az should take only 1 more as we have to delete only one (the c)
    char

    Hence we use the minimum of these three ops to proceed
    X = 2
"""


def print_matrix(m):
    for row in m:
        print ' '.join(map(str, row))


def edit_distance(str1, str2):
    min_ops = [[0 for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]

    for i in range(1, len(str1) + 1):
        min_ops[0][i] = i

    for j in range(1, len(str2) + 1):
        min_ops[j][0] = j

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):

            if str1[j - 1] == str2[i - 1]:  # strings are equal. no need of editing
                min_ops[i][j] = min_ops[i - 1][j - 1]
            else:
                # abc to az considering c and z
                min_ops[i][j] = 1 + min(min_ops[i - 1][j],  # delete c + ab to az
                                        min_ops[i - 1][j - 1], # ab to a and change c to z
                                        min_ops[i][j - 1])  # abc to a + add z

    return min_ops[len(str2)][len(str1)]


if __name__ == '__main__':
    print edit_distance('sunday', 'saturday')
