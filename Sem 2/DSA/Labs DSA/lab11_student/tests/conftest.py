from typing import Dict, List, Tuple

import pytest


_META = [
    # Test Case 1: A single-node directed graph (with no edges)
    (
        {"A": []},  # Graph
        True,  # Directed
        ["A"],  # List of Nodes
        [],  # List of Edges
        {"A": []},  # Neighbours
    ),
    # Test Case 2: A directed acyclic graph with integer nodes
    (
        {1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1)], 4: []},  # Graph
        True,  # Directed
        [1, 2, 3, 4],  # List of Nodes
        [(1, 2, 1), (1, 3, 1), (2, 4, 1), (3, 4, 1)],  # List of Edges
        {1: [2, 3], 2: [4], 3: [4], 4: []},  # Neighbours
    ),
    # Test Case 3: An undirected cycle graph with string nodes
    (
        {
            "a": [("b", 2), ("d", 2)],
            "b": [("a", 2), ("c", 2)],
            "c": [("b", 2), ("d", 2)],
            "d": [("c", 2), ("a", 2)],
        },  # Graph
        False,  # Undirected
        ["a", "b", "c", "d"],  # List of Nodes
        [("a", "b", 2), ("a", "d", 2), ("b", "c", 2), ("c", "d", 2)],  # List of Edges
        {
            "a": ["b", "d"],
            "b": ["a", "c"],
            "c": ["b", "d"],
            "d": ["c", "a"],
        },  # Neighbours
    ),
    # Test Case 4: An undirected graph with isolated nodes (integer nodes)
    (
        {1: [], 2: [(3, 1)], 3: [(2, 1)], 4: []},  # Graph
        False,  # Undirected
        [1, 2, 3, 4],  # List of Nodes
        [(2, 3, 1)],  # List of Edges (only one edge in the graph)
        {1: [], 2: [3], 3: [2], 4: []},  # Neighbours
    ),
    # Test Case 5: A weighted directed graph with string nodes
    (
        {"X": [("Y", 3), ("Z", 5)], "Y": [("Z", 2)], "Z": [("W", 4)], "W": []},  # Graph
        True,  # Directed
        ["X", "Y", "Z", "W"],  # List of Nodes
        [("X", "Y", 3), ("X", "Z", 5), ("Y", "Z", 2), ("Z", "W", 4)],  # List of Edges
        {"X": ["Y", "Z"], "Y": ["Z"], "Z": ["W"], "W": []},  # Neighbours
    ),
    # Test Case 6: Directed graph with self-loops and negative weights
    (
        {"A": [("A", -2), ("B", 3)], "B": [("C", -1)], "C": [("A", 4)]},
        True,  # Directed
        ["A", "B", "C"],
        [("A", "A", -2), ("A", "B", 3), ("B", "C", -1), ("C", "A", 4)],
        {"A": ["A", "B"], "B": ["C"], "C": ["A"]},
    ),
    # Test Case 7: Undirected graph with two disconnected components (integers)
    (
        {
            1: [(2, 1), (3, 1)],
            2: [(1, 1), (3, 1)],
            3: [(1, 1), (2, 1)],
            4: [(5, 2), (6, 2)],
            5: [(4, 2), (6, 2)],
            6: [(4, 2), (5, 2)],
        },
        False,  # Undirected
        [1, 2, 3, 4, 5, 6],
        [(1, 2, 1), (1, 3, 1), (2, 3, 1), (4, 5, 2), (4, 6, 2), (5, 6, 2)],
        {1: [2, 3], 2: [1, 3], 3: [1, 2], 4: [5, 6], 5: [4, 6], 6: [4, 5]},
    ),
    # Test Case 8: Directed cyclic graph with multiple cycles (string nodes with creative labels)
    (
        {
            "X": [("Y", 5)],
            "Y": [("Z", 3), ("W", 4)],
            "Z": [("X", 2), ("W", 1)],
            "W": [("Y", 6)],
        },
        True,  # Directed
        ["X", "Y", "Z", "W"],
        [
            ("X", "Y", 5),
            ("Y", "Z", 3),
            ("Y", "W", 4),
            ("Z", "X", 2),
            ("Z", "W", 1),
            ("W", "Y", 6),
        ],
        {"X": ["Y"], "Y": ["Z", "W"], "Z": ["X", "W"], "W": ["Y"]},
    ),
    # Test Case 9: Undirected weighted tree (strings) representing a spanning tree structure
    (
        {
            "root": [("child1", 10), ("child2", 15)],
            "child1": [("root", 10), ("grandchild", 5)],
            "child2": [("root", 15)],
            "grandchild": [("child1", 5)],
        },
        False,  # Undirected
        ["root", "child1", "child2", "grandchild"],
        [
            ("root", "child1", 10),
            ("root", "child2", 15),
            ("child1", "grandchild", 5),
        ],
        {
            "root": ["child1", "child2"],
            "child1": ["root", "grandchild"],
            "child2": ["root"],
            "grandchild": ["child1"],
        },
    ),
    # Test Case 10: Directed acyclic graph (DAG) with mixed positive weights and string nodes
    (
        {
            "start": [("mid1", 7), ("mid2", 3)],
            "mid1": [("end", 1)],
            "mid2": [("end", 2)],
            "end": [],
        },
        True,  # Directed
        ["start", "mid1", "mid2", "end"],
        [
            ("start", "mid1", 7),
            ("start", "mid2", 3),
            ("mid1", "end", 1),
            ("mid2", "end", 2),
        ],
        {"start": ["mid1", "mid2"], "mid1": ["end"], "mid2": ["end"], "end": []},
    ),
]


@pytest.fixture(scope="module", params=_META)
def meta(
    request: pytest.FixtureRequest,
) -> Tuple[Dict, bool, List, List, Dict]:
    G, directed, nodes, edges, neighbours = request.param
    return G, directed, nodes, edges, neighbours
