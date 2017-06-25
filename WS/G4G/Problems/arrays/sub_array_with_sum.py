"""
amzn

more questions down **

http://www.geeksforgeeks.org/find-subarray-with-given-sum/

Initialize a variable curr_sum as first element. curr_sum indicates the
sum of current subarray. Start from the second element and add all elements
one by one to the curr_sum. If curr_sum becomes equal to sum, then print
the solution. If curr_sum exceeds the sum, then remove trailing elements
while curr_sum is greater than sum.

note - this is o(n). check link for proof
"""


def subarray_with_sum(array, sm):
    curr_sum = array[0]
    start = 0

    for i in range(1, len(array) + 1):

        while curr_sum > sm and start < i - 1:
            curr_sum = curr_sum - array[start]
            start += 1

        if curr_sum == sm:
            print start, i - 1

        if i < len(array):
            curr_sum = curr_sum + array[i]


if __name__ == '__main__':
    print ''
    print 'find sub array with given sum'
    subarray_with_sum([1, 4, 20, 3, 10, 5], 33)
    subarray_with_sum([1, 4, 0, 0, 3, 10, 5], 7)
    subarray_with_sum([1, 4], 0)


"""
msft

http://www.geeksforgeeks.org/print-all-subarrays-with-0-sum/
http://www.geeksforgeeks.org/find-subarray-with-given-sum-in-array-of-integers/
"""


def sub_array_with_sum_hashmap(array, sm):
    curr_sum = 0
    # hm with sum and index where it found. This initialization handles a corner case
    # where the sum we are searching the value of first element
    hm = {0: [-1]}

    for i in range(len(array)):
        el = array[i]
        curr_sum += el

        if curr_sum == sm:
            print 0, i

        if hm.get(curr_sum - sm) is not None:
            # ^ this means sm exists
            indexes = hm[curr_sum - sm]
            for idx in indexes:
                print idx + 1, i

        hm[curr_sum] = [i] if hm.get(curr_sum) is None else hm[curr_sum] + [i]


if __name__ == '__main__':
    print ''
    print 'find sub array with given sum including negatives'
    sub_array_with_sum_hashmap([1, 4, 20, 3, 10, 5], 33)
    print ''
    sub_array_with_sum_hashmap([1, 4, 0, 0, 3, 10, 5], 7)
    print ''
    sub_array_with_sum_hashmap([1, 4], 0)
    print ''
    sub_array_with_sum_hashmap([6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7], 0)
