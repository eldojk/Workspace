"""
msft

http://www.geeksforgeeks.org/remove-all-duplicates-from-the-input-string/
"""


def remove_dupes(string):
    hm = {}
    string = list(string)

    i = 0
    j = 0

    while j < len(string):
        c = string[j]

        if hm.get(c):
            j += 1

        else:
            hm[c] = True
            string[i] = string[j]
            i += 1
            j += 1

    return ''.join(string[:i])


if __name__ == '__main__':
    print remove_dupes('geeksforgeeks')
