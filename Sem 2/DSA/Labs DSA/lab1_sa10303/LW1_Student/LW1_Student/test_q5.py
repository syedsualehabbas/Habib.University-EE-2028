import hashlib
import pytest
from q5 import update_record

q5_testcases = [
    # Visible Testcases
    ([('E001', 'Manager', 80000, 5), ('E002', 'Developer', 60000, 2), ('E003', 'Analyst', 50000, 1), ('E004', 'Designer', 70000, 3)], 'E001', 'ID', 'E005', 'ID cannot be updated', [('E001', 'Manager', 80000, 5), ('E002', 'Developer', 60000, 2), ('E003', 'Analyst', 50000, 1), ('E004', 'Designer', 70000, 3)], True), 
    ([('E001', 'Manager', 80000, 5), ('E002', 'Developer', 60000, 2), ('E003', 'Analyst', 50000, 1), ('E004', 'Designer', 70000, 3)], 'E001', 'Position', 'Senior Manager', 'Record updated', [('E001', 'Senior Manager', 80000, 5), ('E002', 'Developer', 60000, 2), ('E003', 'Analyst', 50000, 1), ('E004', 'Designer', 70000, 3)], True), 
    ([('E001', 'Manager', 80000, 5), ('E002', 'Developer', 60000, 2), ('E003', 'Analyst', 50000, 1), ('E004', 'Designer', 70000, 3)], 'E005', 'Salary', 55000, 'Record not found', [('E001', 'Manager', 80000, 5), ('E002', 'Developer', 60000, 2), ('E003', 'Analyst', 50000, 1), ('E004', 'Designer', 70000, 3)], True), 
    ([('E001', 'Manager', 80000, 5), ('E002', 'Developer', 60000, 2), ('E003', 'Analyst', 50000, 1), ('E004', 'Designer', 70000, 3)], 'E002', 'Position', 'Senior Developer', 'Record updated', [('E001', 'Manager', 80000, 5), ('E002', 'Senior Developer', 60000, 2), ('E003', 'Analyst', 50000, 1), ('E004', 'Designer', 70000, 3)], True), 
    
    # Hidden Testcases
    ([('E001', 'Manager', 80000, 5), ('E002', 'Developer', 60000, 2), ('E003', 'Analyst', 50000, 1), ('E004', 'Designer', 70000, 3)], 'E003', 'Salary', 55000, 'cf54c5d03201021de14c552f115cc3fb59cff01bbf8160952f5212999c5936e1', '03ebd9d2420df9865ff9381a1227f7b945ee943377adb00d6b7c85c8db76eb3e', False), 
    ([('E001', 'Manager', 80000, 5), ('E002', 'Developer', 60000, 2), ('E003', 'Analyst', 50000, 1), ('E004', 'Designer', 70000, 3)], 'E004', 'Experience', 4, 'cf54c5d03201021de14c552f115cc3fb59cff01bbf8160952f5212999c5936e1', '99efa1fb0f8011c6db98c5f68903857fd11b0b8e4373d27d62b59aba9624abfe', False), 
    ([('E001', 'Manager', 80000, 5), ('E002', 'Developer', 60000, 2), ('E003', 'Analyst', 50000, 1), ('E004', 'Designer', 70000, 3)], 'E003', 'ID', 'E005', '8c0f5197a938f5b322033e2cc3ca340cd84836c05e6bac81f0cee118f01f6403', '504cb64ef6cc46b6f83fd0fd7f75e2888941efe72f691f42ef998c130fdc1e99', False), 
    ([('E001', 'Manager', 80000, 5), ('E002', 'Developer', 60000, 2), ('E003', 'Analyst', 50000, 1), ('E004', 'Designer', 70000, 3)], 'E005', 'Position', 'Senior Developer', '60de363f36743d355c615af8528d592aa944790b679331bd6fa8c066b8f9ba6e', '504cb64ef6cc46b6f83fd0fd7f75e2888941efe72f691f42ef998c130fdc1e99', False)
    ]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()


@pytest.mark.parametrize("employee_records, ID, record_title, data,result1, result2, testcase", q5_testcases)
def test_q5(employee_records, ID, record_title, data, result1, result2, testcase):
    if testcase == True:
        assert update_record(employee_records, ID, record_title, data) == result1 and employee_records == result2
    else:
        assert hashcode(update_record(employee_records, ID, record_title, data)) == result1 and hashcode(employee_records) == result2