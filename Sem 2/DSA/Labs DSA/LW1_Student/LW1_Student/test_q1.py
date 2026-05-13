import pytest
import hashlib
from q1 import last_name_first

q1_testcases = [
    # Visible Testcases
    ([('Ahmed', 'Dawood'), ('Haroon', 'Hussain', 'Fawad', 'Rasheed'), ('Muhammad', 'Faisal', 'Amin')], [('Dawood', 'Ahmed'), ('Rasheed', 'Haroon', 'Hussain', 'Fawad'), ('Amin', 'Muhammad', 'Faisal')], True), 
    ([('Haroon', 'Hussain', 'Fawaz', 'Rasheed'), ('Ahmed', 'Dawood'), ('Haroon', 'Hussain', 'Fawad', 'Rasheed'), ('Aamir', 'Dawood'), ('Muhammad', 'Mohsin', 'Amin'), ('Muhammad', 'Faisal', 'Amin')], [('Rasheed', 'Haroon', 'Hussain', 'Fawaz'), ('Dawood', 'Ahmed'), ('Rasheed', 'Haroon', 'Hussain', 'Fawad'), ('Dawood', 'Aamir'), ('Amin', 'Muhammad', 'Mohsin'), ('Amin', 'Muhammad', 'Faisal')], True), 
    ([('Zara',), ('Lara',), ('Mara',), ('Fara',), ('Sara',), ('Kara',), ('Tara',), ('Hara',), ('Dara',)], [('Zara',), ('Lara',), ('Mara',), ('Fara',), ('Sara',), ('Kara',), ('Tara',), ('Hara',), ('Dara',)], True), 
    ([('Bloody', 'Mary'), ('Bloody', 'Mary'), ('Bloody', 'Mary')], [('Mary', 'Bloody'), ('Mary', 'Bloody'), ('Mary', 'Bloody')], True), 
    ([('Haroon', 'Hussain', 'Fawad', 'Rasheed')], [('Rasheed', 'Haroon', 'Hussain', 'Fawad')], True), 

    # Hidden Testcases
    ([('Haider', 'Iqbal', 'Jumani'), ('Hamza', 'Ahmed'), ('Mohammad', 'Ibrahim', 'Adnan', 'Zafar', 'Dada'), ('Maria', 'Khurram', 'Husain'), ('Maryam', 'Karam', 'Kalwar'), ('Mehtab', 'Juman'), ('Mubaraka', 'Mohammad', 'Shaikh', 'Ali')], '3d5665b4a8149e9e120e4668cafdebf0327acde87d32fe71774ea82796fa7150', False), 
    ([('Mubaraka', 'Mohammad', 'Shaikh', 'Alli'), ('Haider', 'Iqbal', 'Jumani'), ('Maria', 'Hoorram', 'Husain'), ('Hamza', 'Ahmed'), ('Haider', 'Iqbal', 'Hasan', 'Jumani'), ('Mohammad', 'Ibrahim', 'Adnan', 'Zafar', 'Dada'), ('Maria', 'Khurram', 'Husain'), ('Mehtab', 'Arifa', 'Juman'), ('Maryam', 'Karam', 'Kalwar'), ('Mehtab', 'Juman'), ('Hafza', 'Ahmed'), ('Mubaraka', 'Mohammad', 'Shaikh', 'Ali')], '3c89bb5cb44078a61e4453ac5210b84742fb14dab1825db5a4508c4aac750c43', False), 
    ([('Rana',), ('Pana',), ('Lana',), ('Vana',), ('Zana',), ('Sana',), ('Hana',), ('Dana',)], 'c83353d8ff740cf194614bfc1c1f4251db5b9a65ba370c5cab5922b62b434df4', False), 
    ([('Candyman',), ('Candyman',), ('Candyman',), ('Candyman',), ('Candyman',), ('Candyman',)], 'e673ca0735e3fc9abe8b2252e82d2358b997f12778f4f4a7d15abe9da470ad26', False), 
    ([], '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945', False)
]
def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("t,result,testcase",q1_testcases)
def test_q1(t, result, testcase):
    if testcase == True:
        assert last_name_first(t) == None and t == result
    else:
        assert last_name_first(t) == None and hashcode(t) == result