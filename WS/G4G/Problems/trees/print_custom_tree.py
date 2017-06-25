"""
http://www.geeksforgeeks.org/custom-tree-problem/
"""
# todo fix


def print_tree(links, char, prefix):
    print prefix, char

    if links.get(char) is None:
        return

    for neighbour in links[char]:
        print_tree(links, neighbour, prefix + '_ _ ')


if __name__ == '__main__':
    _links = {
        'a': ['b', 'e'],
        'b': ['c', 'd']
    }

    print_tree(_links, 'a', '_ _ ')