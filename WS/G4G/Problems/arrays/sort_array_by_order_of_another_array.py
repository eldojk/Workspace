"""
amzn, msft

http://www.geeksforgeeks.org/sort-array-according-order-defined-another-array/
"""

HM = None


def comparator(num1, num2):
    if HM.get(num1) is None and HM.get(num2) is None:
        if num1 < num2:
            return -1

        elif num1 > num2:
            return 1

        else:
            return 0

    if HM.get(num1) is not None and HM.get(num2) is not None:
        n1 = HM[num1]
        n2 = HM[num2]

        if n1 < n2:
            return -1

        elif n1 > n2:
            return 1

        else:
            return 0

    if HM.get(num1) is not None:
        return -1

    else:
        return 1


def sort_by_array(array1, array2):
    global HM
    HM = {}

    for i in range(len(array2)):
        HM[array2[i]] = i

    array1.sort(cmp=comparator)
    return array1


if __name__ == '__main__':
    print sort_by_array([2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8, 7, 5, 6, 9, 7, 5],
                        [2, 1, 8, 3, 4])
