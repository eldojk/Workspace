# coding=utf-8
"""
http://www.geeksforgeeks.org/given-an-array-of-pairs-find-all-symmetric-pairs-in-it/
"""
from DS.algos.math.factorial import iterative_factorial
from G4G.Problems.bst.merge_two_balanced_bst import get_inorder_array
from G4G.Problems.bst.vertical_sum import Node
from sys import maxint


def find_symmetric_pairs(array):
    hm = {key: value for (key, value) in array}

    for element in array:
        key = element[0]
        value = element[1]

        symmetric_val = hm.get(value)
        if symmetric_val == key:
            print element,


if __name__ == '__main__':
    find_symmetric_pairs([(11, 20), (30, 40), (5, 10), (40, 30), (10, 5)])

"""
amzn

http://www.geeksforgeeks.org/find-four-elements-a-b-c-and-d-in-an-array-such-that-ab-cd/
"""


def find_ab_cd_equal_sum(array):
    sums = {}

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            _sum = array[i] + array[j]
            if sums.get(_sum):
                print sums[_sum], 'and', (array[i], array[j])
            else:
                sums[_sum] = (array[i], array[j])


if __name__ == '__main__':
    print ''
    print ''
    find_ab_cd_equal_sum([3, 4, 7, 1, 2, 9, 8])

"""
http://www.geeksforgeeks.org/find-itinerary-from-a-given-list-of-tickets/
"""


def find_itinerary(hm):
    sources = set(hm.keys())
    destinations = set(hm.values())

    source = list(sources - destinations)[0]

    while hm.get(source):
        print source, hm[source]
        source = hm[source]


if __name__ == "__main__":
    print ''
    itinerary = {
        "Chennai": "Banglore",
        "Bombay": "Delhi",
        "Goa": "Chennai",
        "Delhi": "Goa"
    }
    find_itinerary(itinerary)

"""
http://www.geeksforgeeks.org/find-missing-elements-of-a-range/
"""


def print_missing_elements_in_range(array, hi, lo):
    print ''
    _range = range(hi, lo + 1)
    hm = {el: True for el in array}

    for el in _range:
        if hm.get(el):
            continue
        else:
            print el,


if __name__ == "__main__":
    print_missing_elements_in_range([10, 12, 11, 15], 10, 15)
    print ''

"""
http://www.geeksforgeeks.org/pair-with-given-product-set-1-find-if-any-pair-exists/
"""


def find_pair_with_given_product(array, product):
    hm = {}
    for el in array:
        if el == 0 and product == 0:
            return True
        elif product % el == 0 and hm.get(product / el):
            return True
        else:
            hm[el] = True

    return False


if __name__ == '__main__':
    print ''
    print find_pair_with_given_product([10, 20, 9, 40], 400)
    print find_pair_with_given_product([10, 20, 9, 40], 190)
    print find_pair_with_given_product([-10, 20, 9, -40], 400)
    print find_pair_with_given_product([-10, 20, 9, 40], -400)
    print find_pair_with_given_product([0, 20, 9, 40], 0)

"""
amzn

http://www.geeksforgeeks.org/find-subarray-with-given-sum/

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
    subarray_with_sum([1, 4, 20, 3, 10, 5], 33)
    subarray_with_sum([1, 4, 0, 0, 3, 10, 5], 7)
    subarray_with_sum([1, 4], 0)


def sub_array_with_sum_hashmap(array, sm):
    curr_sum = 0
    hm = {}

    for i in range(len(array)):
        el = array[i]
        curr_sum += el

        if curr_sum == sm:
            print 0, i

        if hm.get(curr_sum - sm) is not None:
            indexes = hm[curr_sum - sm]
            for idx in indexes:
                print idx + 1, i

        hm[curr_sum] = [i] if hm.get(curr_sum) is None else hm[curr_sum] + [i]


if __name__ == '__main__':
    print ''
    sub_array_with_sum_hashmap([1, 4, 20, 3, 10, 5], 33)
    sub_array_with_sum_hashmap([1, 4, 0, 0, 3, 10, 5], 7)
    sub_array_with_sum_hashmap([1, 4], 0)

"""
http://www.geeksforgeeks.org/print-all-subarrays-with-0-sum/
"""

if __name__ == '__main__':
    print ''
    sub_array_with_sum_hashmap([6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7], 0)

"""
http://www.geeksforgeeks.org/group-shifted-string/
"""


def get_int_rep(string):
    s = ord(string[0]) - ord('a')
    rep = ''
    for i in range(1, len(string)):
        ascii = ord(string[i]) - ord('a')
        diff = ascii - s
        rep += str(diff)
        s = ascii

    return rep


def find_shifted_strings(array):
    hm = {}
    for s in array:
        rep = get_int_rep(s)
        hm[rep] = [s] if hm.get(rep) is None else hm[rep] + [s]

    for el in hm.keys():
        print hm[el] if len(hm[el]) > 1 else '',


if __name__ == '__main__':
    print ''
    find_shifted_strings(["acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"])

"""
amzn

