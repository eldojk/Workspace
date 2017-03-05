"""
http://www.geeksforgeeks.org/print-postorder-from-given-inorder-and-preorder-traversals/
"""

INDEX = 0


def search(array, root):
    for i in range(len(array)):
        if array[i] == root:
            return i

    return -1


def print_post_order(preorder, inorder, start, end):
    global INDEX

    if start > end:
        return

    root = preorder[INDEX]
    INDEX += 1
    idx = search(inorder, root)

    print_post_order(preorder, inorder, start, idx - 1)
    print_post_order(preorder, inorder, idx + 1, end)

    print root,


if __name__ == '__main__':
    print_post_order([1, 2, 4, 5, 3, 6], [4, 2, 5, 1, 3, 6], 0, 5)
