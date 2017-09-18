# coding=utf-8
"""
http://www.geeksforgeeks.org/given-an-array-of-pairs-find-all-symmetric-pairs-in-it/
"""
from DS.algos.math.factorial import iterative_factorial
from G4G.Problems.bst.merge_two_balanced_bst import get_inorder_array
from G4G.Problems.bst.vertical_sum import Node
from sys import maxint


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


def find_symmetric_pairs(array):
    hm = {key: value for (key, value) in array}

    for element in array:
        key = element[0]
        value = element[1]

        symmetric_val = hm.get(value)
        if symmetric_val == key:
            print element,


if __name__ == '__main__':
    print 'symmetric pairs'
    find_symmetric_pairs([(11, 20), (30, 40), (5, 10), (40, 30), (10, 5)])


"""
amzn

find 4 elements a, b, c, d such that a + b = c + d.
If there are multiple answers, then print any of them.

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
    print 'find 4 elements a, b, c, d such that a + b = c + d'
    find_ab_cd_equal_sum([3, 4, 7, 1, 2, 9, 8])


"""
http://www.geeksforgeeks.org/find-itinerary-from-a-given-list-of-tickets/
"""


def find_itinerary(hm):
    sources = set(hm.keys())
    destinations = set(hm.values())

    # starting point will be in sources but not
    # in destinations
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
    _range = range(hi, lo + 1)
    hm = {el: True for el in array}

    for el in _range:
        if hm.get(el):
            continue
        else:
            print el,


if __name__ == "__main__":
    print ''
    print 'missing elements in range'
    print_missing_elements_in_range([10, 12, 11, 15], 10, 15)
    print ''


def print_missing_elements_in_range_using_sort(array, lo, hi):
    array.sort()
    r = range(lo, hi + 1)
    l = 0
    h = len(array) - 1
    i = 0

    while i <= h:
        idx = binary_search(array, l, h, r[i])
        if idx == -1:
            print r[i],
        else:
            break

        i += 1

    id = idx + 1
    while id <= h:
        if array[id] - array[id - 1] > 1:
            for i in range(array[id - 1] + 1, array[id]):
                print i,

        id += 1


if __name__ == "__main__":
    print ''
    print 'missing elements in range using sorting'
    print_missing_elements_in_range_using_sort([10, 12, 11, 15], 10, 15)
    print ''


"""
amzn

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
    print 'Pair with given product'
    print find_pair_with_given_product([10, 20, 9, 40], 400),
    print find_pair_with_given_product([10, 20, 9, 40], 190),
    print find_pair_with_given_product([-10, 20, 9, -40], 400),
    print find_pair_with_given_product([-10, 20, 9, 40], -400),
    print find_pair_with_given_product([0, 20, 9, 40], 0)


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
    print 'Group shifted string together'
    find_shifted_strings(["acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"])


"""
amzn

http://www.geeksforgeeks.org/count-maximum-points-on-same-line/
"""


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


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
    print 'Max points on a line'
    print find_max_pts_in_same_line([(-1, 1), (0, 0), (1, 1), (2, 2), (3, 3), (3, 4)])


"""
we can also sort the rows and find pairs

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
    print 'Sum pairs in different rows'
    m = [[1, 3, 2, 4],
         [5, 8, 7, 6],
         [9, 10, 13, 11],
         [12, 0, 14, 15]]
    find_pair_some_different_rows(m, 11)


"""
http://www.geeksforgeeks.org/distinct-strings-odd-even-changes-allowed/
"""


def get_encoding(string):
    od = []
    ev = []
    for i in range(len(string)):
        if i % 2 == 0:
            ev.append(string[i])
        else:
            od.append(string[i])

    od.sort()  #todo to much complexity. use freq count array instead of this
    ev.sort()

    return "".join(od) + "".join(ev)


def find_distinct_odd_even_swappable_strings(strings):
    hm = {}

    count = 0
    for s in strings:
        key = get_encoding(s)
        if hm.get(key):
            continue
        else:
            hm[key] = True
            count += 1

    print count


if __name__ == '__main__':
    print ''
    print ''
    print 'Distinct strings'
    find_distinct_odd_even_swappable_strings(["abcd", "cbad", "bacd"])
    find_distinct_odd_even_swappable_strings(["abc", "cba"])


"""
http://www.geeksforgeeks.org/maximum-distance-two-occurrences-element-array/
"""


def max_dist_of_two_elements(array):
    # todo too much time complexity. redo
    hm = {}

    # todo
    # just store first occurrence and track max distances
    # for subsequent occurrences
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
    print 'Max distance b/w two occurrences of some element'
    print max_dist_of_two_elements([3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2])


"""
http://www.geeksforgeeks.org/count-index-pairs-equal-elements-array/
"""


def nc2(n):
    if n == 1:
        return 1

    return (n * (n - 1)) / 2


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
    print 'union and intersection'
    print sorted_array_union([1, 3, 4, 5, 7], [2, 3, 5, 6])
    print sorted_array_intersection([1, 3, 4, 5, 7], [2, 3, 5, 6])


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
    print 'missing number: ',
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
    print 'pair with produc two arrays'
    print get_pair_with_given_product_two_arrays([1, 3, 5], [4, 5, 6], 15)


"""
amzn

