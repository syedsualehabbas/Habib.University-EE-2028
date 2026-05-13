import hashlib

import pytest
from q1 import Get, Initialize, IsEmpty, IsFull, NumberOfElements, Set, Size


Initialize_testcases = [
    # Visible Testcases
    (5, [None, None, None, None, None], True),
    (3, [None, None, None], True),
    # Hidden Testcases
    (0, "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", False),
    (1, "778d5d27b716881dd9d3b58baaed62878f93076984cf0cbb45d393bedf363cb2", False),
]
Get_testcases = [
    # Visible Testcases
    ([10, 20, 30, 40, 50], 0, 10, True),
    ([10, 20, 30, 40, 50], 1, 20, True),
    # Hidden Testcases
    (
        [10, 20, 30, 40, 50],
        2,
        "624b60c58c9d8bfb6ff1886c2fd605d2adeb6ea4da576068201b6c6958ce93f4",
        False,
    ),
    (
        [10, 20, 30, 40, 50],
        3,
        "d59eced1ded07f84c145592f65bdf854358e009c5cd705f5215bf18697fed103",
        False,
    ),
]

Set_testcases = [
    # Visible Testcases
    ([10, 20, 30, 40, 50], 0, 60, [60, 20, 30, 40, 50], True),
    ([10, 20, 30, 40, 50], 1, 60, [10, 60, 30, 40, 50], True),
    # Hidden Testcases
    (
        [10, 20, 30, 40, 50],
        2,
        60,
        "abf8ed3903d4b113230ac53a0e0295eda5dafa4bfd81643130eba33eca47f752",
        False,
    ),
    (
        [10, 20, 30, 40, 50],
        3,
        60,
        "84c1004425e0eae2afdcf73cec807514276ceff51d48a29b343e14087fec235f",
        False,
    ),
]

Size_testcases = [
    # Visible Testcases
    ([10, 20, 30, 40, 50], 5, True),
    ([10, None, None], 3, True),
    # Hidden Testcases
    ([42], "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b", False),
    (
        [None, None, None],
        "4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce",
        False,
    ),
]

NumberOfElements_testcases = [
    # Visible Testcases
    ([10, 20, 30, 40, 50], 5, True),
    ([10, None, None], 1, True),
    # Hidden Testcases
    ([42], "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b", False),
    (
        [None, None, None],
        "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9",
        False,
    ),
]

IsFull_testcases = [
    # Visible Testcases
    ([10, 20, 30, 40, 50], True, True),
    ([10, None, None], False, True),
    # Hidden Testcases
    ([42], "3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18", False),
    (
        [None, None, None],
        "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe",
        False,
    ),
]

IsEmpty_testcases = [
    # Visible Testcases
    ([10, 20, 30, 40, 50], False, True),
    ([None, None, None], True, True),
    # Hidden Testcases
    ([42], "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe", False),
    (
        [10, None, None],
        "60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe",
        False,
    ),
]


def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()


@pytest.mark.parametrize("n,result,testcase", Initialize_testcases)
def test_Initialize(n, result, testcase):
    if testcase:
        assert Initialize(n) == result
    else:
        assert hashcode(Initialize(n)) == result


@pytest.mark.parametrize("list,index,result,testcase", Get_testcases)
def test_Get(list, index, result, testcase):
    if testcase:
        assert Get(list, index) == result
    else:
        assert hashcode(Get(list, index)) == result


@pytest.mark.parametrize("list,index,value,result,testcase", Set_testcases)
def test_Set(list, index, value, result, testcase):
    if testcase:
        assert (Set(list, index, value)) is None and list == result
    else:
        assert (Set(list, index, value)) is None and hashcode(list) == result


@pytest.mark.parametrize("list,result,testcase", Size_testcases)
def test_Size(list, result, testcase):
    if testcase:
        assert Size(list) == result
    else:
        assert hashcode(Size(list)) == result


@pytest.mark.parametrize("list,result,testcase", NumberOfElements_testcases)
def test_NumberOfElements(list, result, testcase):
    if testcase:
        assert NumberOfElements(list) == result
    else:
        assert hashcode(NumberOfElements(list)) == result


@pytest.mark.parametrize("list,result,testcase", IsFull_testcases)
def test_IsFull(list, result, testcase):
    if testcase:
        assert IsFull(list) == result
    else:
        assert hashcode(IsFull(list)) == result


@pytest.mark.parametrize("list,result,testcase", IsEmpty_testcases)
def test_IsEmpty(list, result, testcase):
    if testcase:
        assert IsEmpty(list) == result
    else:
        assert hashcode(IsEmpty(list)) == result
