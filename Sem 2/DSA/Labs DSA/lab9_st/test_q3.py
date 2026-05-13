import pytest
import hashlib
from q3 import *

q3_testcases = [
    # Visible Testcases
    ([("hello", 10), ("world", 19)], ["hello", "world", "olleh", "ALPHA"], 10, [10, 19, None, None], ([None, None, 'hello', 'world', None, None, None, None, None, None], [None, None, 10, 19, None, None, None, None, None, None]), True),
    ([(0, 1), (1, 2), (42, 5)], [0, 1, 42, 10, 11], 10, [1, 2, 5, None, None], ([0, 1, 42, None, None, None, None, None, None, None], [1, 2, 5, None, None, None, None, None, None, None]), True), 
    ([(2, 14), (3, 12)], [2, 3, 27, 28], 25, [14, 12, None, None], ([None, None, 2, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, 14, 12, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]), True),
    ([('cat', 'c'), ('bat', 'b'), ('rat', 'r'), ('fat', 'f'), ('hat', 'h'), ('mat', 'm')], ['cat', 'bat', 'rat', 'fat', 'hat', 'mat', 'pat'], 5, ['c', 'b', 'r', 'f', 'h', None, None], (['fat', 'bat', 'cat', 'rat', 'hat'], ['f', 'b', 'c', 'r', 'h']), True),

    # Hidden Testcases
    ([("temp", "data"), (98, 1), (532, 324)],["temp", 98, 532, 15, "data"], 1000, '30389b75dd0e9ae8600b6af42358be0bce634d7898ce24f5138ef5ff2936f59e', '5b908d3f47b2ce90a553ee29e579e2e55ea6fd8828d9da7307c874c2934dbc6c', False), 
    ([('hello', 1), (4, 23)], ["hello", 4, 10, 20], 15, "6b6aafafc98de62769ef75588f2fdf1cd13bc1b9adb055e0f73b790e64979af1",'4ceb68135e903b1ec022c4cfafc4a36b5b25829b723c037149f8f12410a9706d', False),
    ([(19, 21), (43, "num"), (7, 21), ("my", "name"), ("string", "check")], [19, 43, 7, "my", "string", 4, 50], 15, "59a3f68ab8cb7fabeddf76ad813640cfcfb4c6e1818bcc085d4e312914ccde3c", 'bc0ee0f411502183f1087345da2ff6d1e48b909cd49c394d01e6e03bd1eb50a4', False),
    ([(19, 21), (43, "num"), (7, 21), ("my", "name"), ("string", "check"), (34, "collision"), ("put!", 8)], [43, 19, 7, "put!", "my", 34, "string", "check", "collision"], 15, "be3af5ac4b48b7e872f38cedbc122b0341e32fb627d2cc110d1e23e8d2b952b3", 'c3981af1bdaa73549242033b94c875b050161dc36efa4551eab71ebe95a5ddee', False),
    ([("temp", "data"), (98, 1), (532, 324)],["temp", 98, 532, 324, 196], 10, "30389b75dd0e9ae8600b6af42358be0bce634d7898ce24f5138ef5ff2936f59e", '685844642c596ac184ea1633c1a45fb96c39cd867b4d3f7a5b201516785ca8c7', False),
    ([(143, "some string"), ("key", "value"), (4, 2), (0, 65)],[0, "key", 4, 143, 1004, 1065], 1000,'f44c87f2f52f1e71b269d6a9956605ae546fa1d7e81950e84b5f2a80f596ee42', 'dfd6b2b9bcc5aa808b7b2abd92a38b7d1643b0c52f9fe7d7c2efa9b51567643f', False),
    ([('applepie', 'apie'), ('applepot', 'apot'), ('applesauce', 'asauce'), ('banana', 'b'), ('bananasplit', 'bsplit'), ('mango', 'm'), ('orange', 'o'), ('strawberry', 's')], ['applepie', 'applepot', 'applesauce', 'banana', 'bananasplit', 'mango', 'orange', 'strawberry'], 7, 'c059485762c3da603d59940f77a72d65697b10a81dd602a89f06384a6fff2cd7', '9f76b7b5f2814b1b9cb5947e43a097307f89927ef0a28b6f6b7c78f8eb751bfd', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("to_put,to_get,size,result,h_r,testcase",q3_testcases)
def test_q3(to_put,to_get,size,result,h_r,testcase):
    H = create_hashtable(size)
    for i in to_put:
        put(H,i[0],i[1],size)
    lst = []
    for i in to_get:
        lst.append(get(H,i,size))
    if testcase==True:
        assert lst == result and H == h_r
    else:
        assert hashcode(lst) == result and hashcode(H) == h_r