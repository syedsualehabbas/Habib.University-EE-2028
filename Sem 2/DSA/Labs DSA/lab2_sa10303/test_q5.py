import pytest
import hashlib
from q5 import reduce_image

q5_testcases = [
    # Visible Testcases
    ([[10, 20, 20], [10, 10, 10], [20, 10, 20]], [[7.368, 10.627, 9.283], [8.879, 10.627, 9.283], [8.434, 8.879, 8.434]], True), 
    ([[10, 10, 10, 10, 10], [20, 20, 20, 20, 20], [80, 80, 80, 80, 80], [60, 60, 60, 60, 60], [70, 70, 70, 70, 70]], [[7.937, 9.283, 9.283, 9.283, 7.937], [15.874, 18.371, 18.371, 18.371, 15.874], [26.777, 31.748, 31.748, 31.748, 26.777], [27.85, 32.46, 32.46, 32.46, 27.85], [23.693, 28.189, 28.189, 28.189, 23.693]], True), 
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[2.224, 3.362, 3.391], [4.514, 5.848, 5.451], [4.919, 6.283, 5.55]], True),

    # Hidden Testcases
    ([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], '7af1e9003c25d598c87f6192c311892c6916a751e8a683ed928950cf32815592', False), 
    ([[1, 2], [1, 2]], 'b5c9692f78a3d180d4d0ca952259cc0bd40dfff2db4b14fd0fc4ebf10c431a46', False), 
    ([[1, 5, 61, 35], [4, 3, 2, 74], [10, 11, 100, 42], [48, 7, 65, 27], [81, 200, 9, 99]], '5b403b95455d3bec607f6efd73379f363569c4bdbfa4531f8de61889927725b1', False), 
    ([[1, 4, 10, 48, 81], [5, 3, 11, 7, 200], [61, 2, 100, 65, 9], [35, 74, 42, 27, 99]], '3ae09b6cba6f040be210a2809d2d8bcbf3e07a57120be4e858215d41b078cccb', False)
    ]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst1,result,testcase",q5_testcases)
def test_q5(lst1,result,testcase):
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
    if any(callable(value) and any(pattern.search(inspect.getsource(reduce_image))
                                   for pattern in verboten)
           for value in globals_copy.values()):
        raise Exception('eval function, getattr function, or list methods may not be used.')
    else:
        if testcase == True:
            assert reduce_image(lst1) == result
        else:
            assert hashcode(reduce_image(lst1)) == result