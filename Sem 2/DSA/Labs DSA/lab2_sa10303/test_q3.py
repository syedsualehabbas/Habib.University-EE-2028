import pytest
import hashlib
from q3 import matrix_transpose

q3_testcases = [
    # Visible Testcases
    ([[12, 7], [4, 5], [3, 8]], [[12, 4, 3], [7, 5, 8]], True), 
    ([[12, 4, 3], [7, 5, 8]], [[12, 7], [4, 5], [3, 8]], True),

    # Hidden Testcases
    ([[5, 4, 3], [4, 0, 4], [7, 10, 3]], 'b42a5b24b21f70e1906e2f299eecd64cf614586d2a5356a2bd6609e08e39b92f', False), 
    ([[5, 4], [4, 0], [7, 10], [-1, 8]], 'b4b7293a64bc6e2389d49b9ac72d844c6f090e2078fb6de49781164d5afb2e1b', False), 
    ([[1, 2, 3], [4, 5, 6]], '3821d19d25b6f8e539ad60f5beac15e6f2870d88244123ffebf5c9b56cff14ce', False)
    ]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst1,result,testcase",q3_testcases)
def test_q3(lst1,result,testcase):
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
    if any(callable(value) and any(pattern.search(inspect.getsource(matrix_transpose))
                                   for pattern in verboten)
           for value in globals_copy.values()):
        raise Exception('eval function, getattr function, or list methods may not be used.')
    else:
        if testcase == True:
            assert matrix_transpose(lst1) == result
        else:
            assert hashcode(matrix_transpose(lst1)) == result