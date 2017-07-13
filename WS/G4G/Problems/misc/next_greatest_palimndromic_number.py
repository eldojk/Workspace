# coding=utf-8
"""
amzn

http://www.geeksforgeeks.org/given-a-number-find-next-smallest-palindrome-larger-than-this-number/

^ very detailed explanation (refer to see the cases)

There can be three different types of inputs that need to be handled separately.
1) The input number is palindrome and has all 9s. For example “9 9 9”. Output should be “1 0 0 1”
2) The input number is not palindrome. For example “1 2 3 4”. Output should be “1 3 3 1”
3) The input number is palindrome and doesn’t have all 9s. For example “1 2 2 1”.
Output should be “1 3 3 1”.
"""


def are_all_9s(array):
    for n in array:
        if n != 9:
            return False

    return True


def print_number(array):
    print ''.join(map(str, array))


def gen_next_pal(array):
    n = len(array)
    mid = n // 2
    left_smaller = False  # flag to check if copying left to right is sufficient

    i = mid - 1
    j = mid if n % 2 == 0 else mid + 1

    # ignore same middle digits
    while i >= 0 and array[i] == array[j]:
        i -= 1
        j += 1

    # Find if the middle digit(s) need to be incremented or not
    # (or copying left side is not sufficient)
    if i < 0 or array[i] < array[j]:
        left_smaller = True

    # mirror the right with left
    while i >= 0:
        array[j] = array[i]
        i -= 1
        j += 1

    # handling middle digits increment requirement
    if left_smaller:
        carry = 1
        i = mid - 1

        if n % 2 == 1:
            array[mid] += carry
            carry = array[mid] // 10
            array[mid] %= 10
            j = mid + 1

        else:
            j = mid

        while i >= 0:
            array[i] += carry
            carry = array[i] // 10
            array[i] %= 10
            array[j] = array[i]
            i -= 1
            j += 1


def generate_next_palindrome(array):
    if are_all_9s(array):
        zero_arr = [0 for i in range(len(array) + 1)]
        zero_arr[0] = 1
        zero_arr[len(array)] = 1
        print_number(zero_arr)

    else:
        gen_next_pal(array)
        print_number(array)


if __name__ == '__main__':
    arr = [9, 4, 1, 8, 7, 9, 7, 8, 3, 2, 2]

    generate_next_palindrome(arr)
