import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q2 import *


def test_create_airport_graph() -> None:
    G = {
        "Dallas": [("Austin", 200), ("Denver", 780), ("Chicago", 900)],
        "Austin": [("Dallas", 200), ("Houston", 160)],
        "Washington": [("Dallas", 1300), ("Atlanta", 600)],
        "Denver": [("Atlanta", 1400), ("Chicago", 1000)],
        "Atlanta": [("Washington", 600), ("Houston", 800)],
        "Chicago": [("Denver", 1000)],
        "Houston": [("Atlanta", 800)],
    }
    G_ = create_airport_graph()
    assert set(G_.keys()).difference(set(G.keys())) == set(), (
        "List of nodes is incorrect"
    )
    for node in G:
        assert set(G_[node]).difference(set(G[node])) == set(), (
            f"List of edges for node {node} is incorrect"
        )


def test_one_way_connection():
    G = create_airport_graph()
    connections = [
        ("Dallas", "Denver"),
        ("Dallas", "Chicago"),
        ("Austin", "Houston"),
        ("Washington", "Dallas"),
        ("Denver", "Atlanta"),
    ]
    connections_ = one_way_connection(G)
    assert set(connections) == set(connections_), (
        f"Expected {connections}, got {connections_}"
    )


def test_nearest_airport():
    G = create_airport_graph()
    airport_and_nearest_airport = [
        ("Dallas", "Austin"),
        ("Austin", "Houston"),
        ("Washington", "Atlanta"),
        ("Denver", "Chicago"),
        ("Atlanta", "Washington"),
        ("Chicago", "Denver"),
        ("Houston", "Atlanta"),
    ]
    for airport, nearest in airport_and_nearest_airport:
        nearest_ = nearest_airport(G, airport)
        assert nearest == nearest_, (
            f"Nearset airport for {airport} is {nearest}, got {nearest_}"
        )


def test_not_more_than_one_intermediate():
    connections = [
        ("Atlanta", ["Austin", "Chicago", "Dallas", "Denver", "Houston", "Washington"]),
        ("Austin", ["Dallas", "Washington"]),
        ("Chicago", ["Austin", "Dallas", "Denver", "Washington"]),
        ("Dallas", ["Atlanta", "Austin", "Washington"]),
        ("Denver", ["Austin", "Chicago", "Dallas", "Washington"]),
        ("Houston", ["Atlanta", "Austin", "Dallas", "Denver", "Washington"]),
        ("Washington", ["Atlanta", "Denver", "Houston"]),
    ]
    G = create_airport_graph()
    for airport, airports in connections:
        airports_ = not_more_than_one_intermediate(G, airport)
        assert set(airports) == set(airports_), f"Expected {airports}, got {airports_}"


def test_alien_attack():
    G = create_airport_graph()
    alien_attack_ = alien_attack(G)
    G_ = {
        "Dallas": [
            ("Austin", 200),
            ("Denver", 780),
            ("Chicago", 900),
            ("Atlanta", 1700),
        ],
        "Austin": [("Dallas", 200), ("Houston", 160)],
        "Denver": [("Atlanta", 1400), ("Chicago", 1000)],
        "Atlanta": [("Houston", 800), ("Dallas", 1700)],
        "Chicago": [("Denver", 1000)],
        "Houston": [("Atlanta", 800)],
    }
    for node in G:
        assert set(G_[node]) == set(alien_attack_[node]), (
            f"Expected {G_[node]}, got {alien_attack_[node]}"
        )
