from G4G.Problems.stacks.stack import Stack


def get_next_minimum(array):
    stack = Stack()

    for i in range(len(array)):
        while not stack.is_empty() and stack.peek() < array[i]:
            el = stack.peek()
            if array[i] > el:
                stack.pop()
                print '{0} : {1}'.format(el, array[i])

        stack.push(array[i])

    while not stack.is_empty():
        print '{0} : {1}'.format(stack.pop(), '-1')

# get_next_minimum([40,50,11,32,55,68,75])
