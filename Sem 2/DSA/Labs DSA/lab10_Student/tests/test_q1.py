import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import *


def test_create_graph() -> None:
    G = {
        1: [(2, 1), (5, 1)],
        2: [(1, 1), (3, 1), (4, 1), (5, 1)],
        3: [(2, 1), (4, 1)],
        4: [(2, 1), (3, 1), (5, 1)],
        5: [(1, 1), (2, 1), (4, 1)],
    }
    G_ = create_graph()
    assert set(G_.keys()).difference(set(G.keys())) == set(), (
        "List of nodes is incorrect"
    )
    for node in G:
        assert set(G_[node]).difference(set(G[node])) == set(), (
            f"List of edges for node {node} is incorrect"
        )


def test_get_list_of_nodes() -> None:
    nodes = [1, 2, 3, 4, 5]
    G = create_graph()
    nodes_ = get_list_of_nodes(G)
    assert set(nodes_) == set(nodes), "List of nodes is incorrect"


def test_get_list_of_edges() -> None:
    edges = [
        (1, 2, 1),
        (1, 5, 1),
        (2, 3, 1),
        (2, 4, 1),
        (2, 5, 1),
        (3, 4, 1),
        (4, 5, 1),
    ]
    G = create_graph()
    edges_ = get_list_of_edges(G)
    assert set(edges_) == set(edges), "List of edges is incorrect"


def test_get_all_neighbours() -> None:
    neighbours = {1: [2, 5], 2: [1, 3, 4, 5], 3: [2, 4], 4: [2, 3, 5], 5: [1, 2, 4]}
    G = create_graph()
    neighbours_ = get_all_neighbours(G)
    for node in G:
        assert set(neighbours_[node]) == set(neighbours[node]), (
            f"Neighbours of {node} is incorrect"
        )
