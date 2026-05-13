import pytest
import hashlib
from sys import stderr
from q4 import *

q4_testcases = [
    # Visible Testcases
    ([[5, 8, 1], [6, 7, 3], [5, 4, 9]], 0, [[5 , 8 , 1] , [5 , 4 , 9] , [6 , 7 , 3]], True),
    ([['square', 'rectangle', 'triangle'], ['chair','table', 'house'], ['motor cycle', 'car', 'truck']], 2, [['chair', 'table', 'house'], ['square', 'rectangle', 'triangle'], ['motor cycle', 'car', 'truck']], True),

    # Hidden Testcases
    ([[75, 28, 12], [63, 37, 23], [84, 15, 49]], 1, 'b6ac76a4ac5388d81110af83b5c027e3a2d4ef36761a1c40031a7caab5d53048', False),
    ([[65, 73, 42, 72, 80, 93, 4, 78, 34, 35], [13, 20, 34, 57, 20, 96, 1, 76, 15, 91], [27, 5, 40, 74, 37, 96, 65, 21, 79, 64], [0, 74, 13, 51, 81, 78, 64, 47, 81, 42], [34, 56, 33, 54, 94, 77, 51, 11, 56, 30], [12, 91, 93, 73, 98, 29, 18, 84, 99, 74], [43, 16, 62, 78, 70, 50, 51, 86, 10, 39], [54, 44, 74, 2, 39, 6, 47, 80, 95, 7], [83, 52, 49, 73, 24, 88, 81, 11, 99, 59], [100, 60, 97, 90, 23, 71, 52, 79, 13, 71]], 0, '84c8b1290b6452d834575fadb147a512347d934115ad19e7bf2ce1d071e3c16a', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("matrix,col,result,testcase",q4_testcases)
def test_q4(matrix,col,result,testcase):
    if testcase == True:
        assert sort_matrix_by_columnNumber(matrix, col) == result and matrix == result
    else:
        assert hashcode(sort_matrix_by_columnNumber(matrix, col)) == result and hashcode(matrix) == result