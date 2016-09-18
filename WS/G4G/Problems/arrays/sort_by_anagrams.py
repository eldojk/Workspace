"""
Sort a list of strings such that all anagrams are next to each other
CTCI 11.2 #361
"""


def sort_array(array):
    dict = {}

    for string in array:
        key = list(string)
        key.sort()
        key = ''.join(key)

        dict[key] = [string] if dict.get(key) is None else dict[key] + [string]

    sorted_array = []
    for key in dict.keys():
        sorted_array.extend(dict[key])

    return sorted_array

# print sort_array(['abc', 'bcb', 'bca', 'bac', 'bbc', 'aaggf', 'rrts', 'ggafa'])