http://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/
"""


def search_inf_array(array, key):
    l = 0
    h = 1
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
    print 'Segregate odd and even'
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
    print 'Push zeroes to end'
    print push_zeroes_to_end([1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9])


def push_zeroes_to_end_using_swapping(array):
    l = 0
    r = len(array) - 1

    while l < r:

        while array[l] != 0 and l < r:
            l += 1

        while array[r] == 0 and l < r:
            r -= 1

        if l < r:
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1

    return array


if __name__ == '__main__':
    print ''
    print 'Push zeroes to end using swapping'
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
    print 'sorted array to bst'
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

    print 'Count negatives in row wise column wise sorted matrix'
    print count_negatives(m)


"""
amzn

http://www.geeksforgeeks.org/find-pythagorean-triplet-in-an-unsorted-array/
"""


def pythagorean_triplet(array):
    sq_arr = [i*i for i in array]

    sq_arr.sort()

    n = len(array)
    i = n - 1

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
    print 'Pythagorean triplet'
    print pythagorean_triplet([3, 1, 4, 6, 5])


"""
amzn

http://www.geeksforgeeks.org/a-product-array-puzzle/
"""


def get_product_array(array):
    left_arr = [1 for i in array]
    right_arr = [1 for i in array]

    for i in range(1, len(array)):
        left_arr[i] = array[i - 1] * left_arr[i - 1]

    i = len(array) - 2
    while i >= 0:
        right_arr[i] = array[i + 1] * right_arr[i + 1]
        i -= 1

    prod_arr = []
    for i in range(len(array)):
        prod_arr.append(left_arr[i] * right_arr[i])

    return prod_arr


if __name__ == '__main__':
    print ''
    print 'Product array'
    print get_product_array([10, 3, 5, 6, 2])


"""
amzn, msft

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
    array.sort(cmp=custom_comparator, reverse=True)
    print ''.join(array)


if __name__ == '__main__':
    print ''
    print 'largest number by rearranging array of numbers'
    print_largest([54, 546, 548, 60])


"""
amzn, msft

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
amzn, msft

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
    print 'Common element in 3 sorted arrays'
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
    print 'Common elements in n sorted arrays'
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
http://www.geeksforgeeks.org/find-first-last-occurrences-element-sorted-array/

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

    if i == -1 or array[i] != x:
        return 0

    j = last_occurrence(array, 0, n - 1, x)

    return j - i + 1


if __name__ == '__main__':
    print ''
    print 'count occurrences in sorted array'
    print count_occurrences([1, 2, 2, 3, 3, 3, 3], 3)


"""
amzn

read for explanation
http://www.geeksforgeeks.org/find-maximum-value-of-sum-iarri-with-only-rotations-on-given-array-allowed/
"""


def max_sum_rotations(array):
    arr_sum = 0
    curr_val = 0
    n = len(array)

    for i in range(n):
        arr_sum += array[i]
        curr_val += i * array[i]

    max_val = curr_val

    for j in range(1, n):
        curr_val += arr_sum - n * array[n - j]
        max_val = max(curr_val, max_val)

    return max_val


if __name__ == '__main__':
    print ''
    print 'max sum rotation of sum(i*arr[i])'
    print max_sum_rotations([10, 1, 2, 3, 4, 5, 6, 7, 8, 9])


"""
amzn

