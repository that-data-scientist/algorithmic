import math
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        return self.bellman_fords(times, k, n)

    # Tine complexity - O(v + e)
    # Space complexity - O(v)
    def bellman_fords(self, times, source, n) -> int:
        distances = [math.inf for _ in range(n)]
        distances[source - 1] = 0

        for _ in range(n):
            for source, destination, time in times:
                distances[destination - 1] = min(
                    distances[destination - 1],
                    distances[source - 1] + time
                )

        max_time = -math.inf
        for i in range(n):
            if distances[i] == math.inf:
                return -1

            if distances[i] > max_time:
                max_time = distances[i]

        return int(max_time)


def main():
    input = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    print(Solution().networkDelayTime(input, 4, 2))


if __name__ == '__main__':
    main()
