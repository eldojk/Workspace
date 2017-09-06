"""
amzn

Print all permutations of a string

(more down)

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
amzn

Print all combination of given length k possible with characters available in a
given string "S" with repetition

https://careercup.com/question?id=15203851
http://www.geeksforgeeks.org/print-all-combinations-of-given-length/
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


"""
amzn

http://www.geeksforgeeks.org/generate-palindromic-numbers-less-n/

We start from 1 and create palindromes of odd digit and even digits up to n.
For every number (starting from 1), we append its reverse at end if we need even
length palindrome numbers. For odd length palindrome, we append reverse of all digits
except last one
"""


def get_palindromic_number(n, is_odd):
    p = n

    if is_odd:
        n /= 10

    while n > 0:
        p = p * 10 + (n % 10)
        n /= 10

    return p


def print_pals_less_than_n(n):
    k = 2
    while k > 0:

        i = 1
        while True:
            pal = get_palindromic_number(i, k % 2 == 0)

            if pal >= n:
                break

            print pal,
            i += 1

        k -= 1


if __name__ == '__main__':
    print ''
    print ''
    print 'print pals less than n'
    print_pals_less_than_n(250)


"""
amzn

https://stackoverflow.com/questions/12667551/permutations-with-duplicates
http://www.geeksforgeeks.org/print-all-permutations-of-a-string-with-duplicates-allowed-in-input-string/
"""


def permute_wo_dupes(string, prefix):
    if len(string) == 0:
        print ''.join(prefix),

    else:
        for i in range(len(string)):
            if i > 0:
                if string[i] == string[i - 1]:
                    continue

            permute_wo_dupes(string[0: i] + string[i + 1: len(string)], prefix + [string[i]])


def print_permutations_without_duplicates(string):
    s = list(string)
    p = []
    s.sort()
    permute_wo_dupes(s, p)


if __name__ == '__main__':
    print ''
    print ''
    print 'permute wo dupes'
    print_permutations_without_duplicates('asdaa')