http://www.geeksforgeeks.org/find-the-minimum-distance-between-two-numbers/
"""


def min_dist(array, x, y):
    _x = -1
    _y = -1
    min_dis = maxint

    for i in range(len(array)):
        if array[i] == x:
            _x = i

        elif array[i] == y:
            _y = i

        if _x != -1 and _y != -1:
            min_dis = min(
                min_dis,
                abs(_x - _y)
            )

    return min_dis


if __name__ == '__main__':
    print ''
    print 'minimum distance between two elements in array'
    print min_dist([3, 5, 4, 2, 6, 3, 0, 0, 5, 4, 8, 3], 3, 6),
    print min_dist([3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3], 3, 6),
    print min_dist([2, 5, 3, 5, 4, 4, 2, 3], 3, 2)


"""
amzn

http://www.geeksforgeeks.org/third-largest-element-array-distinct-elements/
"""


def third_largest(array):
    first = second = third = array[0]

    for i in xrange(len(array)):
        el = array[i]

        if el > first:
            third = second
            second = first
            first = el

        elif el > second:
            third = second
            second = el

        elif el > third:
            third = el

    return third


if __name__ == '__main__':
    print ''
    print 'Third largest in array'
    print third_largest([12, 13, 1, 10, 34, 16])


"""
amzn

http://www.geeksforgeeks.org/search-an-element-in-an-array-where-difference-between-adjacent-elements-is-1/

The idea is to start comparing from the leftmost element and find the difference
between current array element and x. Let this difference be ‘diff’. From the given
property of array, we always know that x must be at-least ‘diff’ away, so instead of
searching one by one, we jump ‘diff’.
"""


def search_in_diff_1_adj_array(array, x):
    i = 0
    n = len(array)

    while i < n:
        if array[i] == x:
            return i

        diff = abs(x - array[i])

        i += diff

    return -1


if __name__ == '__main__':
    print ''
    print 'search in array with adjacent elements differing by 1'
    print search_in_diff_1_adj_array([8, 7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3], 3)


"""
amzn

http://www.geeksforgeeks.org/find-a-fixed-point-in-a-given-array/
"""


def get_fixed_point(array, l, h):
    if l > h:
        return -1

    mid = (l + h) // 2

    if array[mid] == mid:
        return mid

    elif array[mid] > mid:
        return get_fixed_point(array, l, mid - 1)

    else:
        return get_fixed_point(array, mid + 1, h)


if __name__ == '__main__':
    print ''
    print 'getting fixed point in an array'
    print get_fixed_point([-10, -5, 0, 3, 7], 0, 4),
    print get_fixed_point([0, 2, 5, 8, 17], 0, 4),
    print get_fixed_point([-10, -5, 3, 4, 7, 9], 0, 5)


"""
amzn

http://www.geeksforgeeks.org/find-a-pair-with-the-given-difference/
"""


def find_pair_with_diff(array, diff):
    array.sort()
    n = len(array)
    _max = array[n - 1]

    for val in array:
        key = val + diff

        if key > _max:
            print 'not found'
            break

        # todo need to check if pair == key
        # ^ this can arise when diff = 0
        pair = binary_search(array, 0, n - 1, key)

        if pair != -1:
            print val, array[pair]
            break


if __name__ == '__main__':
    print ''
    print 'pair with the given difference'
    find_pair_with_diff([5, 20, 3, 2, 50, 80], 78)


"""
amzn

(another approach)
http://www.geeksforgeeks.org/find-a-pair-with-the-given-difference/
"""


def find_pair_with_given_diff(array, diff):
    array.sort()
    n = len(array)

    i = 0
    j = 1

    while i < n and j < n:
        if array[j] - array[i] == diff and i != j:
            print array[i], array[j]
            break

        elif array[j] - array[i] < diff:
            j += 1

        else:
            i += 1


if __name__ == '__main__':
    print ''
    print 'pair with the given difference'
    find_pair_with_given_diff([5, 20, 3, 2, 50, 80], 78)


"""
amzn

http://www.geeksforgeeks.org/replace-every-element-with-the-greatest-on-right-side/
"""


def replace_with_ge_on_right(array):
    n = len(array)
    max_from_right = array[n - 1]

    array[n - 1] = -1

    i = n - 2
    while i >= 0:
        temp = array[i]
        array[i] = max_from_right

        if max_from_right < temp:
            max_from_right = temp

        i -= 1

    return array


if __name__ == '__main__':
    print ''
    print 'greatest on the right'
    print replace_with_ge_on_right([16, 17, 4, 3, 5, 2])


"""
amzn

