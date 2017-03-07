"""
http://www.geeksforgeeks.org/find-next-smaller-next-greater-array/

[4, 5, 2, 25]
"""
from G4G.Problems.stacks.stack import Stack


def nge(array):
    _nge = [-1 for i in array]
    s = Stack()

    for i in range(len(array)):
        element = array[i]

        while not s.is_empty() and element > array[s.peek()]:
            _nge[s.peek()] = i
            s.pop()

        s.push(i)

    return _nge


def nse(array):
    _nse = [-1 for i in array]
    s = Stack()

    for i in range(len(array)):
        element = array[i]

        while not s.is_empty() and element < array[s.peek()]:
            _nse[s.peek()] = i
            s.pop()

        s.push(i)

    return _nse


def get_next_smaller_of_next_greater_element(array):
    _nge = nge(array)
    _nse = nse(array)

    nse_of_nge = [-1 for i in array]

    for i in range(len(array)):
        # index of next grtr element
        nge_i = _nge[i]
        if nge_i != -1:
            # index of next smaller of the element
            idx = _nse[nge_i]

            # if it exists store the actual elements
            if idx != -1:
                nse_of_nge[i] = array[idx]

    return nse_of_nge


if __name__ == '__main__':
    print get_next_smaller_of_next_greater_element([5, 1, 9, 2, 5, 1, 7])
