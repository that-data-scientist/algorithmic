# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!
import math
import unittest


class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Time complexity - O(2 * wh)
# Space complexity - O(wh)
def minimumPassesOfMatrixV2(matrix):
    first_order_positives = []
    second_order_positives = []
    num_passes = 0
    num_negatives = 0
    num_conversions = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > 0:
                first_order_positives.append(Coordinates(i, j))

            if matrix[i][j] < 0:
                num_negatives += 1

    while len(first_order_positives) != 0:
        for coordinate in first_order_positives:
            num_conversions += check_neighbor(
                matrix, coordinate.x, coordinate.y + 1, second_order_positives
            )
            num_conversions += check_neighbor(
                matrix, coordinate.x, coordinate.y - 1, second_order_positives
            )
            num_conversions += check_neighbor(
                matrix, coordinate.x + 1, coordinate.y, second_order_positives
            )
            num_conversions += check_neighbor(
                matrix, coordinate.x - 1, coordinate.y, second_order_positives
            )

        first_order_positives = second_order_positives

        if len(second_order_positives) == 0:
            break

        num_passes += 1
        second_order_positives = []

    if num_conversions == num_negatives:
        return num_passes
    else:
        return -1


def check_neighbor(matrix, i, j, second_order_positives):
    if i >= len(matrix) or j >= len(matrix[0]) or i < 0 or j < 0:
        return 0

    if matrix[i][j] >= 0:
        return 0

    if matrix[i][j] < 0:
        matrix[i][j] *= -1
        second_order_positives.append(Coordinates(i, j))
        return 1


# Time complexity - O(mn * 4^d)
# Space complexity - O(mn)
def minimumPassesOfMatrixV1(matrix):
    max_distance = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < 0:
                visited = [
                    [False for _ in range(len(matrix[0]))] for _ in range(len(matrix))
                ]
                distance = dfsUtil(matrix, i, j, 0, visited)
                if distance == math.inf:
                    return -1

                max_distance = max(distance, max_distance)

    return max_distance


def dfsUtil(matrix, i, j, distance, visited):
    if i >= len(matrix) or j >= len(matrix[0]) or i < 0 or j < 0:
        return math.inf

    if visited[i][j] is True:
        return math.inf

    if matrix[i][j] > 0:
        return distance

    if matrix[i][j] == 0:
        return math.inf

    visited[i][j] = True

    min_distance = min(
        dfsUtil(matrix, i, j + 1, distance + 1, visited),
        dfsUtil(matrix, i, j - 1, distance + 1, visited),
        dfsUtil(matrix, i + 1, j, distance + 1, visited),
        dfsUtil(matrix, i - 1, j, distance + 1, visited),
    )

    visited[i][j] = False
    return min_distance


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [
            [0, -1, -3, 2, 0],
            [1, -2, -5, -1, -3],
            [3, 0, 0, -4, -1],
        ]
        expected = 3
        actual = minimumPassesOfMatrixV2(input)
        self.assertEqual(actual, expected)
