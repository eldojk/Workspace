"""
Remove duplicates from ll
CTIC 184, #2.1
"""


def remove_duplicates(node):
    data = {}
    start = node
    prev = None

    while node is not None:
        # first node does not go into this if statement
        if data.get(node.data):
            prev.nxt = node.nxt
        else:
            data[node.data] = 1
            prev = node

        node = node.nxt

    return start
