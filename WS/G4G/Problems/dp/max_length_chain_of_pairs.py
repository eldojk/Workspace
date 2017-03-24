"""
http://www.geeksforgeeks.org/dynamic-programming-set-20-maximum-length-chain-of-pairs/

{{5, 24}, {15, 28}, {27, 40}, {39, 60}, {50, 90} }
	1		1			2		2			3

"""


def comparator(c1, c2):
    if c1[0] < c2[0]:
        return -1
    elif c1[0] > c2[0]:
        return 1

    return 0


def max_len_chain_of_pairs(pairs):
    pairs.sort(cmp=comparator)
    dp = [1 for pair in pairs]

    for i in range(len(pairs)):
        for j in range(i):

            if pairs[i][0] > pairs[j][1] and \
                            dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    return dp[len(pairs) - 1]


if __name__ == '__main__':
    print max_len_chain_of_pairs([(5, 24), (39, 60), (15, 28), (27, 40), (50, 90)])
