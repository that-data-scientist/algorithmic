from typing import List


class Solution:
    def validPath(
            self,
            n: int,
            edges: List[List[int]],
            source: int,
            destination: int
    ) -> bool:
        graph = {}
        create_graph(edges, graph)

        return dfs(graph, destination, source, [])


# Time complexity - O(v + e)
# Space complexity - O(v)
def dfs(graph, destination, current_node, visited):
    if current_node in visited:
        return False

    if current_node == destination:
        return True

    path_found = False

    connected_nodes = graph[current_node]
    visited.append(current_node)

    for node in connected_nodes:
        path_found = path_found or dfs(graph, destination, node, visited)

    return path_found


def create_graph(edges, graph):
    for source, destination in edges:
        if source not in graph.keys():
            graph[source] = []

        if destination not in graph.keys():
            graph[destination] = []

        graph[source].append(destination)
        graph[destination].append(source)


def main():
    path = Solution().validPath(
        6,
        [[0, 7], [0, 8], [6, 1], [2, 0], [0, 4], [5, 8], [4, 7], [1, 3], [3, 5], [6, 5]],
        7, 5
    )
    print(path)


if __name__ == '__main__':
    main()
