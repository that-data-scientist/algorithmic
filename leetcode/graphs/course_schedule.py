from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependency_graph = {}

        for course, dependency in prerequisites:
            if course not in dependency_graph.keys():
                dependency_graph[course] = set()

            if dependency in dependency_graph.keys():
                if course in dependency_graph[dependency]:
                    return False

            dependency_graph[course].add(dependency)

        cycle_found = False

        for node in dependency_graph.keys():
            visited = set()
            cycle_found = cycle_found or self.detect_cycle(dependency_graph, node,
                                                           visited)

        return not cycle_found

    def detect_cycle(self, graph, node, visited):
        if node in visited:
            return True

        if node not in graph.keys():
            return False

        visited.add(node)

        is_cycle_found = False
        for neighbor in graph[node]:
            is_cycle_found = is_cycle_found or self.detect_cycle(graph, neighbor, visited)

        visited.remove(node)
        graph[node] = []
        return is_cycle_found


def main():
    print(Solution().canFinish(2, [[1, 0], [0, 1]]))


if __name__ == '__main__':
    main()
