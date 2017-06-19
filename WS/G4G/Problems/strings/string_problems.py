"""
msft

http://www.geeksforgeeks.org/longest-non-palindromic-substring/

Check for the case where all characters of
the string are same or not.
    If yes, then answer will be '0'.
Else check whether the given string of size
'n' is palindrome or not.
    If yes, then answer will be 'n-1'
Else answer will be 'n'
"""
from G4G.Problems.dp.palindromic_partitioning import is_palindrome


def _is_all_char_same(string):
    ch = string[0]
    for c in string:
        if ch != c:
            return False

    return True


def longest_non_palindromic_substring(string):
    if _is_all_char_same(string):
        return 0

    n = len(string)
    if is_palindrome(string, 0, n - 1):
        return n - 1

    return n


if __name__ == '__main__':
    print longest_non_palindromic_substring('abba')