http://www.geeksforgeeks.org/count-pairs-with-given-sum/
"""


def count_pairs_with_sum(array, s):
    hm = {}

    for num in array:
        if hm.get(num) is None:
            hm[num] = 0

        hm[num] += 1

    twice_count = 0

    for num in array:
        exptd_sum = s - num

        if hm.get(exptd_sum) is not None:
            twice_count += hm[exptd_sum]

        if exptd_sum == num:
            twice_count -= 1

    return twice_count / 2


if __name__ == '__main__':
    print ''
    print 'count pairs with given sum'
    print count_pairs_with_sum([1, 5, 7, -1, 5], 6)


"""
msft

https://www.careercup.com/question?id=11903257

Suppose we have to divide a number ie 1279 by 3. we get 1279 as streams ..first i get 1 ..1%3=1..1 is stored in rem.
Now 2 comes, we do rem=(1*10+2)%3=0.Now 7 is in teh stream,
rem=(rem*10+7)%3=1, when 9 comes rem=(1*10+9)%3=1. So we get at each step where the stream entered till that place
is divisible by three or not.
Same is the case when stream contains 0 and 1. Instead of multiplying the rem by 10, multiply by 2.
"""
#todo


"""
msft

http://www.geeksforgeeks.org/build-lowest-number-by-removing-n-digits-from-a-given-number/
"""
from G4G.Problems.stacks.stack import Stack


def build_lowest_number_removing_k_digits(num, k):
    s = Stack()
    l = len(num) - k

    for c in num:
        if not s.is_empty() and int(s.peek()) > int(c) and k > 0:
            s.pop()
            k -= 1

        s.push(c)

    return ''.join(s.get_list()[:l])


if __name__ == '__main__':
    print ''
    print 'build_lowest_number_removing_k_digits'
    print build_lowest_number_removing_k_digits('4325043', 3)
    print build_lowest_number_removing_k_digits('765028321', 5)
    print build_lowest_number_removing_k_digits('121198', 2)


"""
msft

http://www.geeksforgeeks.org/given-sorted-array-number-x-find-pair-array-whose-sum-closest-x/
http://www.geeksforgeeks.org/two-elements-whose-sum-is-closest-to-zero/
"""


def get_closest_pair(array, x):
    res_l = 0
    res_r = 0
    l = 0
    n = len(array)
    r = n - 1
    diff = maxint

    while r > l:
        if abs(array[l] + array[r] - x) < diff:
            diff = abs(array[l] + array[r] - x)
            res_l = l
            res_r = r

        if array[l] + array[r] > x:
            r -= 1

        else:
            l += 1

    print 'closest pair: ' + str(array[res_l]) + ', ' + str(array[res_r]) + ', diff: ' + str(diff)


if __name__ == '__main__':
    print ''
    print 'get closest pair to given sum'
    get_closest_pair([10, 22, 28, 29, 30, 40], 54)
    get_closest_pair([1, 3, 4, 7, 10], 15)
    ar = [1, 60, -10, 70, -80, 85]
    ar.sort()
    get_closest_pair(ar, 0)


"""
msft

http://www.geeksforgeeks.org/given-two-sorted-arrays-number-x-find-pair-whose-sum-closest-x/
"""


def get_closest_pair_two_arrays(array1, array2, x):
    res_l = 0
    res_r = 0
    l = 0
    m = len(array1)
    n = len(array2)
    r = n - 1
    diff = maxint

    while r >= 0 and l < m:
        if abs(array1[l] + array2[r] - x) < diff:
            diff = abs(array1[l] + array2[r] - x)
            res_l = l
            res_r = r

        if array1[l] + array2[r] > x:
            r -= 1

        else:
            l += 1

    print 'closest pair: ' + str(array1[res_l]) + ', ' + str(array2[res_r]) + ', diff: ' + str(diff)


if __name__ == '__main__':
    print ''
    print 'get closest pair to given sum in two arrays'
    get_closest_pair_two_arrays([1, 4, 5, 7], [10, 20, 30, 40], 32)
    get_closest_pair_two_arrays([1, 4, 5, 7], [10, 20, 30, 40], 50)


"""
msft

http://www.geeksforgeeks.org/array-rotation/
"""


def reverse_arr(array, i, j):
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1


def rotate(array, k):
    n = len(array)
    reverse_arr(array, 0, k - 1)
    reverse_arr(array, k, n - 1)
    array.reverse()
    return array


if __name__ == '__main__':
    print ''
    print 'rotate array'
    print rotate([1, 2, 3, 4, 5, 6, 7], 2)


"""
msft

