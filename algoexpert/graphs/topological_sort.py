# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest


def topologicalSort(jobs, deps):
    no_prereqs = []
    prereq_graph = {}

    for job in jobs:
        no_prereqs.append(job)

    for pre_req, job in deps:
        if job not in prereq_graph.keys():
            prereq_graph[job] = []

        prereq_graph[job].append(pre_req)

        if job in no_prereqs:
            no_prereqs.remove(job)

    visited = []

    while len(no_prereqs) != 0:
        node = no_prereqs.pop()

        if node in visited:
            return []

        visited.append(node)

        for job, pre_reqs in prereq_graph.items():
            if node in pre_reqs:
                pre_reqs.remove(node)
                if len(pre_reqs) == 0:
                    no_prereqs.append(job)

    if len(visited) == len(jobs):
        return visited

    return []


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        jobs = [1, 2, 3, 4]
        deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
        order = topologicalSort(jobs, deps)
        self.assertEqual(isValidTopologicalOrder(order, jobs, deps), True)

    def test_case_2(self):
        jobs = [1, 2, 3, 4, 5, 6, 7, 8]
        deps = [[3, 1], [8, 1], [8, 7], [5, 7], [5, 2], [1, 4], [1, 6], [1, 2], [7, 6]]
        order = topologicalSort(jobs, deps)
        self.assertEqual(isValidTopologicalOrder(order, jobs, deps), True)


def isValidTopologicalOrder(order, jobs, deps):
    visited = {}
    for candidate in order:
        for prereq, job in deps:
            if candidate == prereq and job in visited:
                return False
        visited[candidate] = True
    for job in jobs:
        if job not in visited:
            return False
    return len(order) == len(jobs)
