"""
amzn

http://www.geeksforgeeks.org/dynamic-programming-set-14-variations-of-lis/
"""


def max_bridges_that_can_be_build(cities, northern_cities):
    """
    max number of bridges is the length of longest increasing
    sub sequence among northern cities

    :param cities:
    :param northern_cities:
    :return:
    """
    lis = [1 for i in northern_cities]

    for i in range(len(northern_cities)):
        for j in range(i):

            if northern_cities[j] < northern_cities[i] and \
                            lis[i] < lis[j] + 1:

                lis[i] = lis[j] + 1

    return max(lis)


if __name__ == '__main__':
    print max_bridges_that_can_be_build(range(1, 9), [8, 1, 4, 3, 5, 2, 6, 7])