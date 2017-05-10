"""
amzn

http://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/
"""


def print_duplicates(array):
    for i in range(len(array)):

        if array[abs(array[i])] > 0:
            array[abs(array[i])] = -array[abs(array[i])]
        else:
            print abs(array[i]),


if __name__ == '__main__':
    print_duplicates([1, 2, 3, 1, 3, 6, 6])