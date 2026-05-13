import pytest
import hashlib
from q1 import *

q1_testcases = [
    # Visible Testcases
    (5, ([None, None, None, None, None], [None, None, None, None, None]), True),
    (15, ([None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]), True),

    # Hidden Testcases
    (1000,'c13d5a1ba8f31a1d9d229a99cdbe20b266ed5b0e41894b953dbed8aca831b6a0', False),
    (0, '1391876e63685b7da0e6a923dc6c4c106590930a70cdf4665088614cae243c44', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("size,result,testcase",q1_testcases)
def test_q1(size, result,testcase):
    if testcase == True:
        assert create_hashtable(size) == result
    else:
        assert hashcode(create_hashtable(size)) == result