"""
amzn

Given arrival and departure times of all trains that reach a railway station, find the minimum number of platforms
required for the railway station so that no train waits.
We are given two arrays which represent arrival and departure times of trains that stop

Examples:

Input:  arr[]  = {9:00,  9:40, 9:50,  11:00, 15:00, 18:00}
        dep[]  = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
Output: 3
There are at-most three trains at a time (time between 11:00 to 11:20)

http://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/
ASSUMING TIMES DON'T OVERFLOW TO NEXT DAY
"""


def get_min_trains(arrivals, departures):
    arrivals.sort()
    departures.sort()
    n = len(arrivals)
    i = 0
    j = 0

    max_required = 0
    currently_required = 0

    while i < n and j < n:
        if arrivals[i] < departures[j]:
            currently_required += 1
            max_required = currently_required if currently_required > max_required else max_required
            i += 1
        elif departures[j] < arrivals[i]:
            currently_required -= 1
            j += 1
        else:
            i += 1
            j += 1

    return max_required


if __name__ == '__main__':
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]

    print get_min_trains(arr, dep)
