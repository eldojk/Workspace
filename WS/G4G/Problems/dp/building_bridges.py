# coding=utf-8
"""
amzn, msft

http://www.geeksforgeeks.org/dynamic-programming-set-14-variations-of-lis/

Consider a 2-D map with a horizontal river passing through its center.
There are n cities on the southern bank with x-coordinates a(1) … a(n) and n cities
on the northern bank with x-coordinates b(1) … b(n). You want to connect as many
north-south pairs of cities as possible with bridges such that no two bridges cross.
When connecting cities, you can only connect city i on the northern bank to city
i on the southern bank.

8     1     4     3     5     2     6     7
<---- Cities on the other bank of river---->
--------------------------------------------
  <--------------- River--------------->
--------------------------------------------
1     2     3     4     5     6     7     8
<------- Cities on one bank of river------->
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