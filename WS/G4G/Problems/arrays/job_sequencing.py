"""
http://www.geeksforgeeks.org/job-sequencing-problem-set-1-greedy-algorithm/

Given an array of jobs where every job has a deadline and associated profit if the job is finished before
the deadline.
It is also given that every job takes single unit of time, so the minimum possible
deadline for any job is 1. How to maximize total profit if only one job can be scheduled at a time.
"""


class Job(object):
    def __init__(self, name, deadline, profit):
        self.name = name
        self.deadline = deadline
        self.profit = profit

    def __lt__(self, other):
        return self.profit < other.profit

    def __eq__(self, other):
        return self.profit == other.profit

    def __gt__(self, other):
        return self.profit > other.profit

    def __repr__(self):
        return self.name


def schedule(jobs, n):
    result = [None for i in range(n)]
    slot = [False for i in range(n)]

    jobs.sort()
    jobs.reverse()

    for i in range(len(jobs)):

        job = jobs[i]
        deadline = job.deadline
        j = min(n, deadline) - 1

        while j >= 0:
            if not slot[j]:
                result[j] = jobs[i]
                slot[j] = True
                break
            j -= 1

    return result


if __name__ == '__main__':
    j = [Job('a', 2, 100), Job('b', 1, 19), Job('c', 2, 27), Job('d', 1, 25), Job('e', 3, 15)]
    print schedule(j, 3)