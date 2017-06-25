"""
Reverse a string. CTCI: 173, #1.2
"""


def reverse(string):
    en = len(string) - 1
    _string = list(string)
    for i in range(len(string) / 2):  # iterate till half only, because by the time
        # we reach mid, the other half is done
        j = en - i
        _string[i], _string[j] = _string[j], _string[i]

    return "".join(_string)
