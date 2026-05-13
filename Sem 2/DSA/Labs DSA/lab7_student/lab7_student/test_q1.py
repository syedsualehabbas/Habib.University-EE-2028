import pytest
import hashlib
from q1 import *

q1_testcases = [
    # Visible Testcases
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 8, 3, True), 
    ([0, 1, 2, 3, 8, 13, 17, 19, 32, 42], -1, -1, True), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 13, 4, True), 
    ([0, 1, 2, 5, 8, 13, 15, 17, 19, 20, 32, 42], 14, -1, True), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 0, 0, True), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 2, 2, True), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 1, 1, True), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 17, 5, True),

    # Hidden Testcases 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 19, 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683', False), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 32, '7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451', False), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 42, '2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3', False), 
    ([0, 1, 2, 3, 8, 13, 17, 19, 32, 42], 0, '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 3, '1bad6b8cf97131fceab8543e81f7757195fbb1d36b376ee994ad1cf17699c464', False), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 43, '1bad6b8cf97131fceab8543e81f7757195fbb1d36b376ee994ad1cf17699c464', False), 
    ([0, 1, 2, 5, 8, 13, 15, 17, 19, 20, 32, 42], 15, 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683', False), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], -1, '1bad6b8cf97131fceab8543e81f7757195fbb1d36b376ee994ad1cf17699c464', False), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 46, '1bad6b8cf97131fceab8543e81f7757195fbb1d36b376ee994ad1cf17699c464', False)
    ]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst,item,result,testcase",q1_testcases)
def test_q1(lst,item,result,testcase):
    if testcase == True:
        assert binary_search_iterative(lst,item) == result
    else:
        assert hashcode(binary_search_iterative(lst,item)) == result