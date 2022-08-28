import collections
import math
from typing import List
from copy import deepcopy


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        num_rows = len(heights)
        num_columns = len(heights[0])

        a_visited = set()
        p_visited = set()

        for i in range(num_rows):
            self.dfs(heights, i, 0, p_visited, -1)
            self.dfs(heights, i, num_columns - 1, a_visited, -1)

        for j in range(num_columns):
            self.dfs(heights, 0, j, p_visited, -1)
            self.dfs(heights, num_rows - 1, j, a_visited, -1)

        return list(a_visited.intersection(p_visited))

    def dfs(self, heights, i, j, visited, prev_value):
        if i >= len(heights) or j >= len(heights[0]) or i < 0 or j < 0:
            return

        if (i, j) in visited:
            return

        if heights[i][j] < prev_value:
            return

        visited.add((i, j))

        self.dfs(heights, i+1, j, visited, heights[i][j])
        self.dfs(heights, i-1, j, visited, heights[i][j])
        self.dfs(heights, i, j+1, visited, heights[i][j])
        self.dfs(heights, i, j-1, visited, heights[i][j])


def main():
    result = Solution().pacificAtlantic(
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4]]
    )
    print(result)


if __name__ == '__main__':
    main()