http://www.geeksforgeeks.org/count-frequencies-elements-array-o1-extra-space-time/
"""


def find_counts_without_extra_space(array):
    i = 0
    n = len(array)

    while i < n:
        if array[i] <= 0:
            i += 1
            continue

        element_index = array[i] - 1

        if array[element_index] > 0:
            array[i] = array[element_index]
            array[element_index] = -1

        else:
            array[element_index] -= 1
            array[i] = 0
            i += 1

    for i in range(len(array)):
        print 'count of ' + str(i + 1) + ': ' + str(-array[i])


if __name__ == '__main__':
    print ''
    print 'counts without extra space'
    find_counts_without_extra_space([2, 3, 3, 2, 5])


"""
msft

https://leetcode.com/problems/simplify-path/#/solutions
"""


def simplify_linux_dir_path(path):
    places = [p for p in path.split("/") if p != "." and p != ""]
    s = Stack()

    for p in places:
        if p == ".." and not s.is_empty():
            s.pop()

        else:
            s.push(p)

    return "/" + '/'.join(s.get_list())


if __name__ == '__main__':
    print ''
    print 'Simplify linux path'
    print simplify_linux_dir_path('/a/./b/../../c/')


"""
msft

http://www.geeksforgeeks.org/majority-element/
"""


def get_majority_element(array):
    maj_idx = 0
    count = 1

    for i in range(len(array)):
        if array[maj_idx] == array[i]:
            count += 1
        else:
            count -= 1

        if count == 0:
            maj_idx = i
            count = 1

    return array[maj_idx]


def find_majority_element(array):
    idx = get_majority_element(array)
    el = array[idx]
    cnt = 0
    n = len(array)

    for i in range(n):
        if array[i] == el:
            cnt += 1

    if cnt > n // 2:
        return el

    return None


if __name__ == '__main__':
    print ''
    print 'majority element'
    print find_majority_element([1, 3, 3, 1, 2])
    print find_majority_element([3, 3, 4, 2, 4, 4, 2, 4, 4])


"""
amzn msft

Find pivoted entry in sorted rotated array
"""


def pivoted_element(array, l, h):
    if l > h:
        return -1

    if l == h:
        return l

    mid = (l + h) // 2

    if mid < h and array[mid] > array[mid + 1]:
        return mid

    if mid > l and array[mid - 1] > array[mid]:
        return mid - 1

    if array[l] <= array[mid]:
        return pivoted_element(array, mid + 1, h)

    return pivoted_element(array, l, mid - 1)


if __name__ == '__main__':
    print ''
    print 'Search for pivot element'
    print pivoted_element([5, 6, 7, 8, 9, 10, 1, 2, 3], 0, 8)
    print pivoted_element([30, 40, 50, 10, 20], 0, 4)
    print pivoted_element([1, 2, 3, 4, 5], 0, 4)


"""
amzn

http://www.geeksforgeeks.org/find-index-first-1-sorted-array-0s-1s/

Input : arr[] = {0, 0, 0, 0, 0, 0, 1, 1, 1, 1}
Output : 6
The index of first 1 in the array is 6.
"""


def first_index(array, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if array[mid] == 1 and (mid == 0 or array[mid - 1] == 0):
        return mid

    if array[mid] == 1:
        return first_index(array, start, mid - 1)

    return first_index(array, mid + 1, end)


if __name__ == '__main__':
    print ''
    print 'Find the index of first 1 in a sorted array of 0’s and 1’s'
    print first_index([0, 0, 0, 0, 0, 0, 1, 1, 1, 1], 0, 9)


"""
amzn

Given 2 array of size m , n , find the pairs with minimum difference
"""


def get_min_diff_pair(array1, array2):
    min_diff = maxint
    i = j = 0
    m = len(array1)
    n = len(array2)

    while i < m and j < n:
        diff = abs(array1[i] - array2[j])

        min_diff = min(
            min_diff,
            diff
        )

        if array1[i] < array2[j]:
            i += 1

        else:
            j += 1

    return min_diff


if __name__ == '__main__':
    print ''
    print 'min diff pair in 2 arrays'
    print get_min_diff_pair(
        [1, 3, 4, 5, 6],
        [9, 10, 11]
    )




