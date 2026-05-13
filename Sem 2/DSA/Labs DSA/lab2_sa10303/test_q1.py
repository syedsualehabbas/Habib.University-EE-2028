import pytest
import hashlib
from q1 import initialize_matrix

q1_testcases = [
    # Visible Testcases
    (3, 3, [[0, 0, 0], [0, 0, 0], [0, 0, 0]], True), 
    (2, 5, [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], True), 
    (7, 3, [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], True),

    # Hidden Testcases
    (5, 5, 'd4c2d04bd630e24c65ebb4c74eb57b69176d51b11c2c16b485f19b83a366bafa', False), 
    (6, 2, 'ec18cb84869b03d7be17d95bc38664179b49b25aba084d16086c9789c82097cc', False), 
    (4, 5, '627bc44b1deaf6cbc1ce3bc5e7d1d60fab692a2732bc7d3b36f46583c797dabc', False)
    ]


def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("rows,cols,result,testcase",q1_testcases)
def test_q1(rows,cols,result,testcase):
    import inspect
    import re
    list_methods = ['append', 'extend', 'insert', 'remove', 'pop', 'clear',
                    'index', 'count', 'sort', 'reverse', 'copy']
    verboten_methods = ['\\.[ \\t]*' + method + '[ \\t]*\\('
                        for method in list_methods]
    verboten = ['eval', 'getattr']
    verboten.extend(verboten_methods)
    verboten = [re.compile(pattern) for pattern in verboten]
    globals_copy = globals().copy()
    if any(callable(value) and any(pattern.search(inspect.getsource(initialize_matrix))
                                   for pattern in verboten)
           for value in globals_copy.values()):
        raise Exception('eval function, getattr function, or list methods may not be used.')
    else:
        if testcase == True:
            assert initialize_matrix(rows,cols) == result
        else:
            assert hashcode(initialize_matrix(rows, cols)) == result