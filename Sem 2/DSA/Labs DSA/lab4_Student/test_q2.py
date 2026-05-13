import pytest
import hashlib

from q2 import enQueue, deQueue, front, is_empty

enQueue_testcases = [
    # Visible Testcases
    ([None, None, None, None, None], 1, [1, None, None, None, None], True), 
    ([1, None, None, None, None], 2, [1, 2, None, None, None], True), 
    ([1, 2, None, None, None], 3, [1, 2, 3, None, None], True),

    # Hidden Testcases 
    ([1, 2, 3, None, None], 4, '882eebb63dff6f09947f98df0e2859b4de7170472d6d91721d2e9037d7443d17', False), 
    ([1, 2, 3, 4, None], 5, '0c049903ce2330190375d4c1f2e489888c9ebe39daf75b2564e591e8bc1afe72', False)
    ]

deQueue_testcases = [
    # Visible Testcases
    ([1, 2, 3, 4, 5], 1, [2, 3, 4, 5, None], True), 
    ([2, 3, 4, 5, None], 2, [3, 4, 5, None, None], True), 
    ([3, 4, 5, None, None], 3, [4, 5, None, None, None], True), 

    # Hidden Testcases 
    ([4, 5, None, None, None], '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a', '6f4d329a7e940a3662181357a2381317a359bd9e1edb5895fa0aae8c698230ff', False), 
    ([5, None, None, None, None], 'ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d', 'ed574e6bbc2fa787fa38baf99f0ca6903b20452f895756782f39391093ee957e', False)
    ]

front_testcases = [
    # Visible Testcases
    ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5], True), 
    ([2, 3, 4, 5, None], 2, [2, 3, 4, 5, None], True), 
    ([3, 4, 5, None, None], 3, [3, 4, 5, None, None], True), 
    
    # Hidden Testcases 
    ([4, 5, None, None, None], '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a', 'e16b7a14bfbe98a207ab1a270cfcf0d0f07bbc79111fd4669f03f9cfc7d390e5', False), 
    ([5, None, None, None, None], 'ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d', '6f4d329a7e940a3662181357a2381317a359bd9e1edb5895fa0aae8c698230ff', False)
    ]

isempty_testcases = [
    # Visible Testcases
    ([None, None, None, None, None], True, [None, None, None, None, None], True), 
    ([1, None, None, None, None], False, [1, None, None, None, None], True), 
    
    # Hidden Testcases 
    ([1, 2, 3, 4, 5], '60a33e6cf5151f2d52eddae9685cfa270426aa89d8dbc7dfb854606f1d1a40fe', '0c049903ce2330190375d4c1f2e489888c9ebe39daf75b2564e591e8bc1afe72', False),
    ([None], '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18', '778d5d27b716881dd9d3b58baaed62878f93076984cf0cbb45d393bedf363cb2', False)
    ]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("list,value,result,testcase", enQueue_testcases)
def test_enqueue(list,value,result,testcase):
    if testcase == True:
        assert enQueue(list,value) == None and list == result
    else:
        assert enQueue(list,value) == None and hashcode(list) == result

@pytest.mark.parametrize("list,result,updatedList,testcase", deQueue_testcases)
def test_dequeue(list,result,updatedList,testcase):
    if testcase == True:
        assert deQueue(list) == result and list == updatedList
    else:
        assert hashcode(deQueue(list)) == result and hashcode(list) == updatedList

@pytest.mark.parametrize("list,result,updatedList,testcase", front_testcases)
def test_front(list,result,updatedList,testcase):
    if testcase == True:
        assert front(list) == result and list == updatedList
    else:
        assert hashcode(front(list)) == result and hashcode(list) == updatedList

@pytest.mark.parametrize("list,result,updatedList,testcase", isempty_testcases)
def test_IsEmpty(list,result,updatedList,testcase):
    if testcase==True:
        assert is_empty(list) == result and list == updatedList and type(is_empty(list)) == bool
    else:
        assert hashcode(is_empty(list)) == result and hashcode(list) == updatedList and type(is_empty(list)) == bool