"""
Sort a stack recursively
Do not use loops

Pop out all elements and do a sorted insert on to the stack
Link: http://www.geeksforgeeks.org/sort-a-stack-using-recursion/
"""


def sort_stack(s):
    """
    Pop out all elements and do a sorted insert on to the stack

    :param s:
    :return:
    """
    if not s.is_empty():
        element = s.pop()
        sort_stack(s)
        sorted_insert(s, element)

    return s


def sorted_insert(s, element):
    """
    Sorted Insert

    :param s:
    :param element:
    :return:
    """
    if s.is_empty() or element > s.peek():
        s.push(element)
    else:
        # pop until a push-able condition comes, push it,
        # then push the popped elements
        top = s.pop()
        sorted_insert(s, element)
        s.push(top)
