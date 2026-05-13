import pytest
import hashlib
from sys import stderr
from q1 import *

q1_testcases = [
    # Visible Testcases
    ([54, 26, 93, 17, 77, 31, 44, 55, 20], '[17, 26, 93, 54, 77, 31, 44, 55, 20]\n[17, 20, 93, 54, 77, 31, 44, 55, 26]\n[17, 20, 26, 54, 77, 31, 44, 55, 93]\n[17, 20, 26, 31, 77, 54, 44, 55, 93]\n[17, 20, 26, 31, 44, 54, 77, 55, 93]\n[17, 20, 26, 31, 44, 54, 77, 55, 93]\n[17, 20, 26, 31, 44, 54, 55, 77, 93]\n[17, 20, 26, 31, 44, 54, 55, 77, 93]\n[17, 20, 26, 31, 44, 54, 55, 77, 93]', [17, 20, 26, 31, 44, 54, 55, 77, 93], True), 
    (['Aisha', 'Nadia', 'Waqar', 'Saleha', 'Hasan', 'Shahid', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj'], "['Abdullah', 'Nadia', 'Waqar', 'Saleha', 'Hasan', 'Shahid', 'Shah Jamal', 'Aisha', 'Umair', 'Taj']\n['Abdullah', 'Aisha', 'Waqar', 'Saleha', 'Hasan', 'Shahid', 'Shah Jamal', 'Nadia', 'Umair', 'Taj']\n['Abdullah', 'Aisha', 'Hasan', 'Saleha', 'Waqar', 'Shahid', 'Shah Jamal', 'Nadia', 'Umair', 'Taj']\n['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Waqar', 'Shahid', 'Shah Jamal', 'Saleha', 'Umair', 'Taj']\n['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shahid', 'Shah Jamal', 'Waqar', 'Umair', 'Taj']\n['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Waqar', 'Umair', 'Taj']\n['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Waqar', 'Umair', 'Taj']\n['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']\n['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']\n['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']", ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar'], True), 
    ([4, 1, 3, 9, 7], '[1, 4, 3, 9, 7]\n[1, 3, 4, 9, 7]\n[1, 3, 4, 9, 7]\n[1, 3, 4, 7, 9]\n[1, 3, 4, 7, 9]', [1, 3, 4, 7, 9], True), 
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], '[1, 9, 8, 7, 6, 5, 4, 3, 2, 10]\n[1, 2, 8, 7, 6, 5, 4, 3, 9, 10]\n[1, 2, 3, 7, 6, 5, 4, 8, 9, 10]\n[1, 2, 3, 4, 6, 5, 7, 8, 9, 10]\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True), 
    ([12, 8, -6, 2, 4, 5, 3, 7, 4, 2], '[-6, 8, 12, 2, 4, 5, 3, 7, 4, 2]\n[-6, 2, 12, 8, 4, 5, 3, 7, 4, 2]\n[-6, 2, 2, 8, 4, 5, 3, 7, 4, 12]\n[-6, 2, 2, 3, 4, 5, 8, 7, 4, 12]\n[-6, 2, 2, 3, 4, 5, 8, 7, 4, 12]\n[-6, 2, 2, 3, 4, 4, 8, 7, 5, 12]\n[-6, 2, 2, 3, 4, 4, 5, 7, 8, 12]\n[-6, 2, 2, 3, 4, 4, 5, 7, 8, 12]\n[-6, 2, 2, 3, 4, 4, 5, 7, 8, 12]\n[-6, 2, 2, 3, 4, 4, 5, 7, 8, 12]', [-6, 2, 2, 3, 4, 4, 5, 7, 8, 12], True), 
    (['FunForFun', 'Practice.FunForFun', 'FunforFun'], "['FunForFun', 'Practice.FunForFun', 'FunforFun']\n['FunForFun', 'FunforFun', 'Practice.FunForFun']\n['FunForFun', 'FunforFun', 'Practice.FunForFun']", ['FunForFun', 'FunforFun', 'Practice.FunForFun'], True), 
    ([37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54], '[0, 23, 37, 17, 12, 72, 31, 46, 100, 88, 54]\n[0, 12, 37, 17, 23, 72, 31, 46, 100, 88, 54]\n[0, 12, 17, 37, 23, 72, 31, 46, 100, 88, 54]\n[0, 12, 17, 23, 37, 72, 31, 46, 100, 88, 54]\n[0, 12, 17, 23, 31, 72, 37, 46, 100, 88, 54]\n[0, 12, 17, 23, 31, 37, 72, 46, 100, 88, 54]\n[0, 12, 17, 23, 31, 37, 46, 72, 100, 88, 54]\n[0, 12, 17, 23, 31, 37, 46, 54, 100, 88, 72]\n[0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]\n[0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]\n[0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]', [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100], True), 
    
    # Hidden Testcases
    ([5, 2, 7, 10, 3, 5, 2, 1, 8, 9], '942c7ca6692bd6bf2030173e9c5655afe00d1a7c257aadf5ff2c1c2c45dc5b44', 'b4789af97f8cc5a46eb7c90b3ab321488339a9d3c09731baf7a679b05220c76e', False), 
    ([7, 5, 5, 4, 3, 2, 1], '4ac92570c98238809d89a016b7f74510a96b74129cb0ad9ca98445f253a1998f', 'b518438af1011f2e4f4baf630bc00b80d7b41f384b942815d06f5c99a1ae5ca3', False), 
    ([2], '038966de9f6b9a901b20b4c6ca8b2a46009feebe031babc842d43690c0bc222b', '038966de9f6b9a901b20b4c6ca8b2a46009feebe031babc842d43690c0bc222b', False), 
    ([0, 1, -1], 'ea65e2f03097ce7085c2b598d3da0f91f364d4bde50413d3fc1a90dc6ffecf02', 'e512856be455ce3d0249415a73d5c16913698de91538787853bce94b11eaada7', False), 
    ([0, 1, 2, 3, 9, -1], 'd3758a8d05775644ddf8c3526ded7f44ff14e65fd6ad328343b56c01a0568b15', 'e4d84adb7f224ec80acbc1fd7de45109c456e80cd4d36326e3a08b8701588e53', False), 
    ([1, 2, 3, 4, 5, 6, 7, 8, 11, 10, 0], '9fcdb28ab03fb9e33105a2d2a5e950dadb577d756842b8307e385b7bf359c800', '8128d5ede96a5d11a114922983789e8de5a27d9b2a07991bfdb22181c70a0a9d', False), 
    ([71, 32, 22, 19, 18, 1, 15, 40], '976932b2408bba5a94a78d28db828aaf101f9992e681fe31547cbd62482ae2bb', '978ab89564586985c5bf115acde16a65d03a44ca61184fe20fde0c56b9863b0a', False)
    ]

def xstrip(s):
    lst = s.split('\n')
    for i in range(len(lst)):
        lst[i]=lst[i].rstrip()
    return "\n".join(lst)

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("arr,result,arrres,testcase",q1_testcases)
def test_q1(capsys,arr,result,arrres,testcase):
    selection_sort(arr)
    captured,err = capsys.readouterr()
    captured=captured[:-1]
    if testcase == True:
        assert xstrip(captured) == xstrip(result) and arr == arrres
    else:
        assert hashcode(xstrip(captured)) == result and hashcode(arr) == arrres