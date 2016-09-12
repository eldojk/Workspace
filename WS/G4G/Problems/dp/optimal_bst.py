"""
Given a sorted array keys[0.. n-1] of search keys and an array freq[0.. n-1] of frequency counts, where freq[i] is the
number of searches to keys[i]. Construct a binary search tree of all keys such that the total cost of all the searches
is as small as possible.

Assuming there are n elements the root can be decided as k where k in range(i, j). So if a was root, cost a searching
cost(1, k) + 1*freq(k) + cost(k+1, j). -> Minimise k such that this is met. This is similar to parenthesization problem
(or matrix chain multiplication). Instead of decided where to parenthesize we decide where to choose the root

Similar to matrix multiplication we consider one matrix at first, set of 2 the second time, 3 the next time and so on

TUSHAR: https://www.youtube.com/watch?v=hgA4xxlVvfQ&index=7&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr
"""


def get_cost(cost_arr, k, i, j):
    if k == i:
        return cost_arr[i + 1][j]
    elif k == j:
        return cost_arr[i][j - 1]
    else:
        return cost_arr[i][k - 1] + cost_arr[k + 1][j]


def get_minimum_cost(keys, freqs):
    cost = [[0 for i in range(len(keys))] for j in range(len(keys))]

    # trees containing only one node
    for i in range(len(keys)):
        cost[i][i] = freqs[i]

    max_index = len(keys) - 1
    for l in range(1, len(keys)):
        for i in range(len(keys)):
            j = i + l
            if j <= max_index:
                cost[i][j] = sum(freqs[i:j + 1]) + min([get_cost(cost, k, i, j) for k in range(i, j + 1)])

    print cost[0][max_index]
