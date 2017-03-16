"""
http://www.geeksforgeeks.org/given-an-array-of-pairs-find-all-symmetric-pairs-in-it/
"""
from DS.algos.math.factorial import iterative_factorial


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
        elif product % el == 0 and hm.get(product/el):
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
http://www.geeksforgeeks.org/count-maximum-points-on-same-line/
"""
from fractions import gcd
def compute_slope(p1, p2):
    s = (p2[1] - p1[1], p2[0] - p1[0])
    g = gcd(s[0], s[1])
    s = (s[0]/g, s[1]/g)
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
        if i%2 == 0:
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
    nm2f = iterative_factorial(n-2)

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