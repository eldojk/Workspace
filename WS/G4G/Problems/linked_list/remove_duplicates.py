"""
Remove duplicates from ll
CTIC 184, #2.1
"""

def remove_duplicates(node):
    datas = {}
    start = node
    prev = None

    while node is not None:
        # first node does not go into this if statement
        if datas.get(node.data):
            prev.nxt = node.nxt
        else:
            datas[node.data] = 1
            prev = node

        node = node.nxt

    return start
