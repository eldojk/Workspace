"""
Given certain jobs with start and end time and amount you make on finishing the job, find the maximum value you can make
by scheduling jobs in non-overlapping way.

Jobs can be done serially only, hence maximize the value
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
    values = [j.profit for j in jobs]

    for i in range(1, len(jobs)):
        for j in range(i):
            job_i = jobs[i]
            job_j = jobs[j]

            if not job_i.is_overlapping(job_j):
                values[i] = max(values[i], values[j] + job_i.profit)

    return max(values)
