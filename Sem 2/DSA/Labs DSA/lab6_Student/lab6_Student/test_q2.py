import pytest
import hashlib
from sys import stderr
from q2 import *

q2_testcases = [
    # Visible Testcases
    ([54, 26, 93, 17, 77, 31, 44, 55, 20], '[26, 54, 93, 17, 77, 31, 44, 55, 20]\n[26, 54, 93, 17, 77, 31, 44, 55, 20]\n[17, 26, 54, 93, 77, 31, 44, 55, 20]\n[17, 26, 54, 77, 93, 31, 44, 55, 20]\n[17, 26, 31, 54, 77, 93, 44, 55, 20]\n[17, 26, 31, 44, 54, 77, 93, 55, 20]\n[17, 26, 31, 44, 54, 55, 77, 93, 20]\n[17, 20, 26, 31, 44, 54, 55, 77, 93]', [17, 20, 26, 31, 44, 54, 55, 77, 93], True), 
    (['Aisha', 'Nadia', 'Waqar', 'Saleha', 'Hasan', 'Shahid', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj'], "['Aisha', 'Nadia', 'Waqar', 'Saleha', 'Hasan', 'Shahid', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj']\n['Aisha', 'Nadia', 'Waqar', 'Saleha', 'Hasan', 'Shahid', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj']\n['Aisha', 'Nadia', 'Saleha', 'Waqar', 'Hasan', 'Shahid', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj']\n['Aisha', 'Hasan', 'Nadia', 'Saleha', 'Waqar', 'Shahid', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj']\n['Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shahid', 'Waqar', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj']\n['Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Waqar', 'Abdullah', 'Umair', 'Taj']\n['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Waqar', 'Umair', 'Taj']\n['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Umair', 'Waqar', 'Taj']\n['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']", ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar'], True), 
    ([4, 1, 3, 9, 7], '[1, 4, 3, 9, 7]\n[1, 3, 4, 9, 7]\n[1, 3, 4, 9, 7]\n[1, 3, 4, 7, 9]', [1, 3, 4, 7, 9], True), 
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], '[9, 10, 8, 7, 6, 5, 4, 3, 2, 1]\n[8, 9, 10, 7, 6, 5, 4, 3, 2, 1]\n[7, 8, 9, 10, 6, 5, 4, 3, 2, 1]\n[6, 7, 8, 9, 10, 5, 4, 3, 2, 1]\n[5, 6, 7, 8, 9, 10, 4, 3, 2, 1]\n[4, 5, 6, 7, 8, 9, 10, 3, 2, 1]\n[3, 4, 5, 6, 7, 8, 9, 10, 2, 1]\n[2, 3, 4, 5, 6, 7, 8, 9, 10, 1]\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True), 
    ([12, 8, -6, 2, 4, 5, 3, 7, 4, 2], '[8, 12, -6, 2, 4, 5, 3, 7, 4, 2]\n[-6, 8, 12, 2, 4, 5, 3, 7, 4, 2]\n[-6, 2, 8, 12, 4, 5, 3, 7, 4, 2]\n[-6, 2, 4, 8, 12, 5, 3, 7, 4, 2]\n[-6, 2, 4, 5, 8, 12, 3, 7, 4, 2]\n[-6, 2, 3, 4, 5, 8, 12, 7, 4, 2]\n[-6, 2, 3, 4, 5, 7, 8, 12, 4, 2]\n[-6, 2, 3, 4, 4, 5, 7, 8, 12, 2]\n[-6, 2, 2, 3, 4, 4, 5, 7, 8, 12]', [-6, 2, 2, 3, 4, 4, 5, 7, 8, 12], True),     
    (['FunForFun', 'Practice.FunForFun', 'FunforFun'], "['FunForFun', 'Practice.FunForFun', 'FunforFun']\n['FunForFun', 'FunforFun', 'Practice.FunForFun']", ['FunForFun', 'FunforFun', 'Practice.FunForFun'], True), 

    # Hidden Testcases
    ([37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54], 'ee72d76e6e2f05728ebba6dbdad74bedc29854e545c7cde519c37b9b80c07da2', '1e9c261d574b2ee99aeae7f6de07cbc7a6cc6f487b79e1a80a15443fb300ad04', False), 
    ([5, 2, 7, 10, 3, 5, 2, 1, 8, 9], '0d01791eb7c76b6c98505c97890ff721bf790dd3da9f1ed3594f1cc719ab9906', 'b4789af97f8cc5a46eb7c90b3ab321488339a9d3c09731baf7a679b05220c76e', False), 
    ([7, 5, 5, 4, 3, 2, 1], 'af4f9e488658c96b37455be14e5ef85afda38b5192327345b66af03f7e217fd7', 'b518438af1011f2e4f4baf630bc00b80d7b41f384b942815d06f5c99a1ae5ca3', False), 
    ([0, 1, -1], 'c64a7316f0c0f5a95b34595561842dac2df05de71720e7efcb9e38f58f8f49df', 'e512856be455ce3d0249415a73d5c16913698de91538787853bce94b11eaada7', False), 
    ([0, 1, 2, 3, 9, -1], '8752e80f3066d5353ca5419af042b4520ad65fdaea39edf6e77578d5a3d9c00d', 'e4d84adb7f224ec80acbc1fd7de45109c456e80cd4d36326e3a08b8701588e53', False), 
    ([1, 2, 3, 4, 5, 6, 7, 8, 11, 10, 0], '128babfcd962a17e0649e29adcaa0cac232a379fbfd34f8b8090887bc5e11a59', '8128d5ede96a5d11a114922983789e8de5a27d9b2a07991bfdb22181c70a0a9d', False), 
    ([71, 32, 22, 19, 18, 1, 15, 40], '2e005af087ad6733f591a9efb26adf3bd2da99f939e2c6114027e2e3d98aa808', '978ab89564586985c5bf115acde16a65d03a44ca61184fe20fde0c56b9863b0a', False)
    ]

def xstrip(s):
    lst = s.split('\n')
    for i in range(len(lst)):
        lst[i]=lst[i].rstrip()
    return "\n".join(lst)

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("arr,result,arrres,testcase",q2_testcases)
def test_q2(capsys,arr,result,arrres,testcase):
    insertion_sort(arr)
    captured,err = capsys.readouterr()
    captured=captured[:-1]
    if testcase == True:
        assert xstrip(captured) == xstrip(result) and arr == arrres
    else:
        assert hashcode(xstrip(captured)) == result and hashcode(arr) == arrres