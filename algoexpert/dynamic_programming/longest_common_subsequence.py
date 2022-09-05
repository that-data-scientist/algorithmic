# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest


class Coordinates:
    def __init__(self, row, col):
        self.row = row
        self.col = col


class Node:
    def __init__(self, element, length_subsequence, parent):
        self.element = element
        self.length_subsequence = length_subsequence
        self.parent = parent


def compute_subsequence(subsequence_dp, str1, str2):
    subseq_elements = []

    current_row = len(str1)
    current_col = len(str2)

    while current_row != 0 and current_col != 0:
        current_node = subsequence_dp[current_row][current_col]
        current_element = current_node.element
        if current_element is not None:
            subseq_elements.append(current_element)

        current_row = current_node.parent.row
        current_col = current_node.parent.col

    return list(reversed(subseq_elements))


def longestCommonSubsequence(str1, str2):
    subsequence_dp = [
        [Node(None, 0, None) for _ in range(len(str2) + 1)]
        for _ in range(len(str1) + 1)
    ]

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                current_node = subsequence_dp[i][j]
                diagonal_left_node = subsequence_dp[i - 1][j - 1]

                current_node.element = str1[i - 1]
                current_node.length_subsequence = diagonal_left_node.length_subsequence + 1
                current_node.parent = Coordinates(i - 1, j - 1)
            else:
                current_node = subsequence_dp[i][j]
                left_node = subsequence_dp[i][j - 1]
                top_node = subsequence_dp[i - 1][j]

                if left_node.length_subsequence > top_node.length_subsequence:
                    current_node.length_subsequence = left_node.length_subsequence
                    current_node.parent = Coordinates(i, j - 1)
                else:
                    current_node.length_subsequence = top_node.length_subsequence
                    current_node.parent = Coordinates(i - 1, j)

    return compute_subsequence(subsequence_dp, str1, str2)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = longestCommonSubsequence("ZXVVYZW", "XKYKZPW")
        self.assertEqual(output, ["X", "Y", "Z", "W"])
