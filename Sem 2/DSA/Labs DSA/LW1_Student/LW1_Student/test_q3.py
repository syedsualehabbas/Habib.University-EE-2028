import pytest
import hashlib
from q3 import compute_profit

q3_testcases = [
    # Visible Testcases
    ([('25-Jan-2001', 43.5, 25, 'CAT', 92.45), ('25-Jan-2001', 42.8, 50, 'DD', 51.19), ('25-Jan-2001', 42.1, 75, 'EK', 34.87), ('25-Jan-2001', 37.58, 100, 'GM', 37.58)], 1101.0, True), 
    ([('25-Jan-2001', 43.5, 25, 'CAT', 92.45), ('25-Jan-2001', 42.8, 50, 'DD', 51.19)], 1643.25, True), 
    ([('25-Jan-2001', 43.5, 25, 'CAT', 92.45), ('25-Jan-2001', 42.8, 50, 'DD', 51.19), ('25-Jan-2001', 42.1, 75, 'EK', 34.87), ('25-Jan-2001', 37.58, 100, 'GM', 37.58), ('25-Jan-2001', 43.5, 25, 'CAT', 92.45), ('25-Jan-2001', 42.8, 50, 'DD', 51.19), ('25-Jan-2001', 42.1, 75, 'EK', 34.87), ('25-Jan-2001', 37.58, 100, 'GM', 37.58)], 2202.0, True), 

    # Hidden Testcases
    ([('25-Jan-2001', 43.5, 25, 'CAT', 92.45)], 'f8605d1e89f14c03ccd36ba6035fb63d56da05d27b311a3ef9dcf054781a995c', False),
    ([('25-Jan-2001', 43.5, 25, 'CAT', 22.45), ('25-Jan-2001', 42.8, 50, 'DD', 21.19), ('25-Jan-2001', 42.1, 75, 'EK', 34.87), ('25-Jan-2001', 37.58, 100, 'GM', 37.58), ('25-Jan-2001', 43.5, 25, 'CAT', 32.45), ('25-Jan-2001', 42.8, 50, 'DD', 31.19), ('25-Jan-2001', 42.1, 75, 'EK', 34.87), ('25-Jan-2001', 37.58, 100, 'GM', 37.58)], '2c333be25e0bd0146b747d33b5957b9711b3598c8c5e0118548a1ed1754141cd', False), 
    ([('25-Jan-2001', 43.0, 25, 'CAT', 92.0), ('25-Jan-2001', 42.0, 50, 'DD', 51.0), ('25-Jan-2001', 42.0, 75, 'EK', 34.0), ('25-Jan-2001', 37.0, 100, 'GM', 37.0)], '1d439e0a7c0d46fc4e62e38b72724b12f53dbd2c4c26a7cbc05526e469ef9e7a', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("stock_info,result, testcase",q3_testcases)
def test_q3(stock_info, result, testcase):
    if testcase == True:
        assert round(compute_profit(stock_info),2) == result
    else:
        assert hashcode(round(compute_profit(stock_info),2)) == result