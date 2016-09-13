"""
Given two strings find if one is a permutation or anagram of the other

Approach 1. Sort those two strings and compare O(nlogn)

Approach 2: Compare their character counts -> constant tim, because we have at max 256 compares (ASCII lens)
"""


def get_char_count(string):
    count_arr = [0 for i in range(256)]

    for s in string:
        count_arr[ord(s)] += 1

    return count_arr


def is_anagram(str1, str2):
    c1 = get_char_count(str1)
    c2 = get_char_count(str2)

    for i in range(256):
        if c1[i] != c2[i]:
            return False

    return True
