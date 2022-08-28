import collections
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        bi_graph = collections.defaultdict(list)

        min_num_reorder = 0

        for node, neighbor in connections:
            graph[node].append(neighbor)

            bi_graph[node].append(neighbor)
            bi_graph[neighbor].append(node)

        queue = collections.deque()
        visited = set()
        queue.append(0)

        while len(queue) != 0:
            node = queue.popleft()
            if node in visited:
                continue

            visited.add(node)
            outgoing_edges = graph[node]

            for neighbor in outgoing_edges:
                if neighbor not in visited:
                    min_num_reorder += 1

            for bi_neighbor in bi_graph[node]:
                queue.append(bi_neighbor)

        return min_num_reorder


def main():
    result = Solution().minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]])
    print(result)


if __name__ == '__main__':
    main()
