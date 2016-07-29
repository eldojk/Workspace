def _in(key, low, high):
    return key >= low and key <= high


def _range_search(node, low, high, array):
    if node:
        if node.key >= low:
            _range_search(node.left, low, high, array)

        # TODO modify this to support comparator
        if _in(node.key, low, high):
            array.append(node.key)

        if node.key <= high:
            _range_search(node.right, low, high, array)


def range_search(bst, low, high):
    root = bst.root

    array = []
    _range_search(root, low, high, array)

    return array

