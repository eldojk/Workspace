"""
http://www.geeksforgeeks.org/largest-rectangle-under-histogram/

"""
from G4G.Problems.stacks.stack import Stack


def find_largest_area(hist):
    s = Stack()
    n = len(hist)

    max_area = 0

    i = 0
    while i < n:

        # Push as long as stack top is smaller
        if s.is_empty() or hist[s.peek()] <= hist[i]:
            s.push(i)
            i += 1

        else:
            # pop one by one and calculate area considering, the popped
            # elements height as the smallest. notice we are not
            # incrementing i here. Hence we keep popping until we find
            # a smaller height
            s_top = s.pop()

            # width is from top to i, but not including i
            width = i if s.is_empty() else i - s.peek() - 1
            area_with_top_as_smallest = hist[s_top] * width

            if max_area < area_with_top_as_smallest:
                max_area = area_with_top_as_smallest

    # pop entire stack to consider all elements
    while not s.is_empty():

        s_top = s.pop()

        # here i is N, so width will be from top to N, not
        # including N
        width = i if s.is_empty() else i - s.peek() - 1
        area_with_top_as_smallest = hist[s_top] * width

        if max_area < area_with_top_as_smallest:
            max_area = area_with_top_as_smallest

    return max_area


if __name__ == '__main__':
    print find_largest_area([6, 2, 5, 4, 5, 1, 6])
    print find_largest_area([2, 1, 2, 3, 1])