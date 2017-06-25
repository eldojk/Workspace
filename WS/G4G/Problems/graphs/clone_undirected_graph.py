"""
amzn

http://www.geeksforgeeks.org/clone-an-undirected-graph/
"""
from Queue import Queue


class Node(object):
    pass


def clone_graph(source):
    q = Queue()
    q.put(source)
    hm = {}
    hm[source] = Node(source.data)

    while not q.empty():
        node = q.get()
        clone_node = hm.get(node)

        if len(node.neighbours) != 0:
            for neighbour in node.neighbours:

                clone_neighbour = hm.get(neighbour)

                if clone_neighbour is None:
                    q.add(neighbour)

                    clone_neighbour = Node(neighbour.data)
                    hm.put(neighbour, clone_neighbour)

                clone_node.neighbours.append(clone_neighbour)

    return hm[source]
