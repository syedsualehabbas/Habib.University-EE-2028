import pytest
from skeleton_decrypt import reverse_karatsuba 
from skeleton_decrypt import main 

DubaDuba_testcases = [
    ([(2, 3, 1), (6, 5, 1), (4, 2, 1)],(42,23,10)),
    ([(1, 3,30), [(3, 6,3), (7, 8,3), (4, 2,3)], [(2, 3,3), (6, 5,3), (4, 2,3)]],(421,233,300)),
    ([[(2, 1,1), (6, 10,1), (4, 9,1)], [(2, 8,1), (6, 20,1), (4, 12,1)], (0, 37,10)],(42, 3791,100))
]
@pytest.mark.parametrize("filename, output",DubaDuba_testcases)
def test_reverse_karatsuba(filename, output):
    assert reverse_karatsuba(filename) == output 
     
def test_input_handling():
    assert(main("hw2_st-master/question1_divideAndConquer/input_decrypt.txt") == [((42,23,10),9660),((421,233,300),29427900), ((42,3791,100),15922200)])
