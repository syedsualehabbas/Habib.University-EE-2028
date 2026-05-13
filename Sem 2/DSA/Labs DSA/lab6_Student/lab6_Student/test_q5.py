import pytest
import hashlib
from sys import stderr
from q5 import *

q5_testcases = [
    # Visible Testcases
    ([{"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"}, {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"}, {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"}, {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}], "ID", [{'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'}, {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'}, {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}, {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}], True),
    ([{"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"}, {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"}, {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"}, {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}], "Length", [{'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}, {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'}, {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'}, {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}], True),

    # Hidden Testcases
    ([{"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"}, {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"}, {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"}, {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}],"Breadth",'2e6ab76b9ca1b869b519f37e536fad66ce841da2c4f133bc693a79fbbd5c851b', False),
    ([{"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"}, {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"}, {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"}, {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}],"Color",'4ea76e4f6d055254266c92f05e87a71e156e0cebd3e4d17c735c7b9788af4e28', False)
    ]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("rectangle_records,record_title,result,testcase", q5_testcases)
def test_q5(rectangle_records,record_title,result,testcase):
    if testcase == True:
        assert sort_rectangles(rectangle_records, record_title) == result and rectangle_records == result
    else:
        assert hashcode(sort_rectangles(rectangle_records, record_title)) == result and hashcode(rectangle_records) == result