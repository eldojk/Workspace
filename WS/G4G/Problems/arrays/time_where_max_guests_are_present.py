"""
amzn

http://www.geeksforgeeks.org/find-the-point-where-maximum-intervals-overlap/
"""


def find_maximum_guests_time(arrival, exit):
    arrival.sort()
    exit.sort()

    n = len(arrival)
    i = 0
    j = 0
    max_guests = 0
    guests = 0
    mg_time = 0
    time = 0

    while i < n and j < n:

        if arrival[i] <= exit[j]:
            guests += 1
            time = arrival[i]
            i += 1

        elif exit[j] < arrival[i]:
            guests -= 1
            time = exit[j]
            j += 1

        if guests > max_guests:
            max_guests = guests
            mg_time = time

    # print max_guests
    return mg_time


if __name__ == '__main__':
    print find_maximum_guests_time([1, 2, 10, 5, 5], [4, 5, 12, 9, 12])