from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        return dfs(arr, start, visited)


def dfs(arr, current_pos, visited):
    if current_pos >= len(arr) or current_pos < 0:
        return False

    if current_pos in visited:
        return False

    if arr[current_pos] == 0:
        return True

    visited.add(current_pos)
    neighbors = [
        current_pos + arr[current_pos],
        current_pos - arr[current_pos]
    ]

    can_reach = False

    for neighbor in neighbors:
        can_reach = can_reach or dfs(arr, neighbor, visited)

    return can_reach


def main():
    result = Solution().canReach([4, 2, 3, 0, 3, 1, 2], 5)
    print(result)


if __name__ == '__main__':
    main()
