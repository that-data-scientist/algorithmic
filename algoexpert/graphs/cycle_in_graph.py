# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest


# Time complexity - O(v+e)
# Space complexity - O(v)
def cycleInGraph(edges):
    for node in range(len(edges)):
        cycle_status = dfsUtil(edges, node, [])

        if cycle_status:
            return cycle_status

    return False


def dfsUtil(edges, node, visited):
    if node in visited:
        return True

    visited.append(node)

    for dest_node in edges[node]:
        cycle_found = dfsUtil(edges, dest_node, visited)
        if cycle_found:
            return cycle_found

    visited.remove(node)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]
        expected = True
        actual = cycleInGraph(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = [[1, 2], [2], []]
        expected = False
        actual = cycleInGraph(input)
        self.assertEqual(actual, expected)
