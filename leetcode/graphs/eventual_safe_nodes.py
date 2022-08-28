import collections


class Solution:
    def eventualSafeNodes(self, graph):
        num_nodes = len(graph)
        node_status = [False for _ in range(num_nodes)]

        graph = [set(neighbors) for neighbors in graph]
        rgraph = [set() for _ in range(num_nodes)]
        to_process = collections.deque()

        for node, neighbors in enumerate(graph):
            if len(neighbors) == 0:
                to_process.append(node)
            for neighbor in neighbors:
                rgraph[neighbor].add(node)

        while len(to_process) > 0:
            safe_node = to_process.pop()
            node_status[safe_node] = True

            for reverse_neighbor in rgraph[safe_node]:
                graph[reverse_neighbor].remove(safe_node)

                if len(graph[reverse_neighbor]) == 0:
                    to_process.append(reverse_neighbor)

        return [i for i in range(num_nodes) if node_status[i] is True]


def main():
    input_1 = [[1, 2], [2, 3], [5], [0], [5], [], []]
    result_1 = Solution().eventualSafeNodes(input_1)
    print(result_1)

    input_2 = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
    result_2 = Solution().eventualSafeNodes(input_2)
    print(result_2)


if __name__ == '__main__':
    main()
