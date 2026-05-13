import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q2 import *

q2_testcases = [
    # VISIBLE TESTCASES
    ({'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Washington': [('Dallas', 1300), ('Atlanta', 600)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Washington', 600), ('Houston', 800)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}, ['Dallas','Denver','Atlanta','Washington'], True, True),
    ({'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'ORD': [('MIA', 1), ('DFW', 1)], 'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 'MIA': [('DFW', 1), ('LAX', 1)], 'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] }, ['BOS', 'MIA', 'JFK'], False, True),
    ({'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 'ORD': [('MIA', 1), ('DFW', 1)], 'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 'MIA': [('DFW', 1), ('LAX', 1)], 'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] }, ['JFK','MIA', 'DFW'], False, True),

    # HIDDEN TESTCASES
    ({'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Washington': [('Dallas', 1300), ('Atlanta', 600)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Washington', 600), ('Houston', 800)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}, ['Dallas','Atlanta','Washington'], "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe", False),
    ({'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Washington': [('Dallas', 1300), ('Atlanta', 600)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Washington', 600), ('Houston', 800)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}, ['Austin','Houston', 'Atlanta', 'Washington', 'Dallas'], "3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18", False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()

@pytest.mark.parametrize("inp, start, result, testcase", q2_testcases)
def test_q2(inp, start, result, testcase):
    if testcase == True:
        assert check_cycles(inp, start) == result
    else:
        assert hashcode(check_cycles(inp, start)) == result