http://www.geeksforgeeks.org/count-maximum-points-on-same-line/
"""
from fractions import gcd


def compute_slope(p1, p2):
    s = (p2[1] - p1[1], p2[0] - p1[0])
    g = gcd(s[0], s[1])
    s = (s[0] / g, s[1] / g)
    return s


def find_max_pts_in_same_line(pts):
    slope_map = {}

    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            p1 = pts[i]
            p2 = pts[j]
            slope = compute_slope(p1, p2)
            if slope_map.get(slope):
                slope_map[slope].add(p1)
                slope_map[slope].add(p2)
            else:
                slope_map[slope] = set([p1, p2])

    max_num = 0
    max_slope = None
    for k in slope_map.keys():
        if max_num < len(slope_map[k]):
            max_num = len(slope_map[k])
            max_slope = slope_map[k]

    return max_slope


if __name__ == '__main__':
    print ''
    print ''
    print find_max_pts_in_same_line([(-1, 1), (0, 0), (1, 1), (2, 2), (3, 3), (3, 4)])


"""
http://www.geeksforgeeks.org/find-pairs-given-sum-elements-pair-different-rows/
"""


def find_pair_some_different_rows(matrix, k):
    hm = {}
    for i in range(len(matrix)):
        for el in matrix[i]:
            hm[el] = i

    for i in range(len(matrix)):
        for el in matrix[i]:
            if hm.get(k - el) is not None and hm[k - el] != i:
                print (el, k - el),


if __name__ == '__main__':
    print ''
    m = [[1, 3, 2, 4],
         [5, 8, 7, 6],
         [9, 10, 13, 11],
         [12, 0, 14, 15]]
    find_pair_some_different_rows(m, 11)

"""
http://www.geeksforgeeks.org/distinct-strings-odd-even-changes-allowed/
"""


def get_odd_even_swap_char_anagram(string):
    od = []
    ev = []
    for i in range(len(string)):
        if i % 2 == 0:
            ev.append(string[i])
        else:
            od.append(string[i])

    od.sort()
    ev.sort()

    return "".join(od) + "".join(ev)


def find_distinct_odd_even_swappable_strings(strings):
    hm = {}

    count = 0
    for s in strings:
        key = get_odd_even_swap_char_anagram(s)
        if hm.get(key):
            continue
        else:
            hm[key] = True
            count += 1

    print count


if __name__ == '__main__':
    print ''
    print ''
    find_distinct_odd_even_swappable_strings(["abcd", "cbad", "bacd"])
    find_distinct_odd_even_swappable_strings(["abc", "cba"])

"""
http://www.geeksforgeeks.org/maximum-distance-two-occurrences-element-array/
"""


def max_dist_of_two_elements(array):
    hm = {}
    for i in range(len(array)):
        if hm.get(array[i]) is not None:
            hm[array[i]].append(i)
        else:
            hm[array[i]] = [i]

    max_dist = 0
    for key in hm.keys():
        el = hm[key]
        dist_el = abs(max(el) - min(el))
        max_dist = max(max_dist, dist_el)

    return max_dist


if __name__ == '__main__':
    print ''
    print max_dist_of_two_elements([3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2])

"""
http://www.geeksforgeeks.org/count-index-pairs-equal-elements-array/
"""


def nc2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1

    nf = iterative_factorial(n)
    cf = 2
    nm2f = iterative_factorial(n - 2)

    return nf / (cf * nm2f)


def count_index_pairs_equal_elements(array):
    fc = {}
    for el in array:
        if fc.get(el) is not None:
            fc[el] += 1
        else:
            fc[el] = 1

    sm = 0
    for k in fc.keys():
        if fc[k] > 1:
            sm += nc2(fc[k])

    return sm


if __name__ == '__main__':
    print ''
    print count_index_pairs_equal_elements([1, 1, 2])
    print count_index_pairs_equal_elements([1, 1, 1])

"""
http://www.geeksforgeeks.org/union-and-intersection-of-two-sorted-arrays-2/
"""


def sorted_array_union(array1, array2):
    i = 0;
    j = 0;

    union = []
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            union.append(array1[i])
            i += 1
        elif array1[i] > array2[j]:
            union.append(array2[j])
            j += 1
        else:
            union.append(array1[i])
            i += 1
            j += 1

    while i < len(array1):
        union.append(array1[i])
        i += 1

    while j < len(array2):
        union.append(array2[j])
        j += 1

    return union


def sorted_array_intersection(array1, array2):
    i = 0;
    j = 0;

    intersection = []
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            i += 1
        elif array1[i] > array2[j]:
            j += 1
        else:
            intersection.append(array1[i])
            i += 1
            j += 1

    return intersection


if __name__ == '__main__':
    print ''
    print sorted_array_union([1, 3, 4, 5, 7], [2, 3, 5, 6])
    print sorted_array_intersection([1, 3, 4, 5, 7], [2, 3, 5, 6])

"""
Find a pair with sum 0 sorted array
"""


def find_pair_with_sum(array, sm):
    i = 0
    j = len(array) - 1

    while i <= j:
        if array[i] + array[j] == sm:
            return i, j
        elif array[i] + array[j] > sm:
            j -= 1
        else:
            i += 1

    return None


if __name__ == '__main__':
    print ''
    a = [-3, 1, 2, 3, 4, 9, 10]
    print find_pair_with_sum(a, 0)


"""
amzn

