# coding=utf-8
"""
msft

https://www.careercup.com/question?id=5698738912755712

Given two sets of strings A and B. Find the (A-B) U (B-A) ( U = union ). The answer should be in lexicographical order
and A’s elements should appear before B’s.
"""


def get_result(array1, array2):
    array1.sort()
    array2.sort()

    res = []
    i = 0
    m = len(array1)
    j = 0
    n = len(array2)

    while i < m and j < n:
        if array1[i] < array2[j]:
            res.append(array1[i])
            i += 1

        elif array2[j] < array1[i]:
            res.append(array2[j])
            j += 1

        else:
            while i + 1 < m:
                if array1[i] == array1[i + 1]:
                    i += 1
                else:
                    break

            while j + 1 < n:
                if array2[j] == array2[j + 1]:
                    j += 1
                else:
                    break

            i += 1
            j += 1

    while i < m:
        res.append(array1[i])
        i += 1

    while j < n:
        res.append(array2[j])
        j += 1

    return res


if __name__ == '__main__':
    print get_result(['a', 'b', 'c', 'c', 'd'], ['c', 'd', 'd', 'g', 'h'])
    print get_result(["asd", "efg", "lkm", "sumit", "rohit", "zxc", "awe"], ["zxc", "awe", "efg", "zzx"])