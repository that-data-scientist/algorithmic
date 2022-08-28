import collections
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        num_rows = len(maze)
        num_columns = len(maze[0])
        exit_points = set()

        for i in range(num_rows):
            if maze[i][0] == ".":
                exit_points.add((i, 0))

            if maze[i][num_columns - 1] == ".":
                exit_points.add((i, num_columns - 1))

        for j in range(num_columns):
            if maze[0][j] == ".":
                exit_points.add((0, j))

            if maze[num_rows - 1][j] == ".":
                exit_points.add((num_rows - 1, j))

        if (entrance[0], entrance[1]) in exit_points:
            exit_points.remove((entrance[0], entrance[1]))

        return bfs(maze, entrance[0], entrance[1], exit_points)


def bfs(maze, i, j, exit_points):
    neighbor_transitions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = collections.deque()
    visited = set()

    queue.append((i, j, 0))

    while len(queue) > 0:
        (x, y, distance) = queue.popleft()

        if x >= len(maze) or y >= len(maze[0]) or x < 0 or y < 0:
            continue

        if (x, y) in exit_points:
            return distance

        if (x, y) in visited:
            continue

        if maze[x][y] != ".":
            continue

        visited.add((x, y))

        for x_transition, y_transition in neighbor_transitions:
            new_x = x + x_transition
            new_y = y + y_transition
            queue.append((new_x, new_y, distance + 1))

    return -1


def main():
    result = Solution().nearestExit(
        [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]
    )
    print(result)


if __name__ == '__main__':
    main()