http://www.geeksforgeeks.org/to-find-smallest-and-second-smallest-element-in-an-array/
"""


def find_second_smallest_and_largest(array):
    first_s = maxint
    second_s = maxint
    first_l = -maxint
    second_l = -maxint

    n = len(array)

    if n < 2:
        print 'Not possible'
        return

    for i in range(n):

        if array[i] < first_s:
            second_s = first_s
            first_s = array[i]

        elif array[i] < second_s and array[i] != first_s:
            second_s = array[i]

        if array[i] > first_l:
            second_l = first_l
            first_l = array[i]

        elif array[i] > second_l and array[i] != first_l:
            second_l = array[i]

    if second_s == maxint or second_l == -maxint:
        print 'No second largest/smallest element'

    else:
        print 'smallest {0}, second smallest {1}'.format(str(first_s), str(second_s))
        print 'largest {0}, second largest {1}'.format(str(first_l), str(second_l))


if __name__ == '__main__':
    print ''
    find_second_smallest_and_largest([12, 13, 1, 10, 34, 1])


"""
http://www.geeksforgeeks.org/find-the-missing-number/
"""


def missing_num(array):
    n = len(array) + 1
    expected_sum = (n * (n + 1)) / 2

    observed_sum = 0
    for candidate in array:
        observed_sum += candidate

    return expected_sum - observed_sum


if __name__ == '__main__':
    print ''
    print missing_num([1, 2, 3, 4, 6, 7, 8])


"""
amzn

http://www.geeksforgeeks.org/count-substrings-with-same-first-and-last-characters/
"""


def find_num_substrings_with_same_first_and_last_char(string):
    """
     each char is a substring with same first and last char

     also for a string ending at char at i, if the same char
     occured before, then that occurrence to this will be a substring

    :param string:
    :return:
    """

    total = len(string)
    occ = {}

    for i in range(len(string)):
        if occ.get(string[i]) is not None:
            num = occ[string[i]]
            total += num
            occ[string[i]] = num + 1
        else:
            occ[string[i]] = 1

    return total


if __name__ == '__main__':
    print ''
    print find_num_substrings_with_same_first_and_last_char('abcab')
    print find_num_substrings_with_same_first_and_last_char('aba')


"""
amzn
"""


def get_pair_with_given_product_two_arrays(array1, array2, product):
    hm = {i: True for i in array2}

    for num in array1:
        element = product // num

        if hm.get(element):
            return num, element

    return None


if __name__ == '__main__':
    print ''
    print get_pair_with_given_product_two_arrays([1, 3, 5], [4, 5, 6], 15)


"""
amzn

