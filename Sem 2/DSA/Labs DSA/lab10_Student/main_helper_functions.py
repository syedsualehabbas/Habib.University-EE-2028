from helper_functions import *


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def _test(got, expected):
    if got == expected:
        prefix = " OK "
        print(prefix)
    else:
        prefix = "  X "
        print("%s got: %s expected: %s" % (prefix, repr(got), repr(expected)))


def _test_listofedges(got, expectedLst):
    if got == expectedLst:
        prefix = " OK "
        print(prefix)
    else:
        prefix = "  X "
        print(
            "%s got: %s expected one of these outputs: %s"
            % (prefix, repr(got), repr(expectedLst))
        )


def addNodes_testcases():
    G = {}
    nodes = [0, 1, 2, 3, 4, 5]
    addNodes(G, nodes)
    _test(G, {0: [], 1: [], 2: [], 3: [], 4: [], 5: []})

    #######################################################

    G = {}
    nodes = [2, 4, 6, 8, 10]
    addNodes(G, nodes)
    _test(G, {2: [], 4: [], 6: [], 8: [], 10: []})

    #######################################################

    G = {}
    nodes = ["A", "B", "C", "D", "E"]
    addNodes(G, nodes)
    _test(G, {"A": [], "B": [], "C": [], "D": [], "E": []})

    #######################################################

    G = {}
    nodes = ["BOS", "ORD", "JFK", "DFW", "MIA", "SFO", "LAX"]
    addNodes(G, nodes)
    _test(
        G, {"BOS": [], "ORD": [], "JFK": [], "DFW": [], "MIA": [], "SFO": [], "LAX": []}
    )


