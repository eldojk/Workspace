"""
amzn, msft

more done down

#tricky
http://www.geeksforgeeks.org/find-four-elements-that-sum-to-a-given-value-set-2/

1) Create an auxiliary array aux[] and store sum of all possible pairs in aux[].
The size of aux[] will be n*(n-1)/2 where n is the size of A[].

2) Sort the auxiliary array aux[].

3) Now the problem reduces to find two elements in aux[] with sum equal to X.
"""


class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.sum = a + b

    def __lt__(self, other):
        return self.sum < other.sum

    def __gt__(self, other):
        return self.sum > other.sum

    def __eq__(self, other):
        return self.sum == other.sum


def no_common_present(p1, p2):
    if p1.a == p2.a or p1.b == p2.a or p1.a == p2.b or p1.b == p2.b:
        return False

    return True


def generate_pairs(array):
    pairs = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            pairs.append(Pair(array[i], array[j]))

    return pairs


def find_quadraples(array, k):
    pairs = generate_pairs(array)
    pairs.sort()

    i = 0
    j = len(pairs) - 1

    while i < j:
        p1 = pairs[i]
        p2 = pairs[j]

        if p1.sum + p2.sum < k:
            i += 1

        elif p1.sum + p2.sum > k:
            j -= 1

        else:
            if no_common_present(p1, p2):
                print p1.a, p1.b, p2.a, p2.b

            i += 1
            j -= 1


if __name__ == '__main__':
    find_quadraples([10, 20, 30, 40, 1, 2], 91)
    print ''
    find_quadraples([10, 2, 3, 4, 5, 7, 8], 23)
    # todo remove duplicates by keeping track of printed thingies


"""
amzn, msft
http://www.geeksforgeeks.org/find-four-numbers-with-sum-equal-to-given-sum/

Another solution with n3 complexity but less extra space
"""


def find_numbers(array, k):
    n = len(array)
    array.sort()

    for i in range(n - 3):
        for j in range(i + 1, n - 2):

            sm = k - (array[i] + array[j])

            l = j + 1
            r = n - 1

            while l < r:
                if array[l] + array[r] > sm:
                    r -= 1

                elif array[l] + array[r] < sm:
                    l += 1

                else:
                    print array[i], array[j], array[l], array[r]
                    l += 1
                    r -= 1


if __name__ == '__main__':
    print ''
    print 'method 2'
    find_numbers([10, 20, 30, 40, 1, 2], 91)
    print ''
    find_numbers([10, 2, 3, 4, 5, 7, 8], 23)
