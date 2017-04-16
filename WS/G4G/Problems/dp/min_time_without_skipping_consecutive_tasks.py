# coding=utf-8
"""
http://www.geeksforgeeks.org/minimum-time-to-finish-tasks-without-skipping-two-consecutive/

The given problem has the following recursive property.

Let minTime(i) be minimum time to finish till i’th task. It can be written as minimum of two values.

Minimum time if i’th task is included in list, let this time be incl(i)
Minimum time if i’th task is excluded from result, let this time be excl(i)
minTime(i) = min(excl(i), incl(i))
Result is minTime(n-1) if there are n tasks and indexes start from 0.

incl(i) can be written as below.

// There are two possibilities
// (a) Previous task is also included
// (b) Previous task is not included
incl(i) = min(incl(i-1), excl(i-1)) +
              arr[i] // Since this is inclusive
                     // arr[i] must be included
excl(i) can be written as below.


// There is only one possibility (Previous task must be
// included as we can't skip consecutive tasks.
excl(i) = incl(i-1)
"""


def min_time(tasks):

    incl = tasks[0]
    excl = 0

    for i in range(1, len(tasks)):
        incl_this = tasks[i] + min(
            incl,
            excl
        )

        excl_this = incl

        incl = incl_this
        excl = excl_this

    return min(incl, excl)


if __name__ == '__main__':
    print min_time([10, 5, 2, 7, 10])


