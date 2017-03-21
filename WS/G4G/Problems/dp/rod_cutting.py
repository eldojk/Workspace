"""
Given a rod of length and prices at which different length of this rod can sell, how do you cut this rod to
maximize profit

TUSHAR: https://www.youtube.com/watch?v=IRwVmTmN6go&index=12&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

dp[n] = max(price[i] + dp[n - i]) for all i in sell-able rod lengths if i <= n

length   | 1   2   3   4
-------------------------
price    | 1   5   8   9

n = 10

0	1	2 	3	4	5
0	1	5	8	10	13

"""


def maximum_profit(rods, profits, length):
    max_values = [0 for i in range(length + 1)]

    # starting at max len is 1
    for i in range(1, len(max_values)):

        # for every possible rod cuttings
        for j in range(len(rods)):

            len_rod = rods[j]
            profit_rod = profits[j]

            # check if the length can be used
            if len_rod <= i:
                result = profit_rod + max_values[i - len_rod]

                # update as an when we find a higher value
                if result > max_values[i]:
                    max_values[i] = result

    return max_values[length]


if __name__ == '__main__':
    print maximum_profit([1, 2, 3, 4, 5, 6, 7, 8], [1, 5, 8, 9, 10, 17, 17, 20], 8)
