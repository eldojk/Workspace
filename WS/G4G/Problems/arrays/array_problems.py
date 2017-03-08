"""
http://www.geeksforgeeks.org/given-an-array-of-pairs-find-all-symmetric-pairs-in-it/
"""


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