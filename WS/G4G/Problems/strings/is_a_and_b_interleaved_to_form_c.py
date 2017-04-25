"""
amzn

this is not dp. done it differently here
http://www.geeksforgeeks.org/check-whether-a-given-string-is-an-interleaving-of-two-other-given-strings-set-2/
"""


def remove_string_from_string(a, c):
    if len(a) == 0:
        return c

    c = list(c)

    ia = 0
    ia_max = len(a)

    for i in range(len(c)):
        if c[i] == a[ia]:
            c[i] = None
            ia += 1

        if ia >= ia_max:
            break

    c = [character for character in c if character is not None]

    return ''.join(c), (ia == ia_max)


def is_inter_leaved(a, b, c):
    rm_str, successfully_removed = remove_string_from_string(a, c)

    if not successfully_removed:
        return False

    return rm_str == b


if __name__ == '__main__':
    print is_inter_leaved("abcd", "xyz", "axybczd")
    print is_inter_leaved("AB", "CD", "CADB")
    print is_inter_leaved("AB" ,"CD" ,"CDAB")
    print is_inter_leaved("DAACSA" ,"DAS" ,"AAACC")
    print is_inter_leaved('XXZ', 'XXXY', 'XXZXXXY')