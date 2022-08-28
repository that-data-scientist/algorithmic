import math
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        max_distance = -1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    max_distance = max(
                        max_distance,
                        self.find_distance_to_closest_land(grid, i, j)
                    )

        return max_distance

    def find_distance_to_closest_land(self, grid, i, j):
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
            return math.inf

        if grid[i][j] == -1:
            return math.inf

        if grid[i][j] == 1:
            return 0

        grid[i][j] = -1

        max_distance = 1 + min(
            self.find_distance_to_closest_land(grid, i + 1, j),
            self.find_distance_to_closest_land(grid, i - 1, j),
            self.find_distance_to_closest_land(grid, i, j + 1),
            self.find_distance_to_closest_land(grid, i, j - 1)
        )

        grid[i][j] = 0

        return max_distance


def main():
    result1 = Solution().maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]])
    print(result1)

    result2 = Solution().maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
    print(result2)


if __name__ == '__main__':
    main()
