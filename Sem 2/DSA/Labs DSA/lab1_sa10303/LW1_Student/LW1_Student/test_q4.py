import pytest
import hashlib
from q4 import remove_user

q4_testcases = [
  # Visible Testcases
  ({'Alice': ('123-456-7890', ['Bob', 'Charlie']), 'Bob': ('987-654-3210', ['Alice', 'David']), 'Charlie': ('111-222-3333', ['Alice']), 'David': ('555-666-7777', ['Bob'])}, 'Alice', {'Bob': ('987-654-3210', ['David']), 'Charlie': ('111-222-3333', []), 'David': ('555-666-7777', ['Bob'])}, True), 
  ({'Alice': ('123-456-7890', []), 'Bob': ('987-654-3210', ['Alice']), 'Charlie': ('111-222-3333', ['Alice']), 'David': ('555-666-7777', ['Bob'])}, 'Alice', {'Bob': ('987-654-3210', []), 'Charlie': ('111-222-3333', []), 'David': ('555-666-7777', ['Bob'])}, True), 

  # Hidden Testcases
  ({'Alice': ('123-456-7890', ['Bob']), 'Bob': ('987-654-3210', ['Alice']), 'Charlie': ('111-222-3333', ['Alice']), 'David': ('555-666-7777', ['Bob'])}, 'Eve', '9893cc4d4ae7166e1f75ccf2e72ef46c91140ccd8b6911a68a7b572bcc6fe666', False), 
  ({'Alice': ('123-456-7890', ['Bob'])}, 'Alice', '44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a', False), 
  ({'Alice': ('123-456-7890', ['Bob', 'Charlie']), 'Bob': ('987-654-3210', ['Alice', 'David']), 'Charlie': ('111-222-3333', ['Alice', 'Bob']), 'David': ('555-666-7777', ['Bob', 'Charlie'])}, 'Alice', '83d5ff55960ba4966581b1eea80380cd6886c80be4899724034ac6592134757e', False)
]


def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()


@pytest.mark.parametrize("users_data,user_name,result,testcase", q4_testcases)
def test_q4(users_data, user_name, result, testcase):
    if testcase==True:
      assert remove_user(users_data, user_name)==None and users_data == result
    else:
      assert remove_user(users_data, user_name)==None and hashcode(users_data) == result