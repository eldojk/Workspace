"""
http://www.geeksforgeeks.org/find-pairs-with-given-sum-such-that-pair-elements-lie-in-different-bsts/

^ check the sol
"""

def find_sum_pair(array1, array2, sum_to_find):
    i = 0
    j = len(array2) - 1

    while i < len(array1) and j >= 0:
        if sum_to_find == array1[i] + array2[j]:
            return array1[i], array2[j]
        elif sum_to_find > array1[i] + array2[j]:
            i += 1
        else:
            j -= 1


print find_sum_pair([1, 4, 6, 7, 9], [2, 3, 4, 5, 8], 7)




