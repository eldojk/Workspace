"""
Given certain jobs with start and end time and amount you make on finishing the job,
find the maximum value you can make by scheduling jobs in non-overlapping way.

Jobs can be done serially only, hence maximize the value

https://www.youtube.com/watch?v=cr6Ip0J9izc - tushar roy
"""


class Job:
    def __init__(self, st, end, val):
        self.start = st
        self.end = end
        self.profit = val
        self.time_range = range(self.start, self.end)

    def is_overlapping(self, other):
        return any(i in other.time_range for i in self.time_range)

    def __repr__(self):
        return "{0} - {1} : {2}".format(str(self.start), str(self.end), str(self.profit))


def maximum_value(jobs):
    """
    Jobs are sorted based on finish time. this is important
    We can't schedule job1 before job2 if job1's finish time is
    after job2
    So when we consider a job we want to find all jobs that finishes
    before this one does

    :param jobs:
    :return:
    """
    values = [j.profit for j in jobs]

    for i in range(1, len(jobs)):
        for j in range(i):
            job_i = jobs[i]
            job_j = jobs[j]

            if not job_i.is_overlapping(job_j):
                # value of doing ith job last =
                # value of doing ith job after j -> values[j] + job_i.profit or
                # just doing that ith job alone (if j overlaps)
                values[i] = max(values[i], values[j] + job_i.profit)

    return max(values)


if __name__ == '__main__':
    jbs = [Job(1, 3, 5), Job(2, 5, 6), Job(4, 6, 5), Job(6, 7, 4), Job(5, 8, 11), Job(7, 9, 2)]
    print maximum_value(jbs)
    jbs = [Job(1, 2, 50), Job(3, 5, 20), Job(6, 19, 100), Job(2, 100, 200)]
    print maximum_value(jbs)