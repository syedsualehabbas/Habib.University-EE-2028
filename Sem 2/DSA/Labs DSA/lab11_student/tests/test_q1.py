import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import *

def test_create_directed_graph():
    G = {
        1: [(2, 1)],
        2: [(4, 1)],
        3: [(1, 1), (2, 1)],
        4: [(3, 1), (4, 1)],
    }

    G_ = create_directed_graph()
    assert set(G_.keys()).difference(set(G.keys())) == set(), (
        "List of nodes is incorrect"
    )
    for node in G:
        assert set(G_[node]).difference(set(G[node])) == set(), (
            f"List of edges for node {node} is incorrect"
        )

def test_displaygraph(capsys) -> None:
    G = create_directed_graph()
    displayGraph(G)
    captured,err = capsys.readouterr()
    captured=captured[:-1]
    assert eval(captured) == G

def test_in_degree():
    G = create_directed_graph()
    assert in_neighbors(G) == {
        1: [3],
        2: [1, 3],
        3: [4],
        4: [2, 4],
    }


def test_out_neighbors():
    G = create_directed_graph()
    assert out_neighbors(G) == {
        1: [2],
        2: [4],
        3: [1, 2],
        4: [3, 4],
    }


def test_print_adjacency_matrix():
    G = create_directed_graph()
    assert generate_adjacency_matrix(G) == [
        [-1, 1, -1, -1],
        [-1, -1, -1, 1],
        [1, 1, -1, -1],
        [-1, -1, 1, 1],
    ]


def test_check_degree_sums():
    G = create_directed_graph()
    assert check_degree_sums(G) == True