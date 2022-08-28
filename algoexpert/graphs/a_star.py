# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest
from typing import List


class Node:
    def __init__(self, row, col, value):
        self.id = str(row) + '-' + str(col)
        self.row = row
        self.col = col
        self.value = value
        self.distance_from_start = float('inf')  # g-score
        self.estimated_distance_to_end = float('inf')  # f-score
        self.came_from = None


def initialize_nodes(graph) -> List[List[Node]]:
    nodes = []

    for i, row in enumerate(graph):
        nodes.append([])
        for j, value in enumerate(row):
            nodes[i].append(Node(i, j, value))

    return nodes


def calculate_manhattan_distance(start_node, end_node):
    current_row = start_node.row
    current_col = start_node.col

    end_row = end_node.row
    end_col = end_node.col
    return abs(current_row - end_row) + abs(current_col - end_col)


def a_star_algorithm(start_row, start_col, end_row, end_col, graph):
    nodes = initialize_nodes(graph)

    start_node: Node = nodes[start_row][start_col]
    end_node: Node = nodes[end_row][end_col]

    start_node.distance_from_start = 0
    start_node.estimated_distance_to_end = calculate_manhattan_distance(
        start_node, end_node
    )

    nodes_to_visit = MinHeap([start_node])

    return []


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        start_row = 0
        start_col = 1
        end_row = 4
        end_col = 3

        graph = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 1, 1],
            [0, 0, 0, 0, 0]
        ]

        expected = [[0, 1], [0, 0], [1, 0], [2, 0], [2, 1], [3, 1], [4, 1], [4, 2],
                    [4, 3]]

        actual = a_star_algorithm(start_row, start_col, end_row, end_col, graph)
        self.assertEqual(actual, expected)
