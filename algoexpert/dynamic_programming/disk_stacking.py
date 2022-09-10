# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest


def buildSequence(disks, sequence, max_idx):
    result = []
    cur_idx = max_idx

    while cur_idx is not None:
        result.append(disks[cur_idx])
        cur_idx = sequence[cur_idx]

    return list(reversed(result))


def diskStacking(disks):
    sorted_disks = sorted(disks, key=lambda disk: disk[2])
    # print(sorted_disks)
    max_height = [disk[2] for disk in sorted_disks]
    sequence = [None for _ in range(len(sorted_disks))]
    max_height_index = 0

    for index in range(1, len(sorted_disks)):
        current_disk = sorted_disks[index]

        for j in range(index):
            other_disk = sorted_disks[j]
            if (
                    (other_disk[0] < current_disk[0]) and
                    (other_disk[1] < current_disk[1]) and
                    (other_disk[2] < current_disk[2])
            ):
                if max_height[index] <= current_disk[2] + max_height[j]:
                    max_height[index] = current_disk[2] + max_height[j]
                    sequence[index] = j

        if max_height[index] > max_height[max_height_index]:
            max_height_index = index

    return buildSequence(sorted_disks, sequence, max_height_index)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            diskStacking(
                [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [2, 2, 1], [4, 4, 5]]
            ),
            [[2, 1, 2], [3, 2, 3], [4, 4, 5]],
        )
