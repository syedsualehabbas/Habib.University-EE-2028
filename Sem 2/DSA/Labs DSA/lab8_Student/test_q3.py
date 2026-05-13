import pytest
import hashlib
from sys import stderr
from q3 import *

q3_testcases = [
    # Visible Testcases   
    ([{"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"}, {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"}, {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"}, {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}], "Length", "[{'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}, {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'}, {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'}, {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}]\n[{'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}, {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'}, {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'}, {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}]", [{'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}, {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'}, {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'}, {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}], True),
    ([{"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"}, {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"}, {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"}, {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}], "ID", "[{'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'}, {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'}, {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}, {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}]\n[{'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'}, {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'}, {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}, {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}]\n[{'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'}, {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'}, {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}, {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}]", [{'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'}, {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'}, {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}, {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}], True),

    # Hidden Testcases
    ([{"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"}, {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"}, {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"}, {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}], "Breadth", '2778aca20b3b668d7015d327d6863e4b628cf3c923b5be877d8b931c2ed3ff1d', '2e6ab76b9ca1b869b519f37e536fad66ce841da2c4f133bc693a79fbbd5c851b', False),
    ([{"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"}, {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"}, {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"}, {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}], "Color", 'c72e03a1c7a19902ec68c9246a47f2ee5557c843cdd8613c0e37a224d840f2b6', '4ea76e4f6d055254266c92f05e87a71e156e0cebd3e4d17c735c7b9788af4e28', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("rectangle_records, title, result, lstresult, testcase", q3_testcases)
def test_q3(capsys, rectangle_records, title, result, lstresult, testcase):
    quick_sort_rectangles(rectangle_records, 0, len(rectangle_records)-1, title)
    captured, _ = capsys.readouterr()
    if testcase == True:
        assert captured[:-1] == result and rectangle_records == lstresult
    else:
        assert hashcode(captured[:-1]) == result and hashcode(rectangle_records) == lstresult
