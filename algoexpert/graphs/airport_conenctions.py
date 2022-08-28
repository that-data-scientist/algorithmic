# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest

AIRPORTS = [
    "BGI",
    "CDG",
    "DEL",
    "DOH",
    "DSM",
    "EWR",
    "EYW",
    "HND",
    "ICN",
    "JFK",
    "LGA",
    "LHR",
    "ORD",
    "SAN",
    "SFO",
    "SIN",
    "TLV",
    "BUD",
]

STARTING_AIRPORT = "LGA"


def airportConnections(airports, routes, starting_airport):
    reachable_airports = []
    dfs_util(routes, starting_airport, reachable_airports)

    all_non_reachable_airports = set(airports) - set(reachable_airports)

    all_unreachable_airport_connections = {}

    for airport in all_non_reachable_airports:
        reachable_airports = []
        dfs_util(routes, airport, reachable_airports)
        all_unreachable_airport_connections[airport] = reachable_airports

    all_unreachable_airport_connections_sorted = sorted(
        all_unreachable_airport_connections,
        key=lambda k: len(all_unreachable_airport_connections[k]),
        reverse=True
    )

    can_reach = {}
    for airport in all_non_reachable_airports:
        can_reach[airport] = False

    num_connections = 0
    for airport in all_unreachable_airport_connections_sorted:
        connections = all_unreachable_airport_connections[airport]
        to_add_connection = False

        for connection in connections:
            if connection in can_reach.keys():
                if can_reach[connection] is False:
                    can_reach[connection] = True
                    to_add_connection = True

        if to_add_connection:
            num_connections += 1

    return num_connections


# Time complexity - O(v*e)
# Space complexity - O(v)
def dfs_util(routes, current_airport, reachable_airports):
    if current_airport in reachable_airports:
        return

    reachable_airports.append(current_airport)

    for route in routes:
        if route[0] == current_airport:
            dfs_util(routes, route[1], reachable_airports)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        routes = [
            ["DSM", "ORD"],
            ["ORD", "BGI"],
            ["BGI", "LGA"],
            ["SIN", "CDG"],
            ["CDG", "SIN"],
            ["CDG", "BUD"],
            ["DEL", "DOH"],
            ["DEL", "CDG"],
            ["TLV", "DEL"],
            ["EWR", "HND"],
            ["HND", "ICN"],
            ["HND", "JFK"],
            ["ICN", "JFK"],
            ["JFK", "LGA"],
            ["EYW", "LHR"],
            ["LHR", "SFO"],
            ["SFO", "SAN"],
            ["SFO", "DSM"],
            ["SAN", "EYW"],
        ]
        self.assertTrue(airportConnections(AIRPORTS, routes, STARTING_AIRPORT) == 3)
