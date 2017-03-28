"""
Print all permutations of a string

http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
"""


def _permute(str_list, left, right):
    if left == right:
        print "".join(str_list),
    else:
        for i in range(left, right + 1):
            str_list[left], str_list[i] = str_list[i], str_list[left]
            _permute(str_list, left + 1, right)
            str_list[left], str_list[i] = str_list[i], str_list[left]


def permute(string):
    st_list = list(string)
    _permute(st_list, 0, len(st_list) - 1)

if __name__ == '__main__':
    permute('abc')
    print ''


"""
Print all combination of given length k possible with characters available in a given string "S" with repetition

https://careercup.com/question?id=15203851
"""


def print_k_length_combinations(letters, length, prefix):
    if length == 0:
        print prefix,
        return

    for i in range(len(letters)):
        new_prefix = prefix + letters[i]
        print_k_length_combinations(letters, length - 1, new_prefix)

if __name__ == '__main__':
    print ''
    print_k_length_combinations('abc', 2, '')
