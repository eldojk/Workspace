"""
https://www8.cs.umu.se/kurser/TDBAfl/VT06/algorithms/BOOK/BOOK4/NODE156.HTM

Minimum completion time - assuming that we have an unlimited number of workers,
what is the fastest we can get this job completed while respecting precedence
constraints. If there were no precedence constraints, each task could be worked on
by its own worker, and the total time would be that of the longest single task.
If there were such strict precedence constraints that each task had to follow the
completion of its immediate predecessor, the minimum completion time would be
obtained by summing up the times for each task. The minimum completion time
for a DAG can be easily computed in O(n+m) time. Initialize the completion time
for all the vertices to 0, except the start vertex, which is initialized to the
length of the start task. Perform a topological sort to order the vertices such
that all precedences will have been considered by the time we evaluate each vertex.
For each vertex u, consider all the edges (u,v) leaving u. The completion time of
these vertices is the maximum of the current completion time for v plus the
completion time of u plus the task time of v.
"""
from Queue import Queue


class MinTimeJobScheduling(object):
    def __init__(self, jobs, times):
        self.jobs = jobs
        self.times = times
        self.completion_times = self.times
        self.max_completion_time = 0
        self.visited = [False for i in self.jobs.keys()]

    def topological_queue(self, source, q):
        self.visited[source] = True

        for neighbour in self.jobs[source]:
            if not self.visited[neighbour]:
                self.dfs(neighbour)

        q.put(source)

    def get_max_time(self):
        q = Queue()

        for v in self.jobs.keys():
            if not self.visited[v]:
                self.topological_queue(v, q)

        while not q.empty():
            el = q.get()

            for neighbour in self.jobs[el]:
                self.completion_times[el] = max(
                    self.completion_times[el],
                    self.completion_times[neighbour] + self.times[el]
                )

        return max(self.completion_times)
