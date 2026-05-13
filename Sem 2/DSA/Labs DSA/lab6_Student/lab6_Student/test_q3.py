import pytest
import hashlib
from sys import stderr
from q3 import *

q3_testcases = [
    # Visible Testcases
    ([54, 26, 93, 17, 77, 31, 44, 55, 20], '[26, 54, 17, 77, 31, 44, 55, 20, 93]\n[26, 17, 54, 31, 44, 55, 20, 77, 93]\n[17, 26, 31, 44, 54, 20, 55, 77, 93]\n[17, 26, 31, 44, 20, 54, 55, 77, 93]\n[17, 26, 31, 20, 44, 54, 55, 77, 93]\n[17, 26, 20, 31, 44, 54, 55, 77, 93]\n[17, 20, 26, 31, 44, 54, 55, 77, 93]\n[17, 20, 26, 31, 44, 54, 55, 77, 93]', [17, 20, 26, 31, 44, 54, 55, 77, 93], True), 
    (['Aisha', 'Nadia', 'Waqar', 'Saleha', 'Hasan', 'Shahid', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj'], "['Aisha', 'Nadia', 'Saleha', 'Hasan', 'Shahid', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj', 'Waqar']\n['Aisha', 'Nadia', 'Hasan', 'Saleha', 'Shah Jamal', 'Abdullah', 'Shahid', 'Taj', 'Umair', 'Waqar']\n['Aisha', 'Hasan', 'Nadia', 'Saleha', 'Abdullah', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']\n['Aisha', 'Hasan', 'Nadia', 'Abdullah', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']\n['Aisha', 'Hasan', 'Abdullah', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']\n['Aisha', 'Abdullah', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']\n['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']\n['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']\n['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']", ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar'], True), 
    ([4, 1, 3, 9, 7], '[1, 3, 4, 7, 9]\n[1, 3, 4, 7, 9]\n[1, 3, 4, 7, 9]\n[1, 3, 4, 7, 9]', [1, 3, 4, 7, 9], True), 
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], '[9, 8, 7, 6, 5, 4, 3, 2, 1, 10]\n[8, 7, 6, 5, 4, 3, 2, 1, 9, 10]\n[7, 6, 5, 4, 3, 2, 1, 8, 9, 10]\n[6, 5, 4, 3, 2, 1, 7, 8, 9, 10]\n[5, 4, 3, 2, 1, 6, 7, 8, 9, 10]\n[4, 3, 2, 1, 5, 6, 7, 8, 9, 10]\n[3, 2, 1, 4, 5, 6, 7, 8, 9, 10]\n[2, 1, 3, 4, 5, 6, 7, 8, 9, 10]\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True), 
    ([12, 8, -6, 2, 4, 5, 3, 7, 4, 2], '[8, -6, 2, 4, 5, 3, 7, 4, 2, 12]\n[-6, 2, 4, 5, 3, 7, 4, 2, 8, 12]\n[-6, 2, 4, 3, 5, 4, 2, 7, 8, 12]\n[-6, 2, 3, 4, 4, 2, 5, 7, 8, 12]\n[-6, 2, 3, 4, 2, 4, 5, 7, 8, 12]\n[-6, 2, 3, 2, 4, 4, 5, 7, 8, 12]\n[-6, 2, 2, 3, 4, 4, 5, 7, 8, 12]\n[-6, 2, 2, 3, 4, 4, 5, 7, 8, 12]\n[-6, 2, 2, 3, 4, 4, 5, 7, 8, 12]', [-6, 2, 2, 3, 4, 4, 5, 7, 8, 12], True), 
    (['FunForFun', 'Practice.FunForFun', 'FunforFun'], "['FunForFun', 'FunforFun', 'Practice.FunForFun']\n['FunForFun', 'FunforFun', 'Practice.FunForFun']", ['FunForFun', 'FunforFun', 'Practice.FunForFun'], True), 
    ([37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54], '[23, 0, 17, 12, 37, 31, 46, 72, 88, 54, 100]\n[0, 17, 12, 23, 31, 37, 46, 72, 54, 88, 100]\n[0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]\n[0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]\n[0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]\n[0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]\n[0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]\n[0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]\n[0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]\n[0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]', [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100], True), 
    ([2], '[2]', [2], True), 

    # Hidden Testcases
    ([5, 2, 7, 10, 3, 5, 2, 1, 8, 9], '2529fac619ca0215ada6639c39feb4f1d53e0d82f20de358dc12692891fba99a', 'b4789af97f8cc5a46eb7c90b3ab321488339a9d3c09731baf7a679b05220c76e', False), 
    ([7, 5, 5, 4, 3, 2, 1], '113f7afdc0fc9049bf7feede893688885f2c02ef5f24722556e391e885c10a2f', 'b518438af1011f2e4f4baf630bc00b80d7b41f384b942815d06f5c99a1ae5ca3', False), 
    ([0, 1, -1], 'e5b851fc9277ec870a13985722e20c97d60e5049d9925ee8992a64aec5c8c0eb', 'e512856be455ce3d0249415a73d5c16913698de91538787853bce94b11eaada7', False), 
    ([0, 1, 2, 3, 9, -1], 'fe7e646314fb7d66ac7ce6614e6b810c0227754a8d67a4a9661e9af2a6ac9338', 'e4d84adb7f224ec80acbc1fd7de45109c456e80cd4d36326e3a08b8701588e53', False), 
    ([1, 2, 3, 4, 5, 6, 7, 8, 11, 10, 0], 'db078c0eb2a88397eca2a5ff53015912603c6a81aeb427391005b1efb8e8a514', '8128d5ede96a5d11a114922983789e8de5a27d9b2a07991bfdb22181c70a0a9d', False), 
    ([71, 32, 22, 19, 18, 1, 15, 40], '211971955d96c47119ea023c499d1587fd63df16a6536fac1399226805f24956', '978ab89564586985c5bf115acde16a65d03a44ca61184fe20fde0c56b9863b0a', False)
    ]

def xstrip(s):
    lst = s.split('\n')
    for i in range(len(lst)):
        lst[i]=lst[i].rstrip()
    return "\n".join(lst)

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("arr,result,arrres,testcase",q3_testcases)
def test_q3(capsys,arr,result,arrres,testcase):
    bubble_sort(arr)
    captured,err = capsys.readouterr()
    captured=captured[:-1]
    if testcase == True:
        assert xstrip(captured) == xstrip(result) and arr == arrres
    else:
        assert hashcode(xstrip(captured)) == result and hashcode(arr) == arrres