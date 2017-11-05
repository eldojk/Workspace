"""
amzn

#tricky
http://www.geeksforgeeks.org/generate-unique-partitions-of-an-integer/
"""
from sys import maxint


def generate_partitions(number, curr_max, current_iteration):
    if number == 0:
        return

    # the 2nd check will eliminate duplicates
    if number >= curr_max:
        print number,

        for num in current_iteration:
            print num,

        print ''

    for i in range(1, number):
        curr_max = max(i, curr_max)
        current_iteration.append(i)
        generate_partitions(number - i, curr_max, current_iteration)
        current_iteration.pop()


if __name__ == '__main__':
    generate_partitions(5, -maxint, [])
