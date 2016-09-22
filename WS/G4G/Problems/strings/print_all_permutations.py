"""
Print all permutations of a string

http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
"""


def _permute(string, left, right):
    if left == right:
        print "".join(string)
    else:
        for i in range(left, right + 1):
            string[left], string[i] = string[i], string[left]
            _permute(string, left + 1, right)
            string[left], string[i] = string[i], string[left]


def permute(string):
    st_list = list(string)
    _permute(st_list, 0, len(st_list) - 1)

# print permute('abc')