def addEdges_testcases():
    G = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

    edge_list = [
        (0, 1, 1),
        (0, 2, 1),
        (1, 2, 1),
        (1, 3, 1),
        (2, 4, 1),
        (3, 4, 1),
        (3, 5, 1),
        (4, 5, 1),
    ]
    addEdges(G, edge_list, True)
    _test(
        G,
        {
            0: [(1, 1), (2, 1)],
            1: [(2, 1), (3, 1)],
            2: [(4, 1)],
            3: [(4, 1), (5, 1)],
            4: [(5, 1)],
            5: [],
        },
    )

    ##########################################################################################################

    G = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

    edge_list = [
        (0, 1, 1),
        (0, 2, 1),
        (1, 2, 1),
        (1, 3, 1),
        (2, 4, 1),
        (3, 4, 1),
        (3, 5, 1),
        (4, 5, 1),
    ]
    addEdges(G, edge_list, False)
    _test(
        G,
        {
            0: [(1, 1), (2, 1)],
            1: [(0, 1), (2, 1), (3, 1)],
            2: [(0, 1), (1, 1), (4, 1)],
            3: [(1, 1), (4, 1), (5, 1)],
            4: [(2, 1), (3, 1), (5, 1)],
            5: [(3, 1), (4, 1)],
        },
    )

    ##########################################################################################################

    G = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

    edge_list = [
        (0, 1, 21),
        (0, 2, 15),
        (1, 2, 10),
        (1, 3, 70),
        (2, 4, 50),
        (3, 4, 24),
        (3, 5, 39),
        (4, 5, 99),
    ]
    addEdges(G, edge_list, True)
    _test(
        G,
        {
            0: [(1, 21), (2, 15)],
            1: [(2, 10), (3, 70)],
            2: [(4, 50)],
            3: [(4, 24), (5, 39)],
            4: [(5, 99)],
            5: [],
        },
    )

    ##########################################################################################################

    G = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

    edge_list = [
        (0, 1, 21),
        (0, 2, 15),
        (1, 2, 10),
        (1, 3, 70),
        (2, 4, 50),
        (3, 4, 24),
        (3, 5, 39),
        (4, 5, 99),
    ]
    addEdges(G, edge_list, False)
    _test(
        G,
        {
            0: [(1, 21), (2, 15)],
            1: [(0, 21), (2, 10), (3, 70)],
            2: [(0, 15), (1, 10), (4, 50)],
            3: [(1, 70), (4, 24), (5, 39)],
            4: [(2, 50), (3, 24), (5, 99)],
            5: [(3, 39), (4, 99)],
        },
    )

    ##########################################################################################################

    G = {"BOS": [], "ORD": [], "JFK": [], "DFW": [], "MIA": [], "SFO": [], "LAX": []}
    edges = [
        ("BOS", "JFK", 1),
        ("BOS", "MIA", 1),
        ("BOS", "SFO", 1),
        ("JFK", "BOS", 1),
        ("JFK", "SFO", 1),
        ("JFK", "MIA", 1),
        ("JFK", "DFW", 1),
        ("ORD", "MIA", 1),
        ("ORD", "DFW", 1),
        ("MIA", "DFW", 1),
        ("MIA", "LAX", 1),
        ("DFW", "ORD", 1),
        ("DFW", "SFO", 1),
        ("DFW", "LAX", 1),
        ("SFO", "LAX", 1),
        ("LAX", "ORD", 1),
    ]
    addEdges(G, edges, True)
    _test(
        G,
        {
            "BOS": [("JFK", 1), ("MIA", 1), ("SFO", 1)],
            "ORD": [("MIA", 1), ("DFW", 1)],
            "JFK": [("BOS", 1), ("SFO", 1), ("MIA", 1), ("DFW", 1)],
            "DFW": [("ORD", 1), ("SFO", 1), ("LAX", 1)],
            "MIA": [("DFW", 1), ("LAX", 1)],
            "SFO": [("LAX", 1)],
            "LAX": [("ORD", 1)],
        },
    )

    ##########################################################################################################

    G = {"BOS": [], "ORD": [], "JFK": [], "DFW": [], "MIA": [], "SFO": [], "LAX": []}
    edges = [
        ("BOS", "JFK", 1),
        ("BOS", "MIA", 1),
        ("BOS", "SFO", 1),
        ("JFK", "SFO", 1),
        ("JFK", "MIA", 1),
        ("JFK", "DFW", 1),
        ("ORD", "MIA", 1),
        ("ORD", "DFW", 1),
        ("MIA", "DFW", 1),
        ("MIA", "LAX", 1),
        ("DFW", "SFO", 1),
        ("DFW", "LAX", 1),
        ("SFO", "LAX", 1),
        ("LAX", "ORD", 1),
    ]
    addEdges(G, edges, False)
    _test(
        G,
        {
            "BOS": [("JFK", 1), ("MIA", 1), ("SFO", 1)],
            "ORD": [("MIA", 1), ("DFW", 1), ("LAX", 1)],
            "JFK": [("BOS", 1), ("SFO", 1), ("MIA", 1), ("DFW", 1)],
            "DFW": [("JFK", 1), ("ORD", 1), ("MIA", 1), ("SFO", 1), ("LAX", 1)],
            "MIA": [("BOS", 1), ("JFK", 1), ("ORD", 1), ("DFW", 1), ("LAX", 1)],
            "SFO": [("BOS", 1), ("JFK", 1), ("DFW", 1), ("LAX", 1)],
            "LAX": [("MIA", 1), ("DFW", 1), ("SFO", 1), ("ORD", 1)],
        },
    )

    ##########################################################################################################


def listOfNodes_testcases():
    G = {
        0: [(1, 1), (2, 1)],
        1: [(2, 1), (3, 1)],
        2: [(4, 1)],
        3: [(4, 1), (5, 1)],
        4: [(5, 1)],
        5: [],
    }
    _test(sorted(listOfNodes(G)), sorted([0, 1, 2, 3, 4, 5]))

    ##############################################################################################

    G = {
        "BOS": [("JFK", 1), ("MIA", 1), ("SFO", 1)],
        "ORD": [("MIA", 1), ("DFW", 1)],
        "JFK": [("BOS", 1), ("SFO", 1), ("MIA", 1), ("DFW", 1)],
        "DFW": [("ORD", 1), ("SFO", 1), ("LAX", 1)],
        "MIA": [("DFW", 1), ("LAX", 1)],
        "SFO": [("LAX", 1)],
        "LAX": [("ORD", 1)],
    }
    _test(
        sorted(listOfNodes(G)),
        sorted(["BOS", "ORD", "JFK", "DFW", "MIA", "SFO", "LAX"]),
    )


