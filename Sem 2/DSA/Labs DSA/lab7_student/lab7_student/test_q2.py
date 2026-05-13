import pytest
import hashlib
from q2 import *

q2_testcases = [
    # Visible Testcases
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 8, 3, [0, 1, 2, 8, 13, 17, 19, 32, 42], True), 
    ([0, 1, 2, 3, 8, 13, 17, 19, 32, 42], -1, 0, [-1, 0, 1, 2, 3, 8, 13, 17, 19, 32, 42], True), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 13, 4, [0, 1, 2, 8, 13, 17, 19, 32, 42], True), 
    ([0, 1, 2, 5, 8, 13, 15, 17, 19, 20, 32, 42], 14, 6, [0, 1, 2, 5, 8, 13, 14, 15, 17, 19, 20, 32, 42], True), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 0, 0, [0, 1, 2, 8, 13, 17, 19, 32, 42], True), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 2, 2, [0, 1, 2, 8, 13, 17, 19, 32, 42], True), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 1, 1, [0, 1, 2, 8, 13, 17, 19, 32, 42], True), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 17, 5, [0, 1, 2, 8, 13, 17, 19, 32, 42], True), 

    # Hidden Testcases
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 19, 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683', '3c52dfac512e535d81790d59897a67b4c88c4c4a876e537c22147f25d98ca00d', False), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 32, '7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451', '3c52dfac512e535d81790d59897a67b4c88c4c4a876e537c22147f25d98ca00d', False), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 42, '2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3', '3c52dfac512e535d81790d59897a67b4c88c4c4a876e537c22147f25d98ca00d', False), 
    ([0, 1, 2, 3, 8, 13, 17, 19, 32, 42], 0, '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', '84479da4b2f45deaed8601c23abb775511c24631d871148f981c743594835a35', False), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 3, '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce', '84479da4b2f45deaed8601c23abb775511c24631d871148f981c743594835a35', False), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 43, '19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7', '6a75b2a1e083e9fbf699c9ecfbaaa9c167aa3df8f2d5a8c9b415ef02eea00a98', False), 
    ([0, 1, 2, 5, 8, 13, 15, 17, 19, 20, 32, 42], 15, 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683', '64d8e57db24c7eb1f35d832ae47958810533d7c3b2f9abe78e29094c01f2c718', False), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], -1, '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', 'd7d9cba27c20beedde5bf1535872e060f5ef2ce78e0c5c15e2805ed4bc2fed35', False), 
    ([0, 1, 2, 8, 13, 17, 19, 32, 42], 46, '19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7', '7714ab1d6dab52df13f6450a9fbcda96c279c8498cf69be4d1d1021585e6db22', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst,item,result,resultlst,testcase",q2_testcases)
def test_q2(lst,item,result,resultlst,testcase):
    if testcase == True:
        assert (binary_search_iterative_modified(lst,item)) == result and lst ==resultlst
    else:
        assert hashcode(binary_search_iterative_modified(lst,item)) == result and hashcode(lst) == resultlst