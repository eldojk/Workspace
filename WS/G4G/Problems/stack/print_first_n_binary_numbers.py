from Queue import Queue


def print_binary_nums(n):
    q = Queue()
    q.put('1')

    while n > 0:
        num = q.get()
        print num

        q.put('{0}{1}'.format(num, 0))
        q.put('{0}{1}'.format(num, 1))
        n -= 1


print_binary_nums(10)
