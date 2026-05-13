import pytest
import hashlib
from q2 import *

q2_testcases_hashing = [
    # Visible Testcases
    (5, 10, 5, True),
    ("Hello", 11, 5, True),

    # Hidden Testcases
    ("Hello", 10, '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False),
    ("Testing key", 20, 'e629fa6598d732768f7c726b4b621285f9c3b85303900aa912017db7617d8bdb', False),
    (43, 1000, '44cb730c420480a0477b505ae68af508fb90f96cf0ec54c6ad16949dd427f13a', False)
]

q2_testcases_collisionResolver = [
    # Visible Testcases
    (5, 10, 3, 8, True),
    ("Hello", 11, 2, 7, True),

    # Hidden Testcases
    ("Hello", 10, 6, 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683', False),
    ("Testing key", 20, 12, '7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451', False),
    (43, 1000, 125, '80c3cd40fa35f9088b8741bd8be6153de05f661cfeeb4625ffbf5f4a6c3c02c4', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("key,size,result,testcase", q2_testcases_hashing)
def test_q2(key,size,result,testcase):
    if testcase == True:
        assert hash_function(key, size) == result
    else:
        assert hashcode(hash_function(key, size)) == result

@pytest.mark.parametrize("key,size,iteration,result,testcase", q2_testcases_collisionResolver)
def test_q2_1(key,size,iteration,result,testcase):
    if testcase == True:
        assert collision_resolver(key, size, iteration) == result
    else:
        assert hashcode(collision_resolver(key, size, iteration)) == result