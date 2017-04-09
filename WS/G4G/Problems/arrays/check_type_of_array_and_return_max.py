"""
http://www.geeksforgeeks.org/type-array-maximum-element/
"""


def check_type(array):
    array = array.extend(array)

    n = len(array)

    i = 0
    j = 0

    f1 = False
    f2 = False

    while i < n - 1 and j < n - 1:
        if array[i] < array[i + 1]:
            i += 1
            f1 = True

        if array[j] > array[j + 1]:
            j += 1
            f2 = True

        if not (f1 or f2):
            break

        f1 = False
        f2 = False


    



if __name__ == '__main__':
    #print check_type([4, 5, 6, 1, 2, 3])
    #print check_type([6, 1, 2, 3, 4, 5])
    print check_type([2, 1, 7, 5, 4, 3])