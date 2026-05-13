import hashlib

import pytest
from q4 import InsertAtStart


insert_at_start_testcases = [
    # Visible Testcases
    ([None, None], "a", "Element inserted successfully", ["a", None], True),
    (["a", None], "b", "Element inserted successfully", ["b", "a"], True),
    (["b", "a"], "c", "List is full", ["b", "a"], True),
    # Hidden Testcases
    (
        ["b"],
        "c",
        "71a7bcb2f28205b5712a8cc116ff4ebed793760be4d3209802de4eff77c83dc5",
        "d4a37d37ced8324ba67f3773dfbc749ff4db6deb8e95e2e9580e2e11e4e243be",
        False,
    ),
    (
        ["a", "b", None],
        "c",
        "134ee9beb24a226cc709c7365151d56a29d6c5e892d90a2122a7dd71861f58e5",
        "e98d25fa1ba65a6e1efcfdab966486e42daff252bc6d7564bddf2942b4a56ace",
        False,
    ),
    (
        [None, None, None],
        "a",
        "134ee9beb24a226cc709c7365151d56a29d6c5e892d90a2122a7dd71861f58e5",
        "9bf4b5c1d663646e15eac5a644ee42b0b90740ebbf4afd76cfe061e66fe6c9a9",
        False,
    ),
    (
        ["a", "c", None, None],
        "b",
        "134ee9beb24a226cc709c7365151d56a29d6c5e892d90a2122a7dd71861f58e5",
        "3ac714c130c93025dd2e80be5544952c351e30b51c88e5bf3d3d2c6e7892f783",
        False,
    ),
]


def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()


@pytest.mark.parametrize(
    "list,element,output,final,testcase", insert_at_start_testcases
)
def test_InsertAtStart(list, element, output, final, testcase):
    if testcase:
        assert InsertAtStart(list, element) == output and list == final
    else:
        assert (
            hashcode(InsertAtStart(list, element)) == output and hashcode(list) == final
        )
