# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest


def riverSizes(matrix):
    array = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                # island_length = dfs_util_correct(matrix, i, j)
                island_length = dfs_util_v2(matrix, i, j)

                if island_length > 0:
                    array.append(island_length)

    return array


def dfs_util_correct(matrix, i, j):
    if i >= len(matrix) or j >= len(matrix[0]) or i < 0 or j < 0:
        return 0

    if matrix[i][j] == 0:
        return 0

    matrix[i][j] = 0

    return 1 + (
            dfs_util_correct(matrix, i + 1, j) +
            dfs_util_correct(matrix, i - 1, j) +
            dfs_util_correct(matrix, i, j + 1) +
            dfs_util_correct(matrix, i, j - 1)
    )


def dfs_util_v2(matrix, i, j):
    if matrix[i][j] == 0:
        return 0

    matrix[i][j] = 0
    size = 1

    if (j < len(matrix[0]) - 1) and (matrix[i][j + 1] == 1):
        size += dfs_util_v2(matrix, i, j + 1)
    if (j > 0) and matrix[i][j - 1] == 1:
        size += dfs_util_v2(matrix, i, j - 1)
    if (i < len(matrix) - 1) and (matrix[i + 1][j] == 1):
        size += dfs_util_v2(matrix, i + 1, j)
    if (i > 0) and (matrix[i - 1][j] == 1):
        size += dfs_util_v2(matrix, i - 1, j)

    return size


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        testInput = [
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0]
        ]
        expected = [1, 2, 2, 2, 5]
        self.assertEqual(sorted(riverSizes(testInput)), expected)

    def test_case_2(self):
        testInput = [
            [0]
        ]
        expected = []
        self.assertEqual(sorted(riverSizes(testInput)), expected)

    def test_case_3(self):
        testInput = [
            [1]
        ]
        expected = [1]
        self.assertEqual(sorted(riverSizes(testInput)), expected)

    def test_case_4(self):
        testInput = [
            [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
            [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]
        ]

        expected = [1, 1, 2, 2, 5, 21]
        self.assertEqual(sorted(riverSizes(testInput)), expected)
