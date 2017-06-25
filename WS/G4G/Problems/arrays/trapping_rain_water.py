"""
amzn msft

http://www.geeksforgeeks.org/trapping-rain-water/

An element of array can store water if there are higher bars on left and right.
We can find amount of water to be stored in every element by finding the heights
of bars on left and right sides. The idea is to compute amount of water that can
be stored in every element of array. For example, consider the array {
3, 0, 0, 2, 0, 4}, we can store two units of water at indexes 1 and 2, and one
unit of water at index 2.
"""


def find_total_water(array):
    left = [i for i in array]  # tallest on left including i
    right = [i for i in array]  # tallest on right including i

    water = 0

    for i in range(1, len(array)):
        left[i] = max(left[i - 1], array[i])

    i = len(array) - 2
    while i >= 0:
        right[i] = max(right[i + 1], array[i])
        i -= 1

    for i in range(len(array)):
        water += min(left[i], right[i]) - array[i]

    return water


if __name__ == '__main__':
    print find_total_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])