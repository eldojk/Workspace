"""
amzn, msft

http://www.geeksforgeeks.org/find-first-non-repeating-character-stream-characters/

1) Create an empty DLL. Also create two arrays inDLL[] and repeated[] of size 256.
   inDLL is an array of pointers to DLL nodes. repeated[] is a boolean array,
   repeated[x] is true if x is repeated two or more times, otherwise false.
   inDLL[x] contains pointer to a DLL node if character x is present in DLL,
   otherwise NULL.

2) Initialize all entries of inDLL[] as NULL and repeated[] as false.

3) To get the first non-repeating character, return character at head of DLL.

4) Following are steps to process a new character 'x' in stream.
  a) If repeated[x] is true, ignore this character (x is already repeated two
      or more times in the stream)
  b) If repeated[x] is false and inDLL[x] is NULL (x is seen first time)
     Append x to DLL and store address of new DLL node in inDLL[x].
  c) If repeated[x] is false and inDLL[x] is not NULL (x is seen second time)
     Get DLL node of x using inDLL[x] and remove the node. Also, mark inDLL[x]
     as NULL and repeated[x] as true.
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


def delete_dll_node(node, head, tail):
    if head == node:
        if node.right:
            node.right.left = None

        return node.right, tail

    elif tail == node:
        node.left.right = None

        return head, node.left

    else:
        node.left.right = node.right
        node.right.left = node.left

        return head, tail


def first_non_repeating_char(stream):
    head = None
    tail = None
    in_dll = [None for i in range(26)]
    repeated = [False for i in range(26)]

    for c in stream:
        idx = ord(c) - ord('a')

        if in_dll[idx] is None and not repeated[idx]:
            # first occurrence
            node = Node(c)
            in_dll[idx] = node

            if head:
                tail.right = node
                node.left = tail
                tail = node

            else:
                head = node
                tail = head

        elif in_dll[idx]:
            node = in_dll[idx]

            # remove
            head, tail = delete_dll_node(node, head, tail)
            in_dll[idx] = None
            repeated[idx] = True

        print head


if __name__ == '__main__':
    first_non_repeating_char('geeksforgeeksandgeeksquizfor')