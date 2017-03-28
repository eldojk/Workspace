"""
http://www.geeksforgeeks.org/amazon-interview-experience-set-331-1-year-experienced-se-1/

last pattern question
"""


def print_bars(num):
    for i in range(num):
        print '-',

    print ''


def print_recur(num):
    if num <= 0:
        return

    print_recur(num - 1)
    print_bars(num)
    print_recur(num - 1)


def print_custom(num):
    print_bars(num)
    print_recur(num - 1)
    print_bars(num)


if __name__ == '__main__':
    print_custom(5)