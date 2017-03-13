"""
http://www.geeksforgeeks.org/find-height-binary-tree-represented-parent-array/

wow me !!!
"""


def find_depths(parent_array, depths, index):
    if parent_array[index] == -1:
        depths[index] = 1
        return 1

    if depths[index] != -1:
        return depths[index]

    depths[index] = 1 + find_depths(parent_array, depths, parent_array[index])
    return depths[index]


def find_max_depth(parent_array):
    depths = [-1 for i in parent_array]

    for i in range(len(parent_array)):
        if depths[i] == -1:
            find_depths(parent_array, depths, i)

    print depths
    return max(depths)


if __name__ == '__main__':
    print find_max_depth([1, 5, 5, 2, 2, -1, 3])
    print find_max_depth([-1, 0, 0, 1, 1, 3, 5])
