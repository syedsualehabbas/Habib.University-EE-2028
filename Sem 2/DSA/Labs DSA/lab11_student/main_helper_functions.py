from helper_functions import *

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
        print(prefix)
    else:
        prefix = '  X '
        print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def test_listofedges(got, expectedLst):
    if got == expectedLst:
        prefix = ' OK '
        print(prefix)
    else:
        prefix = '  X '
        print('%s got: %s expected one of these outputs: %s' % (prefix, repr(got), repr(expectedLst)))

def in_out_degree_testcases():
    G ={ 0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: [] }
    test(in_out_degree(G), {0: (0, 2), 1: (1, 2), 2: (2, 1), 3: (1, 2), 4: (2, 1), 5: (2, 0)})

    G = {'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'ORD': [('MIA', 1), ('DFW', 1)], 'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 'MIA': [('DFW', 1), ('LAX', 1)], 'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] }
    test(in_out_degree(G), {'BOS': (1, 3), 'ORD': (2, 2), 'JFK': (1, 4), 'DFW': (3, 3), 'MIA': (3, 2), 'SFO': (3, 1), 'LAX': (3, 1)})

def degree_testcases():
    G = { 0: [(1, 1), (2, 1)], 1: [(0, 1), (2, 1), (3, 1)], 2: [(0, 1), (1, 1), (4, 1)], 3: [(1, 1), (4, 1), (5, 1)], 4: [(3, 1), (2, 1), (5, 1)], 5: [(3, 1), (4, 1)] }
    test(degree(G), {0: 2, 1: 3, 2: 3, 3: 3, 4: 3, 5: 2})

    G = {'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'ORD': [('MIA', 1), ('DFW', 1), ('LAX', 1)], 'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 'DFW': [('JFK', 1), ('ORD', 1), ('MIA', 1), ('SFO', 1), ('LAX', 1)], 'MIA': [('BOS', 1), ('JFK', 1), ('ORD', 1), ('DFW', 1), ('LAX', 1)], 'SFO': [('BOS', 1), ('JFK', 1), ('DFW', 1), ('LAX', 1)], 'LAX': [('MIA', 1), ('DFW', 1), ('SFO', 1), ('ORD', 1)]}
    test(degree(G), {'BOS': 3, 'ORD': 3, 'JFK': 4, 'DFW': 5, 'MIA': 5, 'SFO': 4, 'LAX': 4})

def getInNeighbors_testcases():
    G ={ 0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: [] }
    test(sorted(getInNeighbors(G, 0)), [])

    G ={ 0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: [] }
    test(sorted(getInNeighbors(G, 2)), [0, 1])

    G = {'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'ORD': [('MIA', 1), ('DFW', 1)], 'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 'MIA': [('DFW', 1), ('LAX', 1)], 'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] }
    test(sorted(getInNeighbors(G, "ORD")), sorted(['DFW', 'LAX']))

    G = {'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'ORD': [('MIA', 1), ('DFW', 1)], 'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 'MIA': [('DFW', 1), ('LAX', 1)], 'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] }
    test(sorted(getInNeighbors(G, "MIA")), sorted(['BOS', 'ORD', 'JFK']))

def getOutNeighbors_testcases():
    G ={ 0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: [] }
    test(sorted(getOutNeighbors(G, 0)), sorted([1, 2]))

    G ={ 0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: [] }
    test(sorted(getOutNeighbors(G, 5)), sorted([]))

    G = {'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'ORD': [('MIA', 1), ('DFW', 1)], 'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 'MIA': [('DFW', 1), ('LAX', 1)], 'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] }
    test(sorted(getOutNeighbors(G, "DFW")), sorted(['ORD', 'SFO', 'LAX']))

    G = {'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'ORD': [('MIA', 1), ('DFW', 1)], 'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 'MIA': [('DFW', 1), ('LAX', 1)], 'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] }
    test(sorted(getOutNeighbors(G, "LAX")), sorted(['ORD']))

def isNeighbor_testcases():
    G ={ 0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: [] }
    test(isNeighbor(G, 0, 1), True)

    G ={ 0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: [] }
    test(isNeighbor(G, 1, 0), False)

    G ={ 0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: [] }
    test(isNeighbor(G, 1, 0), False)

    G = {'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'ORD': [('MIA', 1), ('DFW', 1)], 'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 'MIA': [('DFW', 1), ('LAX', 1)], 'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] }
    test(isNeighbor(G, "DFW", "MIA"), False)

    G = {'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'ORD': [('MIA', 1), ('DFW', 1)], 'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 'MIA': [('DFW', 1), ('LAX', 1)], 'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] }
    test(isNeighbor(G, "SFO", "LAX"), True)

    G = {'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'ORD': [('MIA', 1), ('DFW', 1)], 'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 'MIA': [('DFW', 1), ('LAX', 1)], 'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] }
    test(isNeighbor(G, "LAX", "SFO"), False)

def adjlst_to_adj_matrix_testcases():
    G ={ 0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: [] }
    test(adjlst_to_adj_matrix(G), [[-1, 1, 1, -1, -1, -1], [-1, -1, 1, 1, -1, -1], [-1, -1, -1, -1, 1, -1], [-1, -1, -1, -1, 1, 1], [-1, -1, -1, -1, -1, 1], [-1, -1, -1, -1, -1, -1]])

    G = {'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'ORD': [('MIA', 1), ('DFW', 1)], 'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 'MIA': [('DFW', 1), ('LAX', 1)], 'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] }
    test(adjlst_to_adj_matrix(G), [[-1, -1, 1, -1, 1, 1, -1], [-1, -1, -1, 1, 1, -1, -1], [1, -1, -1, 1, 1, 1, -1], [-1, 1, -1, -1, -1, 1, 1], [-1, -1, -1, 1, -1, -1, 1], [-1, -1, -1, -1, -1, -1, 1], [-1, 1, -1, -1, -1, -1, -1]])

    G = { 0: [(1, 1), (2, 1)], 1: [(0, 1), (2, 1), (3, 1)], 2: [(0, 1), (1, 1), (4, 1)], 3: [(1, 1), (4, 1), (5, 1)], 4: [(3, 1), (2, 1), (5, 1)], 5: [(3, 1), (4, 1)] }
    test(adjlst_to_adj_matrix(G), [[-1, 1, 1, -1, -1, -1], [1, -1, 1, 1, -1, -1], [1, 1, -1, -1, 1, -1], [-1, 1, -1, -1, 1, 1], [-1, -1, 1, 1, -1, 1], [-1, -1, -1, 1, 1, -1]])

    G = {'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'ORD': [('MIA', 1), ('DFW', 1), ('LAX', 1)], 'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 'DFW': [('JFK', 1), ('ORD', 1), ('MIA', 1), ('SFO', 1), ('LAX', 1)], 'MIA': [('BOS', 1), ('JFK', 1), ('ORD', 1), ('DFW', 1), ('LAX', 1)], 'SFO': [('BOS', 1), ('JFK', 1), ('DFW', 1), ('LAX', 1)], 'LAX': [('MIA', 1), ('DFW', 1), ('SFO', 1), ('ORD', 1)]}
    test(adjlst_to_adj_matrix(G), [[-1, -1, 1, -1, 1, 1, -1], [-1, -1, -1, 1, 1, -1, 1], [1, -1, -1, 1, 1, 1, -1], [-1, 1, 1, -1, 1, 1, 1], [1, 1, 1, 1, -1, -1, 1], [1, -1, 1, 1, -1, -1, 1], [-1, 1, -1, 1, 1, 1, -1]])

def csv_to_adj_list_testcases():
    test(csv_to_adj_list("connections.csv"), {'Islamabad': [('Taxila', 46), ('Murree', 49)], 'Taxila': [('Islamabad', 46), ('Abbottabad', 74), ('Malam Jabba', 254)], 'Murree': [('Islamabad', 49), ('Nathiagali', 36), ('Muzaffarabad', 68)], 'Nathiagali': [('Murree', 36), ('Abbottabad', 34)], 'Abbottabad': [('Taxila', 74), ('Nathiagali', 34), ('Mansehra', 23)], 'Mansehra': [('Abbottabad', 23), ('Balakot', 37), ('Bisham', 113)], 'Balakot': [('Mansehra', 37), ('Kaghan', 59), ('Bisham', 136)], 'Kaghan': [('Balakot', 59), ('Naran', 22)], 'Naran': [('Kaghan', 22), ('Chilas', 113)], 'Chilas': [('Naran', 113), ('Bisham', 199), ('Gilgit', 133), ('Hunza', 306)], 'Bisham': [('Mansehra', 113), ('Balakot', 136), ('Chilas', 199), ('Malam Jabba', 61)], 'Gilgit': [('Chilas', 133), ('Hunza', 186), ('Skardu', 208)], 'Hunza': [('Chilas', 306), ('Gilgit', 186), ('Khunjerab Pass', 151), ('Skardu', 381)], 'Khunjerab Pass': [('Hunza', 151)], 'Malam Jabba': [('Taxila', 254), ('Bisham', 61)], 'Skardu': [('Gilgit', 208), ('Hunza', 381), ('Muzaffarabad', 484)], 'Muzaffarabad': [('Murree', 68), ('Skardu', 484)]})

def main():
    print("in_out_degree testcases")
    in_out_degree_testcases()

    print("degree testcases")
    degree_testcases()

    print("getInNeighbors testcases")
    getInNeighbors_testcases()

    print("getOutNeighbors testcases")
    getOutNeighbors_testcases()

    print("isNeighbor testcases")
    isNeighbor_testcases()

    print("adjlst_to_adj_matrix testcases")
    adjlst_to_adj_matrix_testcases()

    print("csv_to_adj_list testcases")
    csv_to_adj_list_testcases()

main()