def listOfEdges_testcases():
    G = {
        0: [(1, 1), (2, 1)],
        1: [(2, 1), (3, 1)],
        2: [(4, 1)],
        3: [(4, 1), (5, 1)],
        4: [(5, 1)],
        5: [],
    }
    _test(
        sorted(listOfEdges(G, True)),
        sorted(
            [
                (0, 1, 1),
                (0, 2, 1),
                (1, 2, 1),
                (1, 3, 1),
                (2, 4, 1),
                (3, 4, 1),
                (3, 5, 1),
                (4, 5, 1),
            ]
        ),
    )

    ##############################################################################################

    G = {
        0: [(1, 1), (2, 1)],
        1: [(0, 1), (2, 1), (3, 1)],
        2: [(0, 1), (1, 1), (4, 1)],
        3: [(1, 1), (4, 1), (5, 1)],
        4: [(3, 1), (2, 1), (5, 1)],
        5: [(3, 1), (4, 1)],
    }
    _test_listofedges(
        sorted(listOfEdges(G, False)),
        sorted(
            [
                (0, 1, 1),
                (0, 2, 1),
                (1, 2, 1),
                (1, 3, 1),
                (2, 4, 1),
                (3, 4, 1),
                (3, 5, 1),
                (4, 5, 1),
            ]
        ),
    )

    ##############################################################################################

    G = {
        "BOS": [("JFK", 1), ("MIA", 1), ("SFO", 1)],
        "ORD": [("MIA", 1), ("DFW", 1)],
        "JFK": [("BOS", 1), ("SFO", 1), ("MIA", 1), ("DFW", 1)],
        "DFW": [("ORD", 1), ("SFO", 1), ("LAX", 1)],
        "MIA": [("DFW", 1), ("LAX", 1)],
        "SFO": [("LAX", 1)],
        "LAX": [("ORD", 1)],
    }
    _test(
        sorted(listOfEdges(G, True)),
        sorted(
            [
                ("BOS", "JFK", 1),
                ("BOS", "MIA", 1),
                ("BOS", "SFO", 1),
                ("ORD", "MIA", 1),
                ("ORD", "DFW", 1),
                ("JFK", "BOS", 1),
                ("JFK", "SFO", 1),
                ("JFK", "MIA", 1),
                ("JFK", "DFW", 1),
                ("DFW", "ORD", 1),
                ("DFW", "SFO", 1),
                ("DFW", "LAX", 1),
                ("MIA", "DFW", 1),
                ("MIA", "LAX", 1),
                ("SFO", "LAX", 1),
                ("LAX", "ORD", 1),
            ]
        ),
    )

    ##############################################################################################

    G = {
        "BOS": [("JFK", 1), ("MIA", 1), ("SFO", 1)],
        "ORD": [("MIA", 1), ("DFW", 1), ("LAX", 1)],
        "JFK": [("BOS", 1), ("SFO", 1), ("MIA", 1), ("DFW", 1)],
        "DFW": [("JFK", 1), ("ORD", 1), ("MIA", 1), ("SFO", 1), ("LAX", 1)],
        "MIA": [("BOS", 1), ("JFK", 1), ("ORD", 1), ("DFW", 1), ("LAX", 1)],
        "SFO": [("BOS", 1), ("JFK", 1), ("DFW", 1), ("LAX", 1)],
        "LAX": [("MIA", 1), ("DFW", 1), ("SFO", 1), ("ORD", 1)],
    }
    _test_listofedges(
        sorted(listOfEdges(G, False)),
        sorted(
            [
                ("BOS", "JFK", 1),
                ("BOS", "MIA", 1),
                ("BOS", "SFO", 1),
                ("ORD", "MIA", 1),
                ("ORD", "DFW", 1),
                ("ORD", "LAX", 1),
                ("JFK", "SFO", 1),
                ("JFK", "MIA", 1),
                ("JFK", "DFW", 1),
                ("DFW", "MIA", 1),
                ("DFW", "SFO", 1),
                ("DFW", "LAX", 1),
                ("MIA", "LAX", 1),
                ("SFO", "LAX", 1),
            ]
        ),
    )


def getNeighbours_testcases():
    G = {
        0: [(1, 1), (2, 1)],
        1: [(0, 1), (2, 1), (3, 1)],
        2: [(0, 1), (1, 1), (4, 1)],
        3: [(1, 1), (4, 1), (5, 1)],
        4: [(3, 1), (2, 1), (5, 1)],
        5: [(3, 1), (4, 1)],
    }
    _test(sorted(getNeighbours(G, 0)), sorted([1, 2]))

    ##############################################################################################

    G = {
        "BOS": [("JFK", 1), ("MIA", 1), ("SFO", 1)],
        "ORD": [("MIA", 1), ("DFW", 1), ("LAX", 1)],
        "JFK": [("BOS", 1), ("SFO", 1), ("MIA", 1), ("DFW", 1)],
        "DFW": [("JFK", 1), ("ORD", 1), ("MIA", 1), ("SFO", 1), ("LAX", 1)],
        "MIA": [("BOS", 1), ("JFK", 1), ("ORD", 1), ("DFW", 1), ("LAX", 1)],
        "SFO": [("BOS", 1), ("JFK", 1), ("DFW", 1), ("LAX", 1)],
        "LAX": [("MIA", 1), ("DFW", 1), ("SFO", 1), ("ORD", 1)],
    }
    _test(sorted(getNeighbours(G, "JFK")), sorted(["BOS", "SFO", "MIA", "DFW"]))


