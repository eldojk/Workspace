"""
amzn

http://www.geeksforgeeks.org/serialize-deserialize-n-ary-tree/
"""


class NNode(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def __repr__(self):
        return str(self.data)


def serialize_n_nary_tree(root):
    child_serialization = ''

    for child in root.children:
        child_serialization += serialize_n_nary_tree(child)

    return root.data + child_serialization + ')'


SERIAL_STRING_INDEX = 0


def deserialize_nnary_tree(string, n):
    global SERIAL_STRING_INDEX

    # finished end or no more children
    if SERIAL_STRING_INDEX >= n or string[SERIAL_STRING_INDEX] == ')':
        return None

    val = string[SERIAL_STRING_INDEX]
    node = NNode(val)
    SERIAL_STRING_INDEX += 1

    children = []
    child = deserialize_nnary_tree(string, n)

    while child is not None:
        children.append(child)
        SERIAL_STRING_INDEX += 1
        child = deserialize_nnary_tree(string, n)

    node.children = children
    return node


if __name__ == '__main__':
    r = NNode('A')
    r.children = [NNode('B'), NNode('C'), NNode('D')]
    r.children[0].children = [NNode('E'), NNode('F')]
    r.children[0].children[1].children = [NNode('K')]
    r.children[2].children = [NNode('G'), NNode('H'), NNode('I'), NNode('J')]

    s = serialize_n_nary_tree(r)
    print s

    node = deserialize_nnary_tree(s, len(s))
    print node
    print serialize_n_nary_tree(node)