import pytest
import hashlib
from q4 import matrix_multiplication

q4_testcases = [
    # Visible Testcases
    ([[12, 7, 3], [4, 5, 6], [7, 8, 9]], [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]], [[114, 160, 60, 27], [74, 97, 73, 14], [119, 157, 112, 23]], True), 
    ([[34, 1, 77], [2, 14, 8], [3, 17, 11]], [[6, 8, 1], [9, 27, 5], [2, 43, 31]], [[367, 3610, 2426], [154, 738, 320], [193, 956, 429]], True), 
    ([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]], [[58, 64], [139, 154]], True), 
    ([[7, 3], [2, 5], [6, 8], [9, 0]], [[8, 14, 0, 3, -1], [7, 11, 5, 91, 3], [8, -4, 19, 5, 57]], 'The number of columns in Matrix A does not equal the number of rows in Matrix B required for Matrix Multiplication.', True), 
    ([[3, 4, 2]], [[13, 9, 7, 15], [8, 7, 4, 6], [6, 4, 0, 3]], [[83, 63, 37, 75]], True), 

    # Hidden Testcases
    ([[-1, 3, 4, -3], [2, -2, 6, 0]], [[5, 7, -1], [8, 9, -4], [4, -2, 6], [2, 3, 1]], 'eac14bcfffed9d76473a948ef5804db3ecfc1751d2ec72e5af65b6b090008ca8', False), 
    ([[1, 2, -1], [2, 0, 1]], [[3, 1], [0, -1], [-2, 3]], 'fdda4d5cfc00db23e3792c06d0f52edffef9a9721ffd11b7f3146796a2bea523', False), 
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], [[-2], [1], [0]], '812dd3f4e07326125efa54ae462c88c0f41d59969703ebdda6dcffae22f936c9', False), 
    ([[1, 4, 6, 10], [2, 7, 5, 3]], [[1, 4, 6, 10], [2, 7, 5, 3], [9, 0, 11, 8]], '519b7d5fc632a6bb595c7ec91f3d1f4adfa285e0baae1f051e30b04e248c7b7a', False), 
    ([[1, 4, 6, 10], [2, 7, 5, 3], [9, 0, 11, 8]], [[1, 4, 6, 10], [2, 7, 5, 3]], '519b7d5fc632a6bb595c7ec91f3d1f4adfa285e0baae1f051e30b04e248c7b7a', False)
    ]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst1,lst2,result,testcase",q4_testcases)
def test_q4(lst1,lst2,result,testcase):
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
    if any(callable(value) and any(pattern.search(inspect.getsource(matrix_multiplication))
                                   for pattern in verboten)
           for value in globals_copy.values()):
        raise Exception('eval function, getattr function, or list methods may not be used.')
    else:
        if testcase==True:
            assert matrix_multiplication(lst1,lst2) == result
        else:
            assert hashcode(matrix_multiplication(lst1,lst2)) == result