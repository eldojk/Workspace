"""
amzn

#tricky
http://www.geeksforgeeks.org/generate-unique-partitions-of-an-integer/
"""
from sys import maxint


def generate_partitions(number, max_i, current_iteration):
    if number == 0:
        return

    # the 2nd check will eliminate duplicates
    if number >= max_i:
        print number,

        for num in current_iteration:
            print num,

        print ''

    for i in range(1, number):
        max_i = max(i, max_i)
        current_iteration.append(i)
        generate_partitions(number - i, max_i, current_iteration)
        current_iteration.pop()


if __name__ == '__main__':
    generate_partitions(5, -maxint, [])
