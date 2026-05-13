import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q4 import *

# Note the Graphs used in the test cases is not
# the same as the graphs in the previous questions
q4_testcases = [
    # VISIBLE TESTCASES
    ({'s': [(1, 1), (2, 1)], 1: [(3, 1), (4, 1), (5, 1)], 2: [(6, 1)], 3: [], 4: [], 5: [], 6: [(7, 1)], 7: []}, 1, [1, 2], True),
    ({'s': [(1, 1), (2, 1)], 1: [(3, 1), (4, 1), (5, 1)], 2: [(6, 1)], 3: [], 4: [], 5: [], 6: [(7, 1)], 7: []}, 2, [3, 4, 5, 6], True),
    ({'s': [(1, 1), (2, 1)], 1: [(3, 1), (4, 1), (5, 1)], 2: [(6, 1)], 3: [], 4: [], 5: [], 6: [(7, 1)], 7: []}, 3, [7], True),
    ({'Dallas': [('Austin', 200), ('Denver', 780), ('Washington', 1300)], 'Austin': [('Houston', 160), ('Chicago', 900)], 'Washington': [('Atlanta', 600)], 'Denver': [], 'Atlanta': [], 'Chicago': [], 'Houston': []}, 1, ['Austin', 'Denver', 'Washington'], True),
    ({'Dallas': [('Austin', 200), ('Denver', 780), ('Washington', 1300)], 'Austin': [('Houston', 160), ('Chicago', 900)], 'Washington': [('Atlanta', 600)], 'Denver': [], 'Atlanta': [], 'Chicago': [], 'Houston': []}, 2, ['Atlanta', 'Chicago', 'Houston'], True),
    
    # HIDDEN TESTCASES
    ({'Dallas': [('Austin', 200), ('Denver', 780), ('Washington', 1300)], 'Austin': [('Houston', 160), ('Chicago', 900)], 'Washington': [('Atlanta', 600)], 'Denver': [], 'Atlanta': [], 'Chicago': [], 'Houston': []}, 3, "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", False), 
    ({'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'JFK': [('DFW', 1)], 'MIA': [('LAX', 1), ('ORD', 1)], 'SFO': [], 'ORD': [], 'DFW': [], 'LAX': [('MAX', 1), ('HAX', 1)], 'HAX': [], 'MAX': []}, 1, "8d7c73da8d28a59bcba24359cfaf5aa3302edc857ba0ba727edd9c893b4ca16b", False),
    ({'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'JFK': [('DFW', 1)], 'MIA': [('LAX', 1), ('ORD', 1)], 'SFO': [], 'ORD': [], 'DFW': [], 'LAX': [('MAX', 1), ('HAX', 1)], 'HAX': [], 'MAX': []}, 2, "2451fb44c2c4dcd6e76d61f5efa45cebb1cb945db8e6a48995f0b593621bc4f1", False),
    ({'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'JFK': [('DFW', 1)], 'MIA': [('LAX', 1), ('ORD', 1)], 'SFO': [], 'ORD': [], 'DFW': [], 'LAX': [('MAX', 1), ('HAX', 1)], 'HAX': [], 'MAX': []}, 3, "33c3278b0b171033998c129d3d3b4cfc04ec0a177497144b02108d90e38d6602", False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()


@pytest.mark.parametrize("inp, start, result, testcase", q4_testcases)
def test_q4(inp, start, result, testcase):
    # print(sorted(nodes_of_level(inp, start)), hashcode(sorted(nodes_of_level(inp, start))))
    if testcase == True:
        assert sorted(nodes_of_level(inp, start)) == result
    else:
        assert hashcode(sorted(nodes_of_level(inp, start))) == result