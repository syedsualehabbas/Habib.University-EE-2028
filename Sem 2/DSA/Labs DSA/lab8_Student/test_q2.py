import pytest
import hashlib
from sys import stderr
from q2 import *

q2_testcases = [
    # Visible Testcases
    ([['square', 'rectangle', 'triangle'], ['chair','table', 'house'], ['motor cycle', 'car', 'truck']], 0, 2, 1, "[['motor cycle', 'car', 'truck'], ['chair', 'table', 'house'], ['square', 'rectangle', 'triangle']]\n[['motor cycle', 'car', 'truck'], ['square', 'rectangle', 'triangle'], ['chair', 'table', 'house']]", [['motor cycle', 'car', 'truck'], ['square', 'rectangle', 'triangle'], ['chair', 'table', 'house']], True),
    ([[75, 28, 12], [63, 37, 23], [84, 15, 49]], 0, 2, 1, "[[84, 15, 49], [63, 37, 23], [75, 28, 12]]\n[[84, 15, 49], [75, 28, 12], [63, 37, 23]]", [[84, 15, 49], [75, 28, 12], [63, 37, 23]], True),
    ([[7, 8, 9], [1, 2, 3], [4, 5, 6]], 0, 2, 2, "[[1, 2, 3], [4, 5, 6], [7, 8, 9]]", [[1, 2, 3] , [4, 5, 6] , [7, 8, 9]], True),
    # Hidden Testcases
    ([['square', 'rectangle', 'triangle'], ['chair','table', 'house'], ['motor cycle', 'car', 'truck']], 0, 2, 2, 'de9d9998a7c597008e71db0dfe3dad66d80e0bd36c7d4265f3711d7325a0b1cf', 'b6a6f9140d75a1dda49f0244332b32d72b7f1d411f1a4e8ab105ac6b2fcc67c4', False),
    ([[5, 8, 1], [6, 7, 3], [5, 4, 9]], 0, 2, 0, '8d2d5f3953fb0bb08386d3bdbf9934d5bc62994bc1404c8b6048680e5758c467', '8d2d5f3953fb0bb08386d3bdbf9934d5bc62994bc1404c8b6048680e5758c467', False),
    ([[65, 73, 42, 72, 80, 93, 4, 78, 34, 35], [13, 20, 34, 57, 20, 96, 1, 76, 15, 91], [27, 5, 40, 74, 37, 96, 65, 21, 79, 64], [0, 74, 13, 51, 81, 78, 64, 47, 81, 42], [34, 56, 33, 54, 94, 77, 51, 11, 56, 30], [12, 91, 93, 73, 98, 29, 18, 84, 99, 74], [43, 16, 62, 78, 70, 50, 51, 86, 10, 39], [54, 44, 74, 2, 39, 6, 47, 80, 95, 7], [83, 52, 49, 73, 24, 88, 81, 11, 99, 59], [100, 60, 97, 90, 23, 71, 52, 79, 13, 71]], 0, 9, 0, 'e27c5f4e1b4f2e23e01928e0f3077814e046208a4fb09227bd124b1b5782f318', '84c8b1290b6452d834575fadb147a512347d934115ad19e7bf2ce1d071e3c16a', False)
    ]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("matrix,low,high,column,result,lstresult,testcase",q2_testcases)
def test_q2(capsys, matrix, low, high, column, result, lstresult, testcase):
    quick_sort_by_column_number(matrix, low, high, column)
    captured, _ = capsys.readouterr()
    if testcase == True:
        assert captured[:-1] == result and matrix == lstresult
    else:
        assert hashcode(captured[:-1]) == result and hashcode(matrix) == lstresult