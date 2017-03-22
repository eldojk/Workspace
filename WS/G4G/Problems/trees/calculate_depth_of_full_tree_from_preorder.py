"""
http://www.geeksforgeeks.org/calculate-depth-full-binary-tree-preorder/

Input  : nlnll
Output : 3
"""

INDEX = 0


def calc_depth(pre_order, n):
    global INDEX
    if INDEX >= n or pre_order[INDEX] == 'l':
        return 1

    INDEX += 1
    left_height = calc_depth(pre_order, n)

    INDEX += 1
    right_height = calc_depth(pre_order, n)

    return max(left_height, right_height) + 1


if __name__ == '__main__':
    print calc_depth('nlnll', 5)
    INDEX = 0
    print calc_depth('nlnnlll', 7)