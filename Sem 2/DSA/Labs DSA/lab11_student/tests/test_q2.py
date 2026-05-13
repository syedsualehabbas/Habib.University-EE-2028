import os
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q2 import *

def test_create_airport_graph():
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

def test_max_inbound_outbound_airport():
    G = create_airport_graph()
    assert max_inbound_outbound_airport(G) == ("Atlanta", "Dallas")
