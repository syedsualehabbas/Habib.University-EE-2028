import pytest
import hashlib
from q5 import *

q5_testcases = [
    # Visible Testcases
    ([("temp", "data"),(98, 1),(532, 324)],[532],["temp", ], 10, (['data'], ([None, None, '#', None, None, None, None, None, 'temp', 98], [None, None, '#', None, None, None, None, None, 'data', 1])), True),
    ([("temp", "data"),(98, 1),(532, 324)],[532, 98, 532],["temp", 98], 10, (['data', None], ([None, None, '#', None, None, None, None, None, 'temp', '#'], [None, None, '#', None, None, None, None, None, 'data', '#'])), True),
    ([('hello', 10), ('world', 19)], ['hello'], ['hello'], 10, ([None], ([None, None, '#', 'world', None, None, None, None, None, None], [None, None, '#', 19, None, None, None, None, None, None])), True),

    # Hidden Testcases
    ([('hello', 10), ("world", 19)], ['world'], ['hello'], 10, "267810bcc407a8f82806107e02d3642643a31521b783c6be6d9e8c2f81778b1a", False),
    ([("hello", 1), (4, 23)], ["hello", "world"], [4], 15, "0fc2bf09ca9fcd320a0033ad28549da24c4fea611e89de7030efe327cf13e2b1", False),
    ([("hello", 1), (4, 23)], [4], ["hello"], 15, "6c7e1d26a5cedf5553a39429c01e1f353deebea2f8b5eb18f4ac1c9fea4e74d8", False),
    ([(143, "some string"),("key", "value"),(4,2), (0, 65)],[143, 143],[0, "key"], 1000,'a3b1a0202abd7bdc5f4a477d5fcfd0153b21976515ad8c041f5d6d60d443fd1b', False),
    ([(0, 1), (1, 2), (42, 5)], [0, 42], [1, 24, 0], 1000, '09ec2ddaf68bf889185e0635bc65efa87a0087347a895457816b69e529d06c9e', False),
    ([(2, 14), (3, 12)], [2], [3], 25, "6351ef1345b1f2b8463652e066dc13a8fee36ddd6aefe8da6649be734d3a4e15", False),
    ([(2, 14), (3, 12)], [3], [2], 25, "d5ce329608a003a32eb36acecf57ad755b0b99e86ce18e63fc970341ed53c962", False),
    ([(19, 21), (43, "num"), (7, 21), ("my", "name"), ("string", "check")], [19, 34], [43, 7, "my", "string"], 15, "b0b9fdad33fff55d393e552e0e8d71d2decbf1ced543d55a2ac5996b042467b7", False),
    ([(19, 21), (43, "num"), (7, 21), ("my", "name"), ("string", "check")], [19, 43, 19], [7, "my", "string"], 15, "71679c0aeadea1903fcd7909f696a742b2412708e7db9e8fe3d574860b9678ea", False),
    ([(19, 21), (43, "num"), (7, 21), ("my", "name"), ("string", "check"), (34, "collision"), ("put!", 8)], [19, "put!", 34], [43, 7, "my", "string"], 15, "241cdf407e4b9cc865c19fa56949b019caadd93aa570358863b5ebecc6b1c217", False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("to_put, to_delete, to_get, size, result, testcase", q5_testcases)
def test_q5(to_put, to_delete, to_get, size, result, testcase):
    a = main(to_put, to_delete, to_get, size)
    if testcase == True:
        assert a == result
    else:
        assert hashcode(a) == result
    
