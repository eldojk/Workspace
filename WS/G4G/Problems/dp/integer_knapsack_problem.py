"""
https://www.youtube.com/watch?v=8LusJS5-AGo&index=1&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

For each weight, value is the MAX of either:
adding wt : -> value[i] + value_arr[current_wt - weight[i]]
or not adding wt -> value_arr[i]
"""


def best_knapsack_value(values, weights, max_wt):
    value_arr = [0] + [0 for i in range(max_wt)]

    for curr_wt in range(len(value_arr)):
        for i in range(len(weights)):
            if weights[i] <= curr_wt:
                value_arr[curr_wt] = max(values[i] + value_arr[curr_wt - weights[i]], value_arr[i])

    return value_arr[max_wt]
