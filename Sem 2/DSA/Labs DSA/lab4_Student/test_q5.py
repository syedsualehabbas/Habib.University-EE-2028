import pytest
import hashlib
from q5 import *

q5_testcases = [
    # Visible Testcases
    ("( A + B ) * ( C + D )", "A B + C D + *", True),
    ("A * B + C * D", "A B * C D * +", True),
    ("A * B + C", "A B * C +", True),
    ("A * ( B + C )", "A B C + *", True),
    ("( A + B ) * C - ( D - E ) * ( F + G )", "A B + C * D E - F G + * -", True),    
    ("( ( ( A + B ) * C ) - ( ( D - E ) * ( F + G ) ) )", "A B + C * D E - F G + * -", True),
    ("( P + Q ) * ( M - N )", "P Q + M N - *", True),

    # Hidden Testcases
    ("( P + Q ) / ( M - N ) - ( A * B )", "0cdff534743663022c3111b18fe502df368851808be917be2c710c4db6a96e21", False),
    ("X + Y", "1d3f8bc14474b9b14400fe078381a09c6a9978c83f20e6a30dfd9bdd03b2866c", False),
    ("X + Y * Z", "5ef92da34864a8c395b2073619ab25978137fb42d8b4033faf4cac3d6c42a87a", False),
    ("( X + Y ) * Z", "84f9c680888f4bc1b1df04d24e19ce90062b6c0fbe9c72b8ad2ff8ff9f972802", False),
    ("A + B * C + D", "4205141e00310a4ecb039bc1fcaf35ea43731e764cf6f8c3de988dba5c8c0527", False),
    ("A + B + C + D", "80642afdc7b874b689d126a573654f978b2c46ba7af895467f2d71532fe95bea", False),
    ("( A + B ) * C", "f8b44969acd1947d2f085d059d2b610f0d191b712b70f398b17e120bd8c3e2e6", False),
    ("a + b * c - ( d / e + f * g * h )", "5e739bb70342522ae258f1b86fcd7b5bbc635d41d08fc19abe69341fdb2956bf", False)
    ]


def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()


@pytest.mark.parametrize("inp,result,testcase", q5_testcases)
def test_q5(inp, result, testcase):
    if testcase==True:
        assert Infix_to_Postfix(inp) == result
    else:
        assert hashcode(Infix_to_Postfix(inp)) == result