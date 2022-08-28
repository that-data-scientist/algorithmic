# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest


# Time Complexity - O(m*n)
# Space Complexity - O(m*n)
def removeIslands(matrix):
    for j in range(len(matrix[0])):
        dfsUtil(matrix, 0, j)

    for i in range(1, len(matrix)):
        dfsUtil(matrix, i, 0)

    for j in range(1, len(matrix[0])):
        dfsUtil(matrix, len(matrix) - 1, j)

    for i in range(1, len(matrix) - 1):
        dfsUtil(matrix, i, len(matrix[0]) - 1)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
            elif matrix[i][j] == 2:
                matrix[i][j] = 1

    return matrix


def dfsUtil(matrix, i, j):
    if i >= len(matrix) or j >= len(matrix[0]) or i < 0 or j < 0:
        return

    if matrix[i][j] != 1:
        return

    matrix[i][j] = 2

    dfsUtil(matrix, i + 1, j)
    dfsUtil(matrix, i - 1, j)
    dfsUtil(matrix, i, j + 1)
    dfsUtil(matrix, i, j - 1)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 1],
        ]
        expected = [
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1],
        ]
        actual = removeIslands(input)
        self.assertEqual(actual, expected)
