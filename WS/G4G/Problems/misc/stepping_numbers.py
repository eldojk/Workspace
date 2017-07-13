# coding=utf-8
"""
http://www.geeksforgeeks.org/stepping-numbers/

Given two integers ‘n’ and ‘m’, find all the stepping numbers in range [n, m]. A
number is called stepping number if all
adjacent digits have an absolute difference of 1. 321 is a Stepping Number while 421 is not.

Examples:

Input : n = 0, m = 21
Output : 0 1 2 3 4 5 6 7 8 9 10 12 21

Input : n = 10, m = 15
Output : 10, 12
"""


def get_numbers_with_this_prefix(num):
    last_digit = num % 10
    nums = []

    if last_digit != 0:
        k = last_digit - 1
        stepping_num = (num * 10) + k
        nums.append(stepping_num)

    if last_digit != 9:
        k = last_digit + 1
        stepping_num = (num * 10) + k
        nums.append(stepping_num)

    return nums


def stepping_numbers(n):
    if n <= 9:
        print range(10)

    nums = range(10)
    i = 1
    finished = False

    while not finished:
        curr_num = nums[i]
        next_nums = get_numbers_with_this_prefix(curr_num)

        for num in next_nums:
            if num > n:
                finished = True
                break

            nums.append(num)

        i += 1

    return nums


if __name__ == '__main__':
    print stepping_numbers(144)
