# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest
import collections


def twoEdgeConnectedGraph(edges):
    if len(edges) == 0:
        return True

    arrival_times = [-1 for _ in range(len(edges))]
    start_vertex = 0

    if find_minimum_arrival_time_of_ancestor(
            start_vertex, -1, 0, arrival_times, edges
    ) == -1:
        return False

    for time in arrival_times:
        if time == -1:
            return False

    return True


def find_minimum_arrival_time_of_ancestor(
        current_vertex, parent, current_time, arrival_times, edges
):
    arrival_times[current_vertex] = current_time

    min_arrival_time = current_time

    for neighbor in edges[current_vertex]:
        if arrival_times[neighbor] == -1:
            min_arrival_time = min(
                min_arrival_time,
                find_minimum_arrival_time_of_ancestor(
                    neighbor, current_vertex, current_time + 1, arrival_times, edges
                )
            )
        elif neighbor != parent:
            min_arrival_time = min(min_arrival_time, arrival_times[neighbor])

    if min_arrival_time == current_time and parent != -1:
        return -1

    return min_arrival_time


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[1, 2, 5], [0, 2], [0, 1, 3], [2, 4, 5], [3, 5], [0, 3, 4]]
        expected = True
        actual = twoEdgeConnectedGraph(input)
        self.assertEqual(actual, expected)
