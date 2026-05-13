import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q3 import *

q3_testcases = [
    # VISIBLE TESTCASES
    ({'s': [(1, 1), (2, 1)], 1: [(3, 1), (4, 1), (5, 1)], 2: [(6, 1)], 3: [], 4: [], 5: [], 6: [(7, 1)], 7: []}, 's', ['s', 1, 2, 3, 4, 5, 6, 7], True),
    ({'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'ORD': [('MIA', 1), ('DFW', 1)], 'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 'MIA': [('DFW', 1), ('LAX', 1)], 'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] },'BOS', ['BOS', 'JFK', 'MIA', 'SFO', 'DFW', 'LAX', 'ORD'], True),
    ({'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'ORD': [('MIA', 1), ('DFW', 1)], 'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 'MIA': [('DFW', 1), ('LAX', 1)], 'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] },'MIA', ['MIA', 'DFW', 'LAX', 'ORD', 'SFO'], True),
    ({'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'ORD': [('MIA', 1), ('DFW', 1)], 'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 'MIA': [('DFW', 1), ('LAX', 1)], 'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] }, 'JFK', ['JFK', 'BOS', 'SFO', 'MIA', 'DFW', 'LAX', 'ORD'], True),

    # HIDDEN TESTCASES
    ({'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Washington': [('Dallas', 1300), ('Atlanta', 600)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Washington', 600), ('Houston', 800)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}, "Austin", "68b2b263030f7e99f38b7b85033af488bbac603ef152917136ac7ac61ec09f2b", False),
    ({'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Washington': [('Dallas', 1300), ('Atlanta', 600)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Washington', 600), ('Houston', 800)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}, "Chicago", "e7e3939d881265f81d68e5cd024249f27b472fd5b7da4264c7f6c9089015a279", False),
    ({0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: []}, 0, "b0229c06acf4d5c98db175d4d054cd39e7fff51d8c37754b4a4b424f7967710d", False),
    ({0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: []}, 1, "0c049903ce2330190375d4c1f2e489888c9ebe39daf75b2564e591e8bc1afe72", False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()


@pytest.mark.parametrize("inp, start, result, testcase", q3_testcases)
def test_q3(inp, start, result, testcase):
    if testcase == True:
        assert BFS(inp, start) == result
    else:
        assert hashcode(BFS(inp, start)) == result
