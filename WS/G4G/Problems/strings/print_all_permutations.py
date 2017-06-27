"""
amzn

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
Print all combination of given length k possible with characters available in a
given string "S" with repetition

https://careercup.com/question?id=15203851
"""


def print_k_length_combinations(letters, length, current):
    if length == 0:
        print current,
        return

    for i in range(len(letters)):
        new_prefix = current + letters[i]
        print_k_length_combinations(letters, length - 1, new_prefix)

if __name__ == '__main__':
    print ''
    print_k_length_combinations('abc', 2, '')


"""
msft

print all combinations of characters in a string

http://www.mytechinterviews.com/combinations-of-a-string
"""


def print_all_length_combinations(string, index, outer_string):

    for i in range(index, len(string)):

        outer_string.append(string[i])

        print ''.join(outer_string),

        print_all_length_combinations(string, i + 1, outer_string)

        outer_string.pop()


if __name__ == '__main__':
    print ''
    print ''
    print_all_length_combinations('abc', 0, [])


"""
msft

http://qa.geeksforgeeks.org/3895/find-all-unique-combinations
"""


def _print_unique_combinations(array, result, k, index):
    if k > 0:
        for i in range(index, len(array)):
            c = array[i]
            result.append(c)
            _print_unique_combinations(array, result, k - c, i)
            result.pop()

    elif k < 0:
        return

    else:
        print result,


def print_unique_combinations(array, k):
    for i in range(len(array)):
        _print_unique_combinations(array, [array[i]], k - array[i], i)


if __name__ == '__main__':
    print ''
    print ''
    print_unique_combinations([2, 3, 6, 7], 7)
    print ''
    print_unique_combinations([2, 4, 6, 8], 8)