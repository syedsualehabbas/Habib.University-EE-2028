import pytest
import hashlib

from q1 import push, pop, top, is_empty

push_testcases = [
    # Visible Testcases
    ([None, None, None, None, None], 1, [1, None, None, None, None], True), 
    ([1, None, None, None, None], 2, [1, 2, None, None, None], True), 
    ([1, 2, None, None, None], 3, [1, 2, 3, None, None], True), 
    
    # Hidden Testcases 
    ([1, 2, 3, None, None], 4, '882eebb63dff6f09947f98df0e2859b4de7170472d6d91721d2e9037d7443d17', False), 
    ([1, 2, 3, 4, None], 5, '0c049903ce2330190375d4c1f2e489888c9ebe39daf75b2564e591e8bc1afe72', False)
    ]

pop_testcases = [
    # Visible Testcases
    ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, None], True), 
    ([1, 2, 3, 4, None], 4, [1, 2, 3, None, None], True), 
    ([1, 2, 3, None, None], 3, [1, 2, None, None, None], True),

    # Hidden Testcases
    ([1, 2, None, None, None], 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', '64fbbbb484c06e10a55ae21de03880fe96b54897d4f5946b23d8a40925fb3845', False), 
    ([1, None, None, None, None], '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', 'ed574e6bbc2fa787fa38baf99f0ca6903b20452f895756782f39391093ee957e', False)
    ]

top_testcases = [
    # Visible Testcases
    ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5], True), 
    ([1, 2, 3, 4, None], 4, [1, 2, 3, 4, None], True), 
    ([1, 2, 3, None, None], 3, [1, 2, 3, None, None], True),

    # Hidden Testcases 
    ([1, 2, None, None, None], 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', 'c6162e02a82c23176381e31a626463cc2a3660fe4b66596785edcc16c1dd1f9b', False), 
    ([1, None, None, None, None], '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', '64fbbbb484c06e10a55ae21de03880fe96b54897d4f5946b23d8a40925fb3845', False)
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

@pytest.mark.parametrize("list,value,result,testcase", push_testcases)
def test_push(list,value,result,testcase):
    if testcase == True:
        assert push(list,value) == None and list == result
    else:
        assert push(list,value) == None and hashcode(list) == result

@pytest.mark.parametrize("list,result,updatedList,testcase", pop_testcases)
def test_pop(list,result,updatedList,testcase):
    if testcase == True:
        assert pop(list) == result and list == updatedList
    else:
        assert hashcode(pop(list)) == result and hashcode(list) == updatedList

@pytest.mark.parametrize("list,result,updatedList,testcase", top_testcases)
def test_top(list,result,updatedList,testcase):
    if testcase == True:
        assert top(list) == result and list == updatedList
    else:
        assert hashcode(top(list)) == result and hashcode(list) == updatedList

@pytest.mark.parametrize("list,result,updatedList,testcase", isempty_testcases)
def test_IsEmpty(list,result,updatedList,testcase):
    if testcase == True:
        assert is_empty(list) == result and list == updatedList and type(is_empty(list)) == bool
    else:
        assert hashcode(is_empty(list)) == result and hashcode(list) == updatedList and type(is_empty(list)) == bool