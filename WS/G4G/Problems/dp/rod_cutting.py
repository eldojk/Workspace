"""
Given a rod of length and prices at which different length of this rod can sell, how do you cut this rod to
maximize profit

TUSHAR: https://www.youtube.com/watch?v=IRwVmTmN6go&index=12&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr
"""


def maximum_profit(rods, profits, length):
    max_values = [0 for i in range(length + 1)]

    for i in range(len(rods)):
        for j in range(1, length + 1):
            val = profits[i]
            rod_len = rods[i]
            curr_len = j

            if rod_len <= curr_len:
                max_values[j] = max(val + max_values[j - rod_len], max_values[j])

    return max_values[length]
