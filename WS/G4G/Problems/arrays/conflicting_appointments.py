"""
amzn, msft

http://www.geeksforgeeks.org/given-n-appointments-find-conflicting-appointments/
https://www.careercup.com/question?id=11515910

worst algorithm is n2. If you sort by start times (nlogn)
then for each app(current app), do a binary search to find
the largest start time (last conflicting app) which is less
than current apps end time. All the apps between current app
and last conflicting app is conflicting. so nlogn+nlogn
"""


class Appointment(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.start < other.start

    def __gt__(self, other):
        return self.start > other.start

    def __eq__(self, other):
        return self.start == other.start

    def __repr__(self):
        return str(self.start) + ' - ' + str(self.end)


def search_floor_start_time(array, i, j, time):
    if i > j:
        return -1

    if array[j].start <= time:
        return j

    if i == j:
        return i

    mid = (i + j) // 2

    if array[mid].start <= time < array[mid + 1].start:
        return mid

    if array[mid].start < time:
        return search_floor_start_time(array, mid + 1, j, time)

    return search_floor_start_time(array, i, mid - 1, time)


def find_conflicting_appointments(appointments):
    appointments.sort()
    n = len(appointments)

    for i in range(n):
        app = appointments[i]
        time = app.end
        f_index = search_floor_start_time(appointments, i, n - 1, time)

        if appointments[f_index].start == time:
            # even in this case, there are no conflicts
            f_index -= 1

        if f_index > i:
            for j in range(i + 1, f_index + 1):
                print appointments[i], 'and', appointments[j]


if __name__ == '__main__':
    _app = [Appointment(1, 5), Appointment(3, 7), Appointment(2, 6),
            Appointment(10, 15), Appointment(5, 6), Appointment(4, 100)]

    find_conflicting_appointments(_app)
