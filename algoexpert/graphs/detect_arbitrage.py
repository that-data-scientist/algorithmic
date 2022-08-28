# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!
import math
import unittest
from math import log


def detectArbitrageV2(exchange_rates):
    neg_log_exchange_rates = [
        [None for _ in range(len(exchange_rates[0]))] for _ in range(len(exchange_rates))
    ]

    for i in range(len(exchange_rates)):
        for j in range(len(exchange_rates[0])):
            neg_log_exchange_rates[i][j] = -log(exchange_rates[i][j])

    return detect_negative_cycle_bellman_fords(neg_log_exchange_rates)


# Time complexity - O(n^3)
# Space complexity - O(n)
def detect_negative_cycle_bellman_fords(matrix):
    num_nodes = len(matrix)
    shortest_distance = [math.inf for _ in range(num_nodes)]
    shortest_distance[0] = matrix[0][0]

    for _ in range(num_nodes - 1):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                shortest_distance[j] = min(
                    shortest_distance[j], shortest_distance[i] + matrix[i][j]
                )

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            min_distance = min(
                shortest_distance[j], shortest_distance[i] + matrix[i][j]
            )
            if min_distance != shortest_distance[j]:
                return True

    return False


def detectArbitrage(exchange_rates):
    for starting_currency in range(len(exchange_rates)):
        current_currency = starting_currency
        conversions = []
        is_arbitrage = check(
            exchange_rates, starting_currency, current_currency,
            100, 100, True, conversions
        )
        if is_arbitrage:
            return True
    return False


def check(
        exchange_rates,
        starting_currency,
        current_currency,
        starting_value,
        current_value,
        first_pass,
        conversions
):
    if starting_currency == current_currency and not first_pass:
        if current_value > starting_value:
            return True
        return False

    for currency, conversion_rate in enumerate(exchange_rates[current_currency]):
        if current_currency == currency:
            continue

        if (current_currency, currency) in conversions:
            continue
        if (currency, current_currency) in conversions:
            continue

        conversions.append((current_currency, currency))
        new_value = current_value * conversion_rate

        is_arbitrage = check(
            exchange_rates, starting_currency, currency,
            starting_value, new_value, False, conversions
        )
        if is_arbitrage:
            return True

        conversions.remove((current_currency, currency))

    return False


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [
            [1.0, 0.8631, 0.5903],
            [1.1586, 1.0, 0.6849],
            [1.6939, 1.46, 1.0]
        ]
        expected = True
        actual = detectArbitrageV2(input)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        input = [
            [1, 0.5, 0.25],
            [2, 1, 0.5],
            [4, 2, 1]
        ]
        expected = False
        actual = detectArbitrageV2(input)
        self.assertEqual(actual, expected)

    def test_case_3(self):
        input = [
            [1, 0.5, 0.25, 2, 4],
            [2, 1, 0.5, 4, 8],
            [4, 2, 1, 8, 16],
            [0.5, 0.25, 0.0125, 1, 2],
            [0.25, 0.0125, 0.00625, 0.5, 1]
        ]
        expected = False
        actual = detectArbitrageV2(input)
        self.assertEqual(actual, expected)
