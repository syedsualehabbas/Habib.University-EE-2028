import pytest
import hashlib
from q2 import matrix_subtraction

q2_testcases = [
    # Visible Testcases
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]], [[-8, -6, -4], [-2, 0, 2], [4, 6, 8]], True), 
    ([[12, 7, 3], [4, 5, 6], [7, 8, 9]], [[5, 8, 1], [6, 7, 3], [4, 5, 9]], [[7, -1, 2], [-2, -2, 3], [3, 3, 0]], True), 
    ([[1], [2]], [[3, 5], [4, 6]], "Matrices A and B don't have the same dimension required for matrix subtraction.", True),

    # Hidden Testcases 
    ([[1], [1], [1]], [[2], [2], [4]], 'b2b5c1e8e915612b1a7b2ca51381a2a689ebae5222f8dd376da8f2d8ad0dc9ac', False), 
    ([[0, 1, 2], [9, 8, 7]], [[6, 5, 4], [3, 4, 5]], 'bbc6b0272f2539e1e63d05ba1e63b28418562b82baa28e82376133ca6817f7e9', False), 
    ([[1, 1, 1]], [[2, 2, 4]], '85d0cd0d16d2e13bdf6a12b6b452ff4b36cd16b3a5234355d0d6754a9009ccf1', False), 
    ([[1, 2], [0, 3], [6, 7]], [[4, 5], [7, 8]], 'c7b9fbc23c0c3916d13c4888b9b1630446059cfd7e079780be8ed788e1a4253b', False)
    ]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst1,lst2,result,testcase",q2_testcases)
def test_q2(lst1,lst2,result,testcase):
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
    if any(callable(value) and any(pattern.search(inspect.getsource(matrix_subtraction))
                                   for pattern in verboten)
           for value in globals_copy.values()):
        raise Exception('eval function, getattr function, or list methods may not be used.')
    else:
        if testcase == True:
            matrix_subtraction(lst1,lst2) == result
        else:
            assert hashcode(matrix_subtraction(lst1,lst2)) == result