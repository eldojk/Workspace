"""
amzn

http://www.geeksforgeeks.org/count-ways-reach-nth-stair/

A child running up a staircase with n steps can hop either 1 step, 2 steps or 3 steps. How many possible ways can the
child run up n stairs

CTCI 9.1 #316
"""


def get_possible_steps(n):
    steps = [0 for i in range(n + 1)]
    steps[0] = 1
    steps[1] = 1
    steps[2] = 2
    steps[3] = 4

    if n <= 3:
        return steps[n]

    for i in range(4, n + 1):
        steps[i] = steps[i - 1] + steps[i - 2] + steps[i - 3]

    return steps[n]
