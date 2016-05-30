"""
Palindrome
"""


def is_palindrome(string):
    # base case
    str_len = len(string)
    if str_len <= 1:
        return True

    string = string.lower()

    # base case 2 (check if first and last characters are same)
    if string[0] != string[str_len - 1]:
        return False

    # recursive case
    string = string[1:(str_len - 1)]
    return is_palindrome(string)