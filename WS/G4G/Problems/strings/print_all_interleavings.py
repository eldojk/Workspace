"""
amzn

http://www.geeksforgeeks.org/print-all-interleavings-of-given-two-strings/
"""


def print_inter_leavings(str1, str2, m, n, li):
    if m == len(str1) and n == len(str2):
        print ''.join(li)

    if m < len(str1):
        li.append(str1[m])
        print_inter_leavings(str1, str2, m + 1, n, li)
        li.pop()

    if n < len(str2):
        li.append(str2[n])
        print_inter_leavings(str1, str2, m, n + 1, li)
        li.pop()

if __name__ == '__main__':
    print_inter_leavings('AB', 'CD', 0, 0, [])