# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest
from copy import deepcopy

def largestRange(array):
    new_array = sorted(array)

    max_range = [0, 0]
    max_range_length = 1

    cur_range = [0, 0]
    cur_range_length = 1

    for i in range(1, len(new_array)):
        if (new_array[i] - 1) == new_array[i - 1]:
            cur_range_length += 1
            cur_range[1] = i
        else:
            cur_range[0] = i
            cur_range[1] = i
            cur_range_length = 1

        if cur_range_length > max_range_length:
            max_range = deepcopy(cur_range)
            max_range_length = cur_range_length

    return max_range


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]), [0, 7])
