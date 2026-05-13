import pytest

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from helper_functions import (
    adjlst_to_adj_matrix,
    csv_to_adj_list,
    degree,
    getInNeighbors,
    getOutNeighbors,
    in_out_degree,
    initialize_matrix,
    isNeighbor,
)


def test_in_out_degree(meta) -> None:
    G, _, _, _, _ = meta
    _dict = {
        i: (sum(1 for j in G.values() for x, _ in j if x == i), len(G[i])) for i in G
    }
    assert in_out_degree(G) == _dict, "In and out degree is incorrect"


def test_degree(meta) -> None:
    G, _, _, _, _ = meta
    _dict = {i: len(G[i]) for i in G}
    assert degree(G) == _dict, "Degree is incorrect"


def test_getInNeighbors(meta) -> None:
    G, _, _, _, _ = meta
    for node in G:
        assert set(getInNeighbors(G, node)) == set(
            [i for i in G if isNeighbor(G, i, node)]
        ), f"In neighbours of {node} is incorrect"


def test_getOutNeighbors(meta) -> None:
    G, _, _, _, _ = meta
    for node in G:
        assert set(getOutNeighbors(G, node)) == set(
            [i for i, _ in G[node]]
        ), f"Out neighbours of {node} is incorrect"


def test_isNeighbor(meta) -> None:
    G, _, _, _, _ = meta
    for node in G:
        for i, _ in G[node]:
            assert isNeighbor(G, node, i), f"{node} and {i} are not neighbours"


@pytest.mark.parametrize("r", [1, 2, 3, 5, 9])
@pytest.mark.parametrize("c", [1, 2, 3, 5, 9])
def test_initialize_matrix(r, c) -> None:
    matrix = initialize_matrix(r, c)
    assert len(matrix) == r, "Number of rows is incorrect"
    assert all(len(row) == c for row in matrix), "Number of columns is incorrect"
    for row in matrix:
        assert all(x == -1 for x in row), "Matrix is not initialized correctly"


def test_adjlst_to_adj_matrix(meta) -> None:
    G, _, nodes, _, _ = meta
    n = len(nodes)
    _matrix = initialize_matrix(n, n)
    matrix = adjlst_to_adj_matrix(G)
    for row, node in enumerate(nodes):
        for node2, value in G[node]:
            _matrix[row][nodes.index(node2)] = value
    for i in range(n):
        for j in range(n):
            assert matrix[i][j] == _matrix[i][j]


@pytest.mark.parametrize("filename", ["connections.csv"])
def test_csv_to_adj_list(filename: str) -> None:
    G_ = csv_to_adj_list(filename)
    G = {
        "Islamabad": [("Taxila", 46), ("Murree", 49)],
        "Taxila": [("Islamabad", 46), ("Abbottabad", 74), ("Malam Jabba", 254)],
        "Murree": [("Islamabad", 49), ("Nathiagali", 36), ("Muzaffarabad", 68)],
        "Nathiagali": [("Murree", 36), ("Abbottabad", 34)],
        "Abbottabad": [("Taxila", 74), ("Nathiagali", 34), ("Mansehra", 23)],
        "Mansehra": [("Abbottabad", 23), ("Balakot", 37), ("Bisham", 113)],
        "Balakot": [("Mansehra", 37), ("Kaghan", 59), ("Bisham", 136)],
        "Kaghan": [("Balakot", 59), ("Naran", 22)],
        "Naran": [("Kaghan", 22), ("Chilas", 113)],
        "Chilas": [("Naran", 113), ("Bisham", 199), ("Gilgit", 133), ("Hunza", 306)],
        "Bisham": [
            ("Mansehra", 113),
            ("Balakot", 136),
            ("Chilas", 199),
            ("Malam Jabba", 61),
        ],
        "Gilgit": [("Chilas", 133), ("Hunza", 186), ("Skardu", 208)],
        "Hunza": [
            ("Chilas", 306),
            ("Gilgit", 186),
            ("Khunjerab Pass", 151),
            ("Skardu", 381),
        ],
        "Khunjerab Pass": [("Hunza", 151)],
        "Malam Jabba": [("Taxila", 254), ("Bisham", 61)],
        "Skardu": [("Gilgit", 208), ("Hunza", 381), ("Muzaffarabad", 484)],
        "Muzaffarabad": [("Murree", 68), ("Skardu", 484)],
    }
    assert set(G_.keys()).difference(set(G.keys())) == set(), (
        "List of nodes is incorrect"
    )
    for node in G:
        assert set(G_[node]).difference(set(G[node])) == set(), (
            f"List of edges for node {node} is incorrect"
        )