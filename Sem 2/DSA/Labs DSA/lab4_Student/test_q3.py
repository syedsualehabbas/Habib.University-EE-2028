import pytest
import hashlib
from q3 import *

q3_testcases = [
    # Visible Testcases
    ("()", True, True),
    ("())", False, True),
    ("{()}", True, True),
    ("{)({", False, True),
    ("{()}[]()", True, True),
    ("{[}]", False, True),
    ("()()()([{])}({{[]}})", False, True),

    # Hidden Testcases
    ("]", "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe", False),
    ("(){}}{", "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe", False),
    ("[])", "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe", False),
    ("(])", "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe", False),
    ("([}}])", "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe", False),
    ("[](])", "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe", False),
    ("[", "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe", False),
    ("[[[[[[(((([{{{{{{[[[[", "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe", False)
]


def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()


@pytest.mark.parametrize("inp,result,testcase", q3_testcases)
def test_q3(inp, result,testcase):
    if testcase == True:
        assert balanced_braces(inp) == result
    else:
        assert hashcode(balanced_braces(inp)) == result