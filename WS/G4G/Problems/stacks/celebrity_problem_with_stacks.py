# coding=utf-8
"""
amzn msft

http://www.geeksforgeeks.org/the-celebrity-problem/

In a party of N people, only one person is known to everyone. Such a person may be present in the party,
if yes, (s)he doesn’t know anyone in the party. We can only ask questions like “does A know B? “.
Find the stranger (celebrity) in minimum number of questions.
"""


from G4G.Problems.stacks.stack import Stack


def does_a_know_b(a, b):
    pass


def find_celebrity(array):
    s = Stack()

    for ppl in array:
        s.push(ppl)

    a = s.pop()
    b = s.pop()

    while not s.is_empty():
        if does_a_know_b(a, b):
            a = s.pop()
        else:
            b = s.pop()

    c = None
    if does_a_know_b(a, b):
        c = b
    else:
        c = a

    for person in array:
        if does_a_know_b(c, person) or not does_a_know_b(person, c):
            return None

    return c

