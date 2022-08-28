# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest


def zigzagTraverse(array):
    num_rows = len(array)
    num_cols = len(array[0])

    traverse = []
    cur_row = 0
    cur_col = 0
    direction = "down"

    while (cur_row != num_rows - 1) or (cur_col != num_cols - 1):
        traverse.append(array[cur_row][cur_col])

        if direction == "down":
            if cur_row == num_rows - 1:
                new_row = cur_row
                new_col = cur_col + 1
                direction = 'up'
            elif cur_col == 0:
                new_row = cur_row + 1
                new_col = 0
                direction = 'up'
            else:
                new_row = cur_row + 1
                new_col = cur_col - 1
        else:
            if cur_col == num_cols - 1:
                new_row = cur_row + 1
                new_col = cur_col
                direction = 'down'
            elif cur_row == 0:
                new_row = cur_row
                new_col = cur_col + 1
                direction = 'down'
            else:
                new_row = cur_row - 1
                new_col = cur_col + 1

        cur_row = new_row
        cur_col = new_col

    traverse.append(array[num_rows - 1][num_cols - 1])
    return traverse


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
        self.assertEqual(
            zigzagTraverse(test),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        )

    def test_case_2(self):
        test = [[1]]
        self.assertEqual(
            zigzagTraverse(test),
            [1]
        )
