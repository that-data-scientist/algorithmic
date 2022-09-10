import unittest


def knapsackProblem(items, capacity):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        item_value = items[i - 1][0]
        item_weight = items[i - 1][1]

        for j in range(1, capacity + 1):
            if item_weight > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i - 1][j - item_weight] + item_value
                )

    return [dp[len(items)][capacity], get_items(dp, items)]


def get_items(dp, items):
    current_row = len(dp) - 1
    current_col = len(dp[0]) - 1
    selected_items = []

    while current_row > 0:
        if dp[current_row][current_col] == dp[current_row - 1][current_col]:
            current_row -= 1
        else:
            selected_items.append(current_row - 1)
            current_col -= items[current_row - 1][1]
            current_row -= 1

        if current_col == 0:
            break

    return list(reversed(selected_items))


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10),
            [10, [1, 3]]
        )
