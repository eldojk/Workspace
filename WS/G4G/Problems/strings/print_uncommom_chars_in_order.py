"""
amzn

in O(n)

http://www.geeksforgeeks.org/find-uncommon-characters-two-strings/

can be done with single array, use int array instead of boolean and keep counts
1 - for only one array occurence
2 - for both
0 - none
make sure not to increment multiple times for already occurring chars
"""


def hash_key(c):
    return ord(c) - ord('a')


def ascii(i):
    return i + ord('a')


def fill_char_presence(s, array):
    for c in s:
        array[hash_key(c)] = True


def print_uncommon(s1, s2):
    if s1 is None or s2 is None:
        return

    arr1 = [False for i in xrange(26)]
    arr2 = [False for i in xrange(26)]
    fill_char_presence(s1, arr1)
    fill_char_presence(s2, arr2)

    for i in xrange(26):
        if arr1[i] and arr2[i]:
            continue

        elif arr1[i] or arr2[i]:
            print chr(ascii(i)),


if __name__ == '__main__':
    print_uncommon('characters', 'alphabets')
    print ''
    print_uncommon('geeksforgeeks', 'geeksquiz')
