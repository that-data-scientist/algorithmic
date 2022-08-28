import math
import collections
from typing import List


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.red_neighbors = []
        self.blue_neighbors = []


class Solution:
    def shortestAlternatingPaths(
            self,
            n: int,
            red_edges: List[List[int]],
            blue_edges: List[List[int]]
    ) -> List[int]:
        graph = {}

        for source, destination in red_edges:
            if source not in graph.keys():
                graph[source] = Node(source)

            graph[source].red_neighbors.append(destination)

        for source, destination in blue_edges:
            if source not in graph.keys():
                graph[source] = Node(source)

            graph[source].blue_neighbors.append(destination)

        node_distances = [math.inf for _ in range(n)]
        visited = set()

        queue = collections.deque()
        queue.append((0, 0, "red"))
        queue.append((0, 0, "blue"))

        while len(queue) != 0:
            node, current_distance, current_color = queue.popleft()

            if (node, current_color) in visited:
                continue

            if current_distance < node_distances[node]:
                node_distances[node] = current_distance

            visited.add((node, current_color))

            if node not in graph.keys():
                continue

            if current_color == 'red':
                neighbors = graph[node].red_neighbors
                next_color = 'blue'
            else:
                neighbors = graph[node].blue_neighbors
                next_color = 'red'

            for neighbor in neighbors:
                queue.append((neighbor, current_distance + 1, next_color))

        for node, distance in enumerate(node_distances):
            if distance == math.inf:
                node_distances[node] = -1

        return node_distances


def main():
    result1 = Solution().shortestAlternatingPaths(3, [[0, 1], [1, 2]], [])
    print(result1)

    result2 = Solution().shortestAlternatingPaths(3, [[0, 1]], [[2, 1]])
    print(result2)


if __name__ == '__main__':
    main()
