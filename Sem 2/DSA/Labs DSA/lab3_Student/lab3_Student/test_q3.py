import hashlib

import pytest
from q3 import Remove


remove_testcases = [
    # Visible Testcases
    (
        [10, 20, 30, 40, 50],
        2,
        "Element removed successfully",
        [10, 20, 40, 50, None],
        True,
    ),
    (
        [10, 20, 40, 50, None],
        0,
        "Element removed successfully",
        [20, 40, 50, None, None],
        True,
    ),
    ([20, 40, 50, None, None], 5, "Invalid Index", [20, 40, 50, None, None], True),
    ([20, 40, 50, None, None], 3, "Invalid Index", [20, 40, 50, None, None], True),
    ([20, 40, 50, None, None], 4, "Invalid Index", [20, 40, 50, None, None], True),
    ([None, None, None, None], 0, "List is empty", [None, None, None, None], True),
    (["a", "b"], 0, "Element removed successfully", ["b", None], True),
    (["a"], 0, "Element removed successfully", [None], True),
    # Hidden Testcases
    (
        [10, 20, 30, 40, 50],
        4,
        "d8116103aeebda02e83f02448224e17cb44a78f61747ec2357fdd963ea986d10",
        "0837a13dc6529ae8a355c2f53ce26ed59c0a62cad8d05cdb36c8c19d48111657",
        False,
    ),
    (
        [20, 40, 50, None, None],
        -1,
        "a88ada13a2d454eaa7f2363f7c06c19d8328d10306baffb71139c2081bf35128",
        "b79fab235453230e8ea3fc56ca8afa677cc88c35d916392312ae3998487d5208",
        False,
    ),
    (
        [None],
        0,
        "ba61eea246993d3ff552ff2645a632e9b743d05d0dd96a5cf93f3b472ab69c8a",
        "778d5d27b716881dd9d3b58baaed62878f93076984cf0cbb45d393bedf363cb2",
        False,
    ),
    (
        ["a", "b"],
        1,
        "d8116103aeebda02e83f02448224e17cb44a78f61747ec2357fdd963ea986d10",
        "3ab8d220bfe98366a8885ea3d26ff7bc8e1b4377e5fc080ab3a1f32354aa3175",
        False,
    ),
    (
        [20, 40, 50, None, None, None],
        5,
        "a88ada13a2d454eaa7f2363f7c06c19d8328d10306baffb71139c2081bf35128",
        "325b54d1562c95dd3b1b2fd6f0cb65f9bc1ee18a63e063a306c30ee7665e04f8",
        False,
    ),
    (
        [20, 40, 50, None, None, None],
        4,
        "a88ada13a2d454eaa7f2363f7c06c19d8328d10306baffb71139c2081bf35128",
        "325b54d1562c95dd3b1b2fd6f0cb65f9bc1ee18a63e063a306c30ee7665e04f8",
        False,
    ),
]


def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()


@pytest.mark.parametrize("list,index,output,result,testcase", remove_testcases)
def test_Remove(list, index, output, result, testcase):
    if testcase:
        assert Remove(list, index) == output and list == result
    else:
        assert hashcode(Remove(list, index)) == output and hashcode(list) == result
