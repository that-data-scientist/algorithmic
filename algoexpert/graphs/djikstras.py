import math
import unittest
from queue import PriorityQueue


# Time complexity - O((n+e) * log(n))
# Space complexity - O(n)
def dijkstrasAlgorithm(start, edges):
    shortest_distances = [math.inf for _ in range(len(edges))]
    visited = [False for _ in range(len(edges))]
    shortest_distances[start] = 0

    queue = PriorityQueue()
    queue.put((0, start))

    while not queue.empty():  # Time -  n
        node = queue.get()[1]  # Time -  log(n)
        if visited[node] is True:
            continue

        visited[node] = True
        neighbors = edges[node]

        for neighbor, distance in neighbors:  # Time -  e
            current_shortest_distance_neighbor = shortest_distances[neighbor]
            new_shortest_distance_neighbor = min(
                shortest_distances[neighbor],
                shortest_distances[node] + distance
            )

            if new_shortest_distance_neighbor < current_shortest_distance_neighbor:
                shortest_distances[neighbor] = new_shortest_distance_neighbor

            queue.put((shortest_distances[neighbor], neighbor))  # Time - log(n)

    for index, distance in enumerate(shortest_distances):
        if distance == math.inf:
            shortest_distances[index] = -1

    return shortest_distances


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        start = 0
        edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
        expected = [0, 7, 13, 27, 10, -1]
        actual = dijkstrasAlgorithm(start, edges)
        self.assertEqual(actual, expected)
