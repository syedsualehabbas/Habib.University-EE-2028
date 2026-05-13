import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q4 import GetShortestDistanceBetweenCities

testcases =[
    ('Islamabad', 'Nathiagali', [('Islamabad', 'Murree', 49), ('Murree', 'Nathiagali', 36)]),
    ('Islamabad', 'Naran', [('Islamabad', 'Murree', 49), ('Murree', 'Nathiagali', 36), ('Nathiagali', 'Abbottabad', 34), ('Abbottabad', 'Mansehra', 23), ('Mansehra', 'Balakot', 37), ('Balakot', 'Kaghan', 59), ('Kaghan', 'Naran', 22)]),
    ('Islamabad', 'Murree',[('Islamabad', 'Murree', 49)]),
    ('Islamabad', 'Kaghan',[('Islamabad', 'Murree', 49), ('Murree', 'Nathiagali', 36), ('Nathiagali', 'Abbottabad', 34), ('Abbottabad', 'Mansehra', 23), ('Mansehra', 'Balakot', 37), ('Balakot', 'Kaghan', 59)]),
    ('Islamabad', 'Hunza', [('Islamabad', 'Murree', 49), ('Murree', 'Nathiagali', 36), ('Nathiagali', 'Abbottabad', 34), ('Abbottabad', 'Mansehra', 23), ('Mansehra', 'Balakot', 37), ('Balakot', 'Kaghan', 59), ('Kaghan', 'Naran', 22), ('Naran', 'Chilas', 113), ('Chilas', 'Hunza', 306)]),
    ('Skardu', 'Taxila', [('Skardu', 'Muzaffarabad', 484), ('Muzaffarabad', 'Murree', 68), ('Murree', 'Islamabad', 49), ('Islamabad', 'Taxila', 46)]), 
    ('Muzaffarabad', 'Chilas', [('Muzaffarabad', 'Murree', 68), ('Murree', 'Nathiagali', 36), ('Nathiagali', 'Abbottabad', 34), ('Abbottabad', 'Mansehra', 23), ('Mansehra', 'Balakot', 37), ('Balakot', 'Kaghan', 59), ('Kaghan', 'Naran', 22), ('Naran', 'Chilas', 113)]), 
    ('Islamabad', 'Taxila', [('Islamabad', 'Taxila', 46)]), 
    ('Chilas', 'Muzaffarabad', [('Chilas', 'Naran', 113), ('Naran', 'Kaghan', 22), ('Kaghan', 'Balakot', 59), ('Balakot', 'Mansehra', 37), ('Mansehra', 'Abbottabad', 23), ('Abbottabad', 'Nathiagali', 34), ('Nathiagali', 'Murree', 36), ('Murree', 'Muzaffarabad', 68)]), 
    ('Taxila', 'Mansehra', [('Taxila', 'Abbottabad', 74), ('Abbottabad', 'Mansehra', 23)]), 
    ('Muzaffarabad', 'Gilgit', [('Muzaffarabad', 'Murree', 68), ('Murree', 'Nathiagali', 36), ('Nathiagali', 'Abbottabad', 34), ('Abbottabad', 'Mansehra', 23), ('Mansehra', 'Balakot', 37), ('Balakot', 'Kaghan', 59), ('Kaghan', 'Naran', 22), ('Naran', 'Chilas', 113), ('Chilas', 'Gilgit', 133)]), 
    ('Gilgit', 'Malam Jabba', [('Gilgit', 'Chilas', 133), ('Chilas', 'Bisham', 199), ('Bisham', 'Malam Jabba', 61)]), 
    ('Chilas', 'Balakot', [('Chilas', 'Naran', 113), ('Naran', 'Kaghan', 22), ('Kaghan', 'Balakot', 59)]), 
    ('Khunjerab Pass', 'Malam Jabba', [('Khunjerab Pass', 'Hunza', 151), ('Hunza', 'Chilas', 306), ('Chilas', 'Bisham', 199), ('Bisham', 'Malam Jabba', 61)]), 
    ('Abbottabad', 'Murree', [('Abbottabad', 'Nathiagali', 34), ('Nathiagali', 'Murree', 36)]), 
    ('Muzaffarabad', 'Kaghan', [('Muzaffarabad', 'Murree', 68), ('Murree', 'Nathiagali', 36), ('Nathiagali', 'Abbottabad', 34), ('Abbottabad', 'Mansehra', 23), ('Mansehra', 'Balakot', 37), ('Balakot', 'Kaghan', 59)]), 
    ('Taxila', 'Nathiagali', [('Taxila', 'Abbottabad', 74), ('Abbottabad', 'Nathiagali', 34)]), 
    ('Hunza', 'Murree', [('Hunza', 'Chilas', 306), ('Chilas', 'Naran', 113), ('Naran', 'Kaghan', 22), ('Kaghan', 'Balakot', 59), ('Balakot', 'Mansehra', 37), ('Mansehra', 'Abbottabad', 23), ('Abbottabad', 'Nathiagali', 34), ('Nathiagali', 'Murree', 36)]), 
    ('Taxila', 'Gilgit', [('Taxila', 'Abbottabad', 74), ('Abbottabad', 'Mansehra', 23), ('Mansehra', 'Balakot', 37), ('Balakot', 'Kaghan', 59), ('Kaghan', 'Naran', 22), ('Naran', 'Chilas', 113), ('Chilas', 'Gilgit', 133)]), 
    ('Nathiagali', 'Mansehra', [('Nathiagali', 'Abbottabad', 34), ('Abbottabad', 'Mansehra', 23)]),
    ('Mansehra', 'Chilas', [('Mansehra', 'Balakot', 37), ('Balakot', 'Kaghan', 59), ('Kaghan', 'Naran', 22), ('Naran', 'Chilas', 113)])
]


@pytest.mark.parametrize("i", range(len(testcases)))
def test_GetShortestDistanceBetweenCities(i):
    assert GetShortestDistanceBetweenCities(testcases[i][0], testcases[i][1]) == testcases[i][2]