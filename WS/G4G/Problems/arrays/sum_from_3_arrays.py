"""
amzn

http://stackoverflow.com/questions/3987264/interview-question-three-arrays-and-onn

Assume we have three arrays of length N which contain arbitrary numbers of type long.
Then we are given a number M (of the same type) and our mission is to pick three numbers
A, B and C one from each array (in other words A should be picked from first array,
B from second one and C from third) so the sum A + B + C = M.
"""
from G4G.Problems.arrays.sum_pair_from_two_sorted_arrays import find_sum_pair


def sum_from_three_arrays(a, b, c, _sum):
    a.sort()
    b.sort()

    for num in c:
        result = find_sum_pair(a, b, _sum - num)
        if result:
            return result[0], result[1], num

    return 'Not found'


if __name__ == '__main__':
    print sum_from_three_arrays(
        [6, 5, 8, 3, 9, 2],
        [1, 9, 0, 4, 6, 4],
        [7, 8, 1, 5, 4, 3],
        19
    )