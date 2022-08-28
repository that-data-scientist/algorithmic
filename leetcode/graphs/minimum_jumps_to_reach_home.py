import collections
from typing import List


class Node:
    def __init__(self, pos, num_jumps, last_jump_fw):
        self.pos = pos
        self.num_jumps = num_jumps
        self.last_jump_fw = last_jump_fw


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        return bfs(a, b, x, forbidden)


def bfs(fw_step, bw_step, home, forbidden):
    queue = collections.deque()
    queue.append(Node(0, 0, True))

    while len(queue):
        node = queue.popleft()

        if node.pos == home:
            return node.num_jumps

        if node.pos < 0:
            continue

        if node.pos in forbidden:
            continue

        if node.last_jump_fw:
            queue.append(Node(node.pos + fw_step, node.num_jumps + 1, True))
            queue.append(Node(node.pos - bw_step, node.num_jumps + 1, False))
        else:
            if fw_step > bw_step:
                return -1
            queue.append(Node(node.pos + fw_step, node.num_jumps + 1, True))

    return -1


def main():
    result = Solution().minimumJumps(
        [162, 118, 178, 152, 167, 100, 40, 74, 199, 186, 26, 73, 200, 127, 30, 124, 193,
         84, 184, 36, 103, 149, 153, 9, 54, 154, 133, 95, 45, 198, 79, 157, 64, 122, 59,
         71, 48, 177, 82, 35, 14, 176, 16, 108, 111, 6, 168, 31, 134, 164, 136, 72, 98],
        29,
        98,
        80
    )
    print(result)


if __name__ == '__main__':
    main()
