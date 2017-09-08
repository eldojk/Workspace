"""
amzn

http://www.geeksforgeeks.org/sort-numbers-stored-on-different-machines/
"""
from DS.algos.binary_heap.priority_queue import MIN_PQ, PriorityQueue
from G4G.Problems.binary_heap.smallest_range_in_3_lists import Element


def print_sorted(array):
    k = len(array)
    min_pq = PriorityQueue(k, MIN_PQ)

    for i in range(k):
        min_pq.insert(Element(array[i][0], 0, i))

    while True:
        if min_pq.is_empty():
            break

        element = min_pq.delete_top()

        if element is None:
            print min_pq.N

        print element,

        nxt_array = element.array
        nxt_index = element.index + 1

        if nxt_index == len(array[nxt_array]):
            continue

        nxt_el = array[nxt_array][nxt_index]

        min_pq.insert(Element(nxt_el, nxt_index, nxt_array))


if __name__ == '__main__':
    print_sorted([[30, 40, 50], [35, 45], [10, 60, 70, 80, 100]])