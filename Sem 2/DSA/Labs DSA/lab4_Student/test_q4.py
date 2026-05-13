import pytest
import hashlib
from q4 import *

q4_testcases = [
    # Visible Testcases
    ([1, 2, 3], 2, [1, 1, 2, 2, 3, 3], True),
    (['a', 'b', 'c'], 3, ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'], True),
    (["queue"], 10, ['queue', 'queue', 'queue', 'queue', 'queue', 'queue', 'queue', 'queue', 'queue', 'queue'], True),

    # Hidden Testcases
    (['a', 'b', 'c'], 2, "253850a2e327ae961242ad808aef20dc3d2dd13336801730e3b69c5613df846d", False),
    ([2, 'a', False], 2, "50822226e42844100e405aebcf2f20ffaa126b11b73a7762f761d42b51fc481f", False),
    ([10, 20], 4,"53badcf8cbe44d3b4c46bc6c4369e4064fe291dacc42aef08850862273fbed6c", False)
    ]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("A,n,result,testcase", q4_testcases)
def test_q4(A, n, result,testcase):
    if testcase == True:
        assert stutter(A, n) == result
    else:
        assert hashcode(stutter(A, n)) == result