http://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/
"""


def binary_search(array, l, h, key):
    if h < l:
        return -1

    mid = (l + h) // 2

    if array[mid] == key:
        return mid

    elif array[mid] < key:
        return binary_search(array, mid + 1, h, key)

    else:
        return binary_search(array, l, mid - 1, key)


def search_inf_array(array, key):
    l, h = 0
    val = array[0]

    while val < key:
        l = h
        h *= 2  # double h
        val = array[h]

    return binary_search(array, l, h, key)


"""
amzn

http://www.geeksforgeeks.org/segregate-even-and-odd-numbers/
"""


def segregate_odd_even(array):
    l = 0
    r = len(array) - 1

    while l < r:

        while array[l] % 2 == 1 and l < r:
            l += 1

        while array[r] % 2 == 0 and l < r:
            r -= 1

        if l < r:
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1

    return array


if __name__ == '__main__':
    print ''
    print segregate_odd_even([12, 34, 45, 9, 8, 90, 3])



"""
amzn

http://www.geeksforgeeks.org/move-zeroes-end-array/
"""


def push_zeroes_to_end(array):
    n = len(array)
    c = 0

    for i in range(n):
        if array[i] != 0:
            array[c] = array[i]
            c += 1

    while c < n:
        array[c] = 0
        c += 1

    return array


if __name__ == '__main__':
    print ''
    print push_zeroes_to_end([1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9])


"""
sorted array to balanced bst

http://www.geeksforgeeks.org/sorted-array-to-balanced-bst/
"""


def convert_sorted_array_to_bst(array, l, h):
    if l > h:
        return None

    mid = (l + h) // 2

    root = Node(array[mid])

    root.left = convert_sorted_array_to_bst(array, l, mid - 1)
    root.right = convert_sorted_array_to_bst(array, mid + 1, h)

    return root


if __name__ == '__main__':
    print ''
    r = convert_sorted_array_to_bst([1, 2, 3, 4, 5], 0, 4)
    print get_inorder_array(r, [])


"""
amzn

http://www.geeksforgeeks.org/count-negative-numbers-in-a-column-wise-row-wise-sorted-matrix/
"""


def count_negatives(matrix):
    m = len(matrix)
    n = len(matrix[0])

    count = 0
    i = 0
    j = n - 1

    while i < m and j >= 0:
        if matrix[i][j] < 0:

            count += j + 1

            i += 1

        else:
            j -= 1

    return count


if __name__ == '__main__':
    print ''
    m = [
      [-3, -2, -1,  1],
      [-2,  2,  3,  4],
      [4,   5,  7,  8]
    ]

    print count_negatives(m)


"""
amzn

http://www.geeksforgeeks.org/find-pythagorean-triplet-in-an-unsorted-array/
"""


def pythagorean_triplet(array):
    sq_arr = [i*i for i in array]

    sq_arr.sort()

    n = len(array)
    i = n - 2

    while i >= 2:
        l = 0
        r = i - 1

        while l < r:
            if sq_arr[l] + sq_arr[r] > sq_arr[i]:
                r -= 1

            elif sq_arr[l] + sq_arr[r] < sq_arr[i]:
                l += 1

            else:
                return True
        i -= 1

    return False


if __name__ == '__main__':
    print ''
    print pythagorean_triplet([3, 1, 4, 6, 5])


"""
amzn

http://www.geeksforgeeks.org/a-product-array-puzzle/
"""


def get_product_array(array):
    left_arr = [1 for i in array]
    right_arr = [1 for i in array]

    for i in range(1, len(array)):
        left_arr[i] = array[i] * left_arr[i - 1]

    i = len(array) - 2
    while i >= 0:
        right_arr[i] = array[i] * right_arr[i + 1]
        i -= 1

    prod_arr = []
    for i in range(len(array)):
        prod_arr.append(left_arr[i] * right_arr[i])

    return prod_arr


"""
amzn

http://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/
"""


def custom_comparator(a, b):
    ab = int(a + b)
    ba = int(b + a)

    if ab > ba:
        return 1
    elif ab < ba:
        return -1
    else:
        return 0


def print_largest(array):
    array = map(str, array)
    array.sort(cmp=custom_comparator)
    array.reverse()
    print ''.join(array)


if __name__ == '__main__':
    print ''
    print_largest([54, 546, 548, 60])


"""
amzn

http://www.geeksforgeeks.org/find-two-rectangles-overlap/
"""


def is_in_rectangle(x, a, b):
    return a[0] < x[0] < b[0] and a[1] < x[1] < b[1]


def do_rectangles_overlap(c1, c2, a1, a2):
    c3 = (c1[0], c2[1])
    c4 = (c1[1], c2[0])

    return is_in_rectangle(c1, a1, a2) or \
        is_in_rectangle(c2, a1, a2) or \
        is_in_rectangle(c3, a1, a2) or \
        is_in_rectangle(c4, a1, a2)


"""
amzn

http://www.geeksforgeeks.org/find-common-elements-three-sorted-arrays/
"""


def find_common_among_three_arrays(a, b, c):
    x = y = z = 0

    while x < len(a) and y < len(b) and z < len(c):
        if a[x] == b[y] == c[z]:
            print a[x],
            x += 1
            y += 1
            z += 1

        elif a[x] < b[y]:
            x += 1

        elif b[y] < c[z]:
            y += 1

        else:
            z += 1


if __name__ == '__main__':
    print ''
    find_common_among_three_arrays(
        [1, 5, 10, 20, 40, 80],
        [6, 7, 20, 80, 100],
        [3, 4, 15, 20, 30, 70, 80, 120]
    )


"""
amzn

http://www.ideserve.co.in/learn/find-common-elements-in-n-sorted-arrays
"""


def get_common_elements_n_arrays(arrays):
    smallest_array_finished = False
    base_index = 0
    indices = [0 for i in arrays]

    while base_index < len(arrays[0]) and not smallest_array_finished:

        matched = 0
        for i in range(1, len(arrays)):
            curr_idx = indices[i]

            while curr_idx < len(arrays[i]) and arrays[i][curr_idx] < arrays[0][base_index]:
                curr_idx += 1

            if curr_idx < len(arrays[i]):
                if arrays[i][curr_idx] == arrays[0][base_index]:
                    matched += 1

            else:
                smallest_array_finished = True

            indices[i] = curr_idx

        if matched == len(arrays) - 1:
            print arrays[0][base_index],

        base_index += 1


if __name__ == '__main__':
    print ''
    print ''
    get_common_elements_n_arrays([
        [23, 34, 67, 89, 123, 566, 1000],
        [11, 22, 23, 24,33, 37, 185, 566, 987, 1223, 1234],
        [23, 43, 67, 98, 566, 6780],
        [1, 4, 5, 23, 34, 76, 87, 132, 566, 665],
        [1, 2, 3, 23, 24, 344, 566]
    ])
    print ''


"""
amzn

http://www.geeksforgeeks.org/count-number-of-occurrences-or-frequency-in-a-sorted-array/

1) Use Binary search to get index of the first occurrence of x in arr[]. Let the index of
the first occurrence be i.
2) Use Binary search to get index of the last occurrence of x in arr[]. Let the index of
the last occurrence be j.
3) Return (j – i + 1);
"""


def first_occurrence(array, l, h, x):
    if h >= l:
        mid = (l + h) // 2

        if mid == 0 or (x > array[mid - 1] and array[mid] == x):
            return mid

        elif x > array[mid]:
            return first_occurrence(array, mid + 1, h, x)

        else:
            return first_occurrence(array, l, mid - 1, x)

    return -1


def last_occurrence(array, l, h, x):
    if h >= l:
        mid = (l + h) // 2

        if mid == h or (x < array[mid + 1] and array[mid] == x):
            return mid

        elif x < array[mid]:
            return last_occurrence(array, l, mid - 1, x)

        return last_occurrence(array, mid + 1, h, x)

    return -1


def count_occurrences(array, x):
    n = len(array)
    i = first_occurrence(array, 0, n - 1, x)

    if i == -1:
        return 0

    j = last_occurrence(array, 0, n - 1, x)

    return j - i + 1


if __name__ == '__main__':
    print ''
    print count_occurrences([1, 2, 2, 3, 3, 3, 3], 3)




































