"""
http://www.geeksforgeeks.org/count-distinct-elements-in-every-window-of-size-k/
"""


def count_dist(array, k):
    dist_count = 0
    hm = {}

    dist_count, hm = add_first_element(array, dist_count, hm, k)

    print dist_count

    i = 1
    j = k

    while j < len(array):
        el_to_rem = array[i - 1]
        el_to_add = array[j]
        dist_count, hm = add_element(dist_count, hm, el_to_add)
        dist_count, hm = remove_element(dist_count, hm, el_to_rem)

        print dist_count, hm

        i += 1
        j += 1


def add_first_element(array, dist_count, hm, k):
    for i in range(k):
        el = array[i]

        if hm.get(el):
            hm[el] += 1
        else:
            hm[el] = 1
            dist_count += 1

    return dist_count, hm


def add_element(dist_count, hm, el):
    if hm.get(el):
        hm[el] += 1
    else:
        hm[el] = 1
        return dist_count + 1, hm

    return dist_count, hm


def remove_element(dist_count, hm, el):
    if hm.get(el) > 1:
        hm[el] -= 1
    else:
        del hm[el]
        return dist_count - 1, hm

    return dist_count, hm


if __name__ == '__main__':
    count_dist([1, 2, 1, 3, 4, 2, 3], 4)
