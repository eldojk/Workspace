"""
http://stackoverflow.com/questions/9368205/given-a-number-find-the-next-higher-number-which-has-the-exact-same-set-of-digi

Find the first element that is less than its next from the end.
From this element, move right and find next greater element.
swap them. and sort the array to the right
123456784987654321
"""


def next_permutation(string):
    array = list(string)
    array = map(int, array)

    j = len(array) - 1

    while j > 0:
        right = array[j]
        left = array[j - 1]

        if left < right:
            break

        j -= 1

    index = j - 1

    nxt_grtr = j
    for i in range(j, len(array) - 1):
        if array[i] < array[nxt_grtr] and array[i] > array[index]:
            nxt_grtr = i

    array[index], array[nxt_grtr] = array[nxt_grtr], array[index]

    array_to_sort = array[index + 1:]
    array_to_sort.sort()

    for i in range(len(array_to_sort)):
        array[index + 1 + i] = array_to_sort[i]

    array = map(str, array)
    return ''.join(array)

# print next_permutation('123456784987654321')
