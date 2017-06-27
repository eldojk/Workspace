# coding=utf-8
"""
amzn msft

http://www.geeksforgeeks.org/find-next-greater-number-set-digits/

Following are few observations about the next greater number.
1) If all digits sorted in descending order, then output is always “Not Possible”. For example, 4321.
2) If all digits are sorted in ascending order, then we need to swap last two digits. For example, 1234.
3) For other cases, we need to process the number from rightmost side (why? because we need to find the smallest of all
greater numbers)

You can now try developing an algorithm yourself.

Following is the algorithm for finding the next greater number.
I) Traverse the given number from rightmost digit, keep traversing till you find a digit which is smaller than the
previously traversed digit. For example, if the input number is “534976”, we stop at 4 because 4 is smaller than next
digit 9. If we do not find such a digit, then output is “Not Possible”.

II) Now search the right side of above found digit ‘d’ for the smallest digit greater than ‘d’. For “534976″, the right
side of 4 contains “976”. The smallest digit greater than 4 is 6.

III) Swap the above found two digits, we get 536974 in above example.

IV) Now sort all digits from position next to ‘d’ to the end of number. The number that we get after sorting is the
output. For above example, we sort digits in bold 536974. We get “536479” which is the next greater number for input
534976.
"""
from sys import maxint


def get_nxt_digit(digit):
    s = map(int, list(digit))

    i = len(s) - 1
    while i > 0:
        if s[i] > s[i - 1]:
            break

        i -= 1

    if i == 0:
        print 'Not possible'
        return

    num = s[i - 1]
    greater_num = maxint
    greater_i = None

    for k in range(i, len(s)):
        val = s[k]
        if num < val < greater_num:
            greater_num = val
            greater_i = k

    s[i - 1], s[greater_i] = s[greater_i], s[i - 1]

    prefix = s[:i]
    suffix = s[i:]
    suffix.sort()

    final = prefix + suffix

    print ''.join(map(str, final))


if __name__ == '__main__':
    get_nxt_digit('534976')
    get_nxt_digit('98765')

