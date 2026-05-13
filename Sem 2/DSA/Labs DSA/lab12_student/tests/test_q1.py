import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import *

q1_testcases = [
    # VISIBLE TESTCASES
    ({0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: []}, 0, [0, 2, 4, 5, 1, 3], True),
    ({0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: []}, 1, [1, 3, 5, 4, 2], True),
    ({'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'ORD': [('MIA', 1), ('DFW', 1)], 'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 'MIA': [('DFW', 1), ('LAX', 1)], 'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] }, 'BOS', ['BOS', 'SFO', 'LAX', 'ORD', 'DFW', 'MIA', 'JFK'], True),
    ({'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'ORD': [('MIA', 1), ('DFW', 1)], 'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 'MIA': [('DFW', 1), ('LAX', 1)], 'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] }, 'MIA', ['MIA', 'LAX', 'ORD', 'DFW', 'SFO'], True),
        
    # HIDDEN TESTCASES
    ({'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'ORD': [('MIA', 1), ('DFW', 1)], 'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 'MIA': [('DFW', 1), ('LAX', 1)], 'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] }, 'JFK', "a750464aa7e611b565ec9adabdc4e4e7343f615abacfcbcbeec9bb4e361453bb", False),
    ({'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Washington': [('Dallas', 1300), ('Atlanta', 600)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Washington', 600), ('Houston', 800)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}, "Dallas", "4bcc02f15a05578d78a37bb117771261e358708ae89af36603342cf3db631503", False),
    ({'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Washington': [('Dallas', 1300), ('Atlanta', 600)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Washington', 600), ('Houston', 800)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}, "Chicago", "8d71786757c521d5e381f1217489e0324f6e727c0133912a4b817935fc122fcf", False)
]


def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()


@pytest.mark.parametrize("inp, start, result, testcase", q1_testcases)
def test_q1(inp, start, result, testcase):
    if testcase == True:
        assert DFS(inp, start) == result
    else:
        assert hashcode(DFS(inp, start)) == result