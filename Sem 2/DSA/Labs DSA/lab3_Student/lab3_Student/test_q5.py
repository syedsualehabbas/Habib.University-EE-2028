import hashlib

import pytest
from q5 import RemoveFromStart


remove_from_start_testcases = [
    # Visible Testcases
    ([None, None], "List is empty", [None, None], True),
    (["a", "b"], "Element removed successfully", ["b", None], True),
    (
        [10, 20, 40, 50, None],
        "Element removed successfully",
        [20, 40, 50, None, None],
        True,
    ),
    # Hidden Testcases
    (
        [None],
        "ba61eea246993d3ff552ff2645a632e9b743d05d0dd96a5cf93f3b472ab69c8a",
        "778d5d27b716881dd9d3b58baaed62878f93076984cf0cbb45d393bedf363cb2",
        False,
    ),
    (
        ["a"],
        "d8116103aeebda02e83f02448224e17cb44a78f61747ec2357fdd963ea986d10",
        "778d5d27b716881dd9d3b58baaed62878f93076984cf0cbb45d393bedf363cb2",
        False,
    ),
    (
        [None, None, None, None],
        "ba61eea246993d3ff552ff2645a632e9b743d05d0dd96a5cf93f3b472ab69c8a",
        "2023f50b8ba151cd10fdb2a83bd4cf75f645443e9303a516b1a78c90f269a310",
        False,
    ),
]


def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode("utf-8")).hexdigest()


@pytest.mark.parametrize("list,output,final,testcase", remove_from_start_testcases)
def test_RemoveFromStart(list, output, final, testcase):
    if testcase:
        assert RemoveFromStart(list) == output and list == final
    else:
        assert hashcode(RemoveFromStart(list)) == output and hashcode(list) == final
