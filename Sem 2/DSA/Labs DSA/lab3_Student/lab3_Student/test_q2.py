import hashlib

import pytest
from q2 import Insert


insert_testcases = [
    # Visible Testcases
    (
        [None, None, None],
        0,
        "a",
        "Element inserted successfully",
        ["a", None, None],
        True,
    ),
    (["a", None, None], 2, "b", "Invalid Index", ["a", None, None], True),
    (
        ["a", None, None],
        1,
        "b",
        "Element inserted successfully",
        ["a", "b", None],
        True,
    ),
    (["a", "b", None], 4, "e", "Invalid Index", ["a", "b", None], True),
    (["a", "b", None], 2, "c", "Element inserted successfully", ["a", "b", "c"], True),
    (["a", "b", "c"], 3, "d", "List is full", ["a", "b", "c"], True),
    (["a", "b", None], 1, "c", "Element inserted successfully", ["a", "c", "b"], True),
    (["a", "b", None], 0, "c", "Element inserted successfully", ["c", "a", "b"], True),
    (
        ["a", "c", None, None],
        0,
        "b",
        "Element inserted successfully",
        ["b", "a", "c", None],
        True,
    ),
    (["a", None], 0, "b", "Element inserted successfully", ["b", "a"], True),
    # Hidden Testcases
    (
        ["a", "b", None],
        -1,
        "e",
        "a88ada13a2d454eaa7f2363f7c06c19d8328d10306baffb71139c2081bf35128",
        "26da2835afd041f34ebfc5a8e7a0582421933402fe77cd3fba8a23aedbbb6833",
        False,
    ),
    (
        ["a"],
        0,
        "b",
        "71a7bcb2f28205b5712a8cc116ff4ebed793760be4d3209802de4eff77c83dc5",
        "a326618a43c0b61aff497f4d8a82f4857fe952c5fae156ab94facf4adbf7dcb4",
        False,
    ),
    (
        ["a", None, None],
        2,
        "e",
        "a88ada13a2d454eaa7f2363f7c06c19d8328d10306baffb71139c2081bf35128",
        "9bf4b5c1d663646e15eac5a644ee42b0b90740ebbf4afd76cfe061e66fe6c9a9",
        False,
    ),
    (
        ["a", None, None, None],
        3,
        "e",
        "a88ada13a2d454eaa7f2363f7c06c19d8328d10306baffb71139c2081bf35128",
        "3b9fdb455eb6b4d933856a76287a3559fad3fd7fac58afae2c11c716ad864382",
        False,
    ),
    (
        ["a", None, None, None],
        2,
        "e",
        "a88ada13a2d454eaa7f2363f7c06c19d8328d10306baffb71139c2081bf35128",
        "3b9fdb455eb6b4d933856a76287a3559fad3fd7fac58afae2c11c716ad864382",
        False,
    ),
]


def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()


@pytest.mark.parametrize("list,index,element,output,result,testcase", insert_testcases)
def test_Insert(list, index, element, output, result, testcase):
    if testcase:
        assert Insert(list, index, element) == output and list == result
    else:
        assert (
            hashcode(Insert(list, index, element)) == output
            and hashcode(list) == result
        )
