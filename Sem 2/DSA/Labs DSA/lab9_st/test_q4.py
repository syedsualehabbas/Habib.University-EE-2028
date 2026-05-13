import pytest
import hashlib
from q4 import *

q4_testcases = [
    # Hidden Testcases - Visible Testcases in q4.py
    ([("temp", "data"), (98,1), (532,324)],["temp", 89, 98, 532, 98], [], 10,'319804b79ef8a25e8badc79886eb1e2bfee8c8ed77bae5ea9ffdb056a93a5f76'),
    ([('hello', 10), ('world', 19)], [19, 'world', 'world', 'hello'], [], 10, "75c2cf8a0a977899fbba161478e792a1a72e7c0d72d39b3d3fe99f36aa862858"),
    ([(2, 14), (3, 12)], [3, 4, 2, 2], [], 25, "02c091973edd98b7b529da2f2b3dde186df9c39afe8a2c3e35635e46a527e5f2"),
    ([(143,"some string"), ("key", "value"), (4,2), (0, 65)],[143, 2, "key", 0, 4, "key"], [], 1000,'fb8fd11e9105b9c82e748e384d1b130427442e534d59f6097a6506f552e158fb'),
    ([(0, 1), (1, 2), (42, 5)], [42, 0, 42, 1, 42], [], 1000,'15bf817af9970100cd6b434e8ab40f7ceddaaaa8c009444a2df72c943a9eef1e'),
    ([("hello", 1), (4, 23)], [4, "hello", 4, "world"], [], 15, "573f8d79989f4bac3d1b4a2d22aae20fcb370f7be5b87cd1b99e2ba0739027d3"),
    ([(19, 21), (43, "num"), (7, 21), ("my", "name"), ("string", "check")], [43, 19, "string", 43, "my", 34, 7], [], 15, "d9a6ed69cde24cd539f7384a028e97ca7b9f306b3a954d81ef6897cf03e322d1"),
    ([(19, 21), (43, "num"), (7, 21), ("my", "name"), ("string", "check"), (34, "collision"), ("put!", 8)], ["collision", 43, 19, "string", 43, "my", 34, 7, "put!"], [], 15, "c6e30027afb4f5d54964e41c2e237f036c99ab7460e171570c4148af558e511e"),
    ([('cat', 'c'), ('bat', 'b'), ('rat', 'r'), ('fat', 'f'), ('hat', 'h'), ('mat', 'm')], ['cat', 'bat', 'rat', 'fat', 'hat', 'mat', 'pat'], [], 5, "502b5d5c694683986d1c82817e7cfa6a5fd540c14f6e132bd0d9b322a345032c"),
    ([('applepie', 'apie'), ('applepot', 'apot'), ('applesauce', 'asauce'), ('banana', 'b'), ('bananasplit', 'bsplit'), ('mango', 'm'), ('orange', 'o'), ('strawberry', 's')], ['applepie', 'applepot', 'applesauce', 'banana', 'bananasplit', 'mango', 'orange', 'strawberry'], [], 7, '8497e8bc2312a19f6d21b9bdebe9265f7030bd5fccbad920676e5c00e474c3df'),
    ([(13, 'a'), (26, 'b'), (5, 'c'), (37, 'd'), (16, 'e'), (15, 'f'), (21, 'g')], [37, 16], [(26, 'h'), (15, 'i'), (48, 'j')], 11, '3e98bd3b8dda0d174a7df0724edfba69b2991c80baf452b59808ff1c5c94575e')
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("to_put,to_delete,to_put2,size,result",q4_testcases)
def test_q4(to_put,to_delete,to_put2,size,result):
    H = create_hashtable(size)
    H_lst = []
    for i in to_put:
        put(H,i[0],i[1],size)
    for i in to_delete:
        delete(H,i,size)
        H_lst.append((H[0].copy(), H[1].copy()))
    for i in to_put2:
        put(H,i[0],i[1],size)
        H_lst.append((H[0].copy(), H[1].copy()))
    assert hashcode(H_lst) == result