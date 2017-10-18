"""
amzn msft

http://www.geeksforgeeks.org/anagram-substring-search-search-permutations/

keep a sliding window of len(needle) size along the haystack and at every move
check if the sliding window values are equal
"""


def compute_char_count(string, i, j):
    cc = [0 for i in range(26)]

    while i <= j:
        c = string[i]
        idx = ord(c) - ord('a')
        cc[idx] += 1

    return cc


def is_char_count_same(cc1, cc2):
    for i in xrange(26):
        if cc1[i] != cc2[i]:
            return False

    return True


def anagram_sub_string_search(haystack, needle):
    i = 0
    j = len(needle) - 1
    ccn = compute_char_count(needle, i, j)
    cch = compute_char_count(haystack, i, j)
    n = len(haystack)

    while True:

        if is_char_count_same(ccn, cch):
            print i,

        i += 1
        j += 1

        if j >= n:
            break

        idx_to_remove = ord(haystack[i - 1]) - ord('a')
        idx_to_add = ord(haystack[j]) - ord('a')

        cch[idx_to_remove] -= 1
        cch[idx_to_add] += 1


if __name__ == '__main__':
    anagram_sub_string_search('bacdgabcda', 'abcd')
