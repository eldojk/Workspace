"""
amzn

this solution takes extra space
http://www.geeksforgeeks.org/find-nth-magic-number/

todo this is wrong
"""


def nth_magic_number(n):
    nums = [0 for i in xrange(n)]
    nums[0] = 5
    pw = 2
    i = 0
    k = 1
    curr = pow(5, 1)

    while k < n:

        if i < k - 1:
            nums[k] = curr + nums[i]
            i += 1
            k += 1

        else:
            pw += 1
            curr = pow(curr, pw)
            nums[k] = curr
            k += 1
            i = 0

    print nums
    return nums[n - 1]


if __name__ == '__main__':
    print nth_magic_number(3)
    print nth_magic_number(15)
