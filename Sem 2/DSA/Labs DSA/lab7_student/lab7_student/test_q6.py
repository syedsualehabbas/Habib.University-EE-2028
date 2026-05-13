import pytest
import hashlib
from q6 import *

q6_testcases = [
    # Visible Testcases
    ([('aa02822', 'ea02822', 80, 65), ('ea02822', 'updated@gmail.com', 80, 65), ('fa08877', 'fa08877@st.habib.edu.pk', 75, 67), ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)], 'randomID', 'Mid2', 50, 'Record not found', [('aa02822', 'ea02822', 80, 65), ('ea02822', 'updated@gmail.com', 80, 65), ('fa08877', 'fa08877@st.habib.edu.pk', 75, 67), ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)], True), 
    ([('aa02822', 'ea02822', 80, 65), ('ea02822', 'ea02822@st.habib.edu.pk', 80, 65), ('fa08877', 'fa08877@st.habib.edu.pk', 66, 67), ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)], 'ea02822', 'Email', 'updated@gmail.com', 'Record updated', [('aa02822', 'ea02822', 80, 65), ('ea02822', 'updated@gmail.com', 80, 65), ('fa08877', 'fa08877@st.habib.edu.pk', 66, 67), ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)], True), 
    ([('aa02822', 'ea02822', 80, 65), ('ea02822', 'updated@gmail.com', 80, 65), ('fa08877', 'fa08877@st.habib.edu.pk', 75, 67), ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)], 'fa08877', 'ID', 'change01', 'ID cannot be updated', [('aa02822', 'ea02822', 80, 65), ('ea02822', 'updated@gmail.com', 80, 65), ('fa08877', 'fa08877@st.habib.edu.pk', 75, 67), ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)], True), 

    # Hidden Testcases
    ([('aa02822', 'ea02822', 80, 65), ('ea02822', 'updated@gmail.com', 80, 65), ('fa08877', 'fa08877@st.habib.edu.pk', 66, 67), ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)], 'fa08877', 'Mid1', 75, 'cf54c5d03201021de14c552f115cc3fb59cff01bbf8160952f5212999c5936e1', '47e93042d67b1d21a11f6ac0c278af6e28a880748fa93456a1a944bd38372ea4', False), 
    ([('aa02822', 'ea02822', 80, 65), ('ea02822', 'updated@gmail.com', 80, 65), ('fa08877', 'fa08877@st.habib.edu.pk', 75, 67), ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)], 'f08877', 'Mid2', 50, '60de363f36743d355c615af8528d592aa944790b679331bd6fa8c066b8f9ba6e', '47e93042d67b1d21a11f6ac0c278af6e28a880748fa93456a1a944bd38372ea4', False), 
    ([('aa02822', 'ea02822', 80, 65), ('ea02822', 'updated@gmail.com', 80, 65), ('fa08877', 'fa08877@st.habib.edu.pk', 75, 67), ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)], 'fa08877', 'Mid2', 50, 'cf54c5d03201021de14c552f115cc3fb59cff01bbf8160952f5212999c5936e1', '7e786db3793580179e1f68bdd408c12e76aa7f0f66dbf64d7423391a967f5d35', False)
    ]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("student_records, ID, record_title, data, result1, result2,testcase",q6_testcases)
def test_q6(student_records, ID, record_title, data,result1,result2,testcase):
    if testcase == True:
        assert update_record(student_records, ID, record_title, data) == result1 and student_records == result2
    else:
        assert hashcode(update_record(student_records, ID, record_title, data)) == result1 and hashcode(student_records) == result2