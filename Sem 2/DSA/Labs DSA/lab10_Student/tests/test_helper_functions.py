import math
import os
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


from helper_functions import (
    addEdges,
    addNodes,
    getNearestNeighbor,
    getNeighbours,
    listOfEdges,
    listOfNodes,
    removeNode,
    removeNodes,
    displayGraph
)


def test_addNodes(meta) -> None:
    G, _, nodes, _, _ = meta
    G_ = {}
    addNodes(G_, nodes)
    assert set(G_.keys()) == set(nodes), "Adding nodes is incorrect"


def test_addEdges(meta) -> None:
    G, directed, nodes, edges, _ = meta
    G_ = {}
    addNodes(G_, nodes)
    addEdges(G_, edges, directed)
    assert set(listOfEdges(G_)) == set(edges), "Adding edges is incorrect"


def test_listofnodes(meta) -> None:
    G, _, nodes, _, _ = meta
    nodes_ = listOfNodes(G)
    print(nodes_)
    assert set(nodes_) == set(nodes), "List of nodes is incorrect"


def test_listOfEdges(meta) -> None:
    G, _, _, edges, _ = meta
    edges_ = listOfEdges(G)
    assert set(edges_) == set(edges), "List of edges is incorrect"


def test_get_neighbours(meta) -> None:
    G, _, _, _, neighbours = meta
    for node in G:
        assert set(getNeighbours(G, node)) == set(neighbours[node]), (
            f"Neighbours of {node} is incorrect"
        )


def test_removeNode(meta) -> None:
    G, _, nodes, _, _ = meta
    G_ = G.copy()
    removeNode(G_, nodes[0])
    assert nodes[0] not in G_, "Node is not removed"


def test_removeNodes(meta) -> None:
    G, _, nodes, _, _ = meta
    G_ = G.copy()
    removeNodes(G_, nodes)
    assert set(G_.keys()).isdisjoint(set(nodes)), "Nodes are not removed"


def test_getNearestNeighbor(meta) -> None:
    G, _, _, _, _ = meta

    for node in G:
        low = (math.inf, math.inf)
        for i, j in G[node]:
            low = (i, j) if j < low[1] else low
        assert getNearestNeighbor(G, node) == low[0], "Nearest neighbour is incorrect"

def test_displaygraph(meta, capsys) -> None:
    G, _, _, _, _ = meta
    displayGraph(G)
    captured,err = capsys.readouterr()
    captured=captured[:-1]
    assert eval(captured) == G