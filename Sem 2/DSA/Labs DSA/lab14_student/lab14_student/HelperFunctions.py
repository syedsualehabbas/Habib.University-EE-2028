# This file contains helper functions for:
# 1. GraphADT

import csv
import math


# GRAPH FUNCTIONS

def AddNodes(G, nodes):
    for i in nodes:
        G[i] = list()
    return G


def AddEdges(G, edges, directed=False):
    if directed:
        for i, j, k in edges:
            try:
                G[i].append((j, k))
            except:
                return False
    else:
        for i, j, k in edges:
            try:
                G[i].append((j, k))
                G[j].append((i, k))
            except:
                return False
    return G

def ListOfNodes(G):
    return [i for i in G.keys()]

def GetNeighbors(G, node):
    return G[node]