def removeNode_testcases():
    G = {
        0: [(1, 1), (2, 1)],
        1: [(2, 1), (3, 1)],
        2: [(4, 1)],
        3: [(4, 1), (5, 1)],
        4: [(5, 1)],
        5: [],
    }
    removeNode(G, 1)
    _test(G, {0: [(2, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: []})

    ###########################################################################################################

    G = {
        0: [(1, 1), (2, 1)],
        1: [(0, 1), (2, 1), (3, 1)],
        2: [(0, 1), (1, 1), (4, 1)],
        3: [(1, 1), (4, 1), (5, 1)],
        4: [(3, 1), (2, 1), (5, 1)],
        5: [(3, 1), (4, 1)],
    }
    removeNode(G, 1)
    _test(
        G,
        {
            0: [(2, 1)],
            2: [(0, 1), (4, 1)],
            3: [(4, 1), (5, 1)],
            4: [(3, 1), (2, 1), (5, 1)],
            5: [(3, 1), (4, 1)],
        },
    )

    ###########################################################################################################

    G = {
        "BOS": [("JFK", 1), ("MIA", 1), ("SFO", 1)],
        "ORD": [("MIA", 1), ("DFW", 1), ("LAX", 1)],
        "JFK": [("BOS", 1), ("SFO", 1), ("MIA", 1), ("DFW", 1)],
        "DFW": [("JFK", 1), ("ORD", 1), ("MIA", 1), ("SFO", 1), ("LAX", 1)],
        "MIA": [("BOS", 1), ("JFK", 1), ("ORD", 1), ("DFW", 1), ("LAX", 1)],
        "SFO": [("BOS", 1), ("JFK", 1), ("DFW", 1), ("LAX", 1)],
        "LAX": [("MIA", 1), ("DFW", 1), ("SFO", 1), ("ORD", 1)],
    }
    removeNode(G, "DFW")
    _test(
        G,
        {
            "BOS": [("JFK", 1), ("MIA", 1), ("SFO", 1)],
            "ORD": [("MIA", 1), ("LAX", 1)],
            "JFK": [("BOS", 1), ("SFO", 1), ("MIA", 1)],
            "MIA": [("BOS", 1), ("JFK", 1), ("ORD", 1), ("LAX", 1)],
            "SFO": [("BOS", 1), ("JFK", 1), ("LAX", 1)],
            "LAX": [("MIA", 1), ("SFO", 1), ("ORD", 1)],
        },
    )


def removeNodes_testcases():
    G = {
        0: [(1, 1), (2, 1)],
        1: [(2, 1), (3, 1)],
        2: [(4, 1)],
        3: [(4, 1), (5, 1)],
        4: [(5, 1)],
        5: [],
    }
    removeNodes(G, [1, 2])
    _test(G, {0: [], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: []})

    ###########################################################################################################

    G = {
        "BOS": [("JFK", 1), ("MIA", 1), ("SFO", 1)],
        "ORD": [("MIA", 1), ("DFW", 1), ("LAX", 1)],
        "JFK": [("BOS", 1), ("SFO", 1), ("MIA", 1), ("DFW", 1)],
        "DFW": [("JFK", 1), ("ORD", 1), ("MIA", 1), ("SFO", 1), ("LAX", 1)],
        "MIA": [("BOS", 1), ("JFK", 1), ("ORD", 1), ("DFW", 1), ("LAX", 1)],
        "SFO": [("BOS", 1), ("JFK", 1), ("DFW", 1), ("LAX", 1)],
        "LAX": [("MIA", 1), ("DFW", 1), ("SFO", 1), ("ORD", 1)],
    }
    removeNodes(G, ["MIA", "LAX"])
    _test(
        G,
        {
            "BOS": [("JFK", 1), ("SFO", 1)],
            "ORD": [("DFW", 1)],
            "JFK": [("BOS", 1), ("SFO", 1), ("DFW", 1)],
            "DFW": [("JFK", 1), ("ORD", 1), ("SFO", 1)],
            "SFO": [("BOS", 1), ("JFK", 1), ("DFW", 1)],
        },
    )


def getNearestNeighbor_testcases():
    G = {
        0: [(1, 21), (2, 15)],
        1: [(0, 21), (2, 10), (3, 70)],
        2: [(0, 15), (1, 10), (4, 50)],
        3: [(1, 70), (4, 24), (5, 39)],
        4: [(3, 24), (2, 50), (5, 99)],
        5: [(3, 39), (4, 99)],
    }
    _test(getNearestNeighbor(G, 0), 2)

    ###########################################################################################################

    G = {
        "BOS": [("JFK", 1), ("MIA", 1), ("SFO", 1)],
        "ORD": [("MIA", 1), ("DFW", 1), ("LAX", 1)],
        "JFK": [("BOS", 1), ("SFO", 1), ("MIA", 1), ("DFW", 1)],
        "DFW": [("JFK", 1), ("ORD", 1), ("MIA", 1), ("SFO", 1), ("LAX", 1)],
        "MIA": [("BOS", 1), ("JFK", 1), ("ORD", 1), ("DFW", 1), ("LAX", 1)],
        "SFO": [("BOS", 1), ("JFK", 1), ("DFW", 1), ("LAX", 1)],
        "LAX": [("MIA", 1), ("DFW", 1), ("SFO", 1), ("ORD", 1)],
    }
    _test(getNearestNeighbor(G, "SFO"), "BOS")


def main():
    print("addNodes testcases")
    addNodes_testcases()

    print("addEdges testcases")
    addEdges_testcases()

    print("listOfNodes testcases")
    listOfNodes_testcases()

    print("listOfEdges testcases")
    listOfEdges_testcases()

    print("getNeighbours testcases")
    getNeighbours_testcases()

    print("removeNode testcases")
    removeNode_testcases()

    print("removeNodes testcases")
    removeNodes_testcases()

    print("getNearestNeighbor testcases")
    getNearestNeighbor_testcases()


# main()
