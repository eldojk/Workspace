"""
http://www.geeksforgeeks.org/count-possible-ways-to-construct-buildings/

Given an input number of sections and each section has 2 plots on either sides of the road. Find all possible ways to
construct buildings in the plots such that there is a space between any 2 buildings.

Let countB(i) be count of possible ways with i sections
              ending with a building.
    countS(i) be count of possible ways with i sections
              ending with a space.

// A space can be added after a building or after a space.
countS(N) = countB(N-1) + countS(N-1)

// A building can only be added after a space.
countB[N] = countS(N-1)

// Result for one side is sum of the above two counts.
result1(N) = countS(N) + countB(N)

// Result for two sides is square of result1(N)
result2(N) = result1(N) * result1(N)
"""


def get_building_construction_ways(n):
    if n == 1:
        return 4

    countS = [0 for i in range(n + 1)]
    countB = [0 for i in range(n + 1)]
    result = [0 for i in range(n + 1)]

    countB[1] = 1
    countS[1] = 1

    for i in range(2, n + 1):

        countS[i] = countS[i - 1] + countB[i - 1]
        countB[i] = countS[i - 1]
        result[i] = countB[i] + countS[i]

    return result[n] ** 2


if __name__ == '__main__':
    print get_building_construction_ways(4)