# coding=utf-8
"""
http://www.geeksforgeeks.org/dynamic-programming-set-21-box-stacking-problem/

https://www.youtube.com/watch?v=9mod_xRB-O0 tushar ( this code is giving different output. tushar may be wrong in
finding box combinations)

The Box Stacking problem is a variation of LIS problem. We need to build a maximum height stack.

Following are the key points to note in the problem statement:
1) A box can be placed on top of another box only if both width and depth of the upper placed box are smaller than width
 nd depth of the lower box respectively.
2) We can rotate boxes. For example, if there is a box with dimensions {1x2x3} where 1 is height, 2×3 is base, then
there can be three possibilities, {1x2x3}, {2x1x3} and {3x1x2}.
3) We can use multiple instances of boxes. What it means is, we can have two different rotations of a box as part of
our maximum height stack.

Following is the solution based on DP solution of LIS problem.

1) Generate all 3 rotations of all boxes. The size of rotation array becomes
3 times the size of original array.
For simplicity, we consider depth as always smaller than or equal to width.

2) Sort the above generated 3n boxes in decreasing order of base area.

3) After sorting the boxes, the problem is same as LIS with following optimal substructure property.
MSH(i) = Maximum possible Stack Height with box i at top of stack
MSH(i) = { Max ( MSH(j) ) + height(i) } where j < i and width(j) > width(i) and depth(j) > depth(i).
If there is no such j then MSH(i) = height(i)

4) To get overall maximum height, we return max(MSH(i)) where 0 < i < n
"""


def get_permutations(box):
    """
    2 1 4
    4 1 2
    4 2 1
    :param box:
    :return:
    """
    l = box[0]
    w = box[1]
    h = box[2]

    rot1 = [0, 0, 0]
    rot2 = [0, 0, 0]

    rot1[2] = w
    rot1[0] = max(l, h)
    rot1[1] = min(l, h)

    rot2[2] = l
    rot2[0] = max(w, h)
    rot2[1] = min(w, h)

    return [box, tuple(rot1), tuple(rot2)]


def comparator(box1, box2):
    ba1 = box1[0] * box1[1]
    ba2 = box2[0] * box2[1]

    if ba1 < ba2:
        return -1
    elif ba1 > ba2:
        return 1
    else:
        return 0


def can_go_on_top(bottom_box, top_box):
    return bottom_box[0] > top_box[0] and bottom_box[1] > top_box[1]


def stack_boxes(boxes):
    box_combinations = []
    for box in boxes:
        box_combinations.extend(get_permutations(box))

    # sorting based on base area decreasing order
    box_combinations.sort(cmp=comparator, reverse=True)

    max_heights = [box[2] for box in box_combinations]
    result = [i for i in range(len(box_combinations))]

    for i in range(len(box_combinations)):
        for j in range(i):

            height_of_i = box_combinations[i][2]
            if can_go_on_top(box_combinations[j], box_combinations[i]) \
                    and max_heights[i] < max_heights[j] + height_of_i:

                max_heights[i] = max_heights[j] + height_of_i
                result[i] = j

    # find max height index
    max_height_idx = 0
    for i in range(len(max_heights)):
        if max_heights[max_height_idx] < max_heights[i]:
            max_height_idx = i

    # print stacking
    i = max_height_idx
    while i != result[i]:
        print box_combinations[i]
        i = result[i]

    print box_combinations[i]


if __name__ == '__main__':
    stack_boxes([(1, 2, 4), (3, 2, 5)])
