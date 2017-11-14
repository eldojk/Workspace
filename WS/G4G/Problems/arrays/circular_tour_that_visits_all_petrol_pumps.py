"""
amzn, msft

#tricky
http://algorithmsandme.in/2017/01/find-first-circular-tour-visits-petrol-pumps/
http://www.geeksforgeeks.org/find-a-tour-that-visits-all-stations


{4, 6}, {6, 5}, {7, 3} and {4, 5}
{4, 5}, {6, 5}, {2, 4} and {6, 4}
"""


def tour(stations):

    total = 0
    available_petrol = 0
    start_pos = 0

    for i in range(len(stations)):
        delta = stations[i][0] - stations[i][1]

        if available_petrol >= 0:
            # we can go forward
            available_petrol += delta

        else:
            # ignore previous and start here
            available_petrol = delta
            start_pos = i

        total += delta

    return start_pos if total >= 0 else -1


if __name__ == '__main__':
    print tour([(4, 6), (6, 5), (7, 3), (4, 5)])
    print tour([(4, 5), (6, 5), (2, 4), (6, 4)])
