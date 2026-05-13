import pytest
import hashlib
from q2 import total_distance

q2_testcases = [
    # Visible Testcases
    ([('UP', 5), ('DOWN', 3), ('LEFT', 3), ('RIGHT', 2)], 3, True), 
    ([('RIGHT', 1), ('DOWN', 0), ('LEFT', -2), ('DOWN', -4)], 5, True), 
    ([('UP', 0)], 0, True), 
    ([('UP', 33), ('LEFT', -57), ('UP', -14), ('UP', -10), ('UP', -50), ('DOWN', -6), ('RIGHT', 32), ('RIGHT', -16), ('UP', 55), ('LEFT', 33), ('UP', 87), ('RIGHT', -37), ('RIGHT', 23), ('RIGHT', 25), ('UP', 92), ('UP', 0), ('UP', 60), ('DOWN', -69), ('DOWN', 89), ('LEFT', -64), ('UP', -9), ('UP', -71), ('UP', -28), ('UP', -81), ('LEFT', 43), ('RIGHT', 30), ('LEFT', -80), ('DOWN', 66), ('RIGHT', -36), ('RIGHT', 37), ('LEFT', -91), ('DOWN', -68), ('UP', 69), ('LEFT', 39), ('LEFT', -99), ('RIGHT', -56), ('LEFT', -40), ('DOWN', 7), ('UP', -61), ('LEFT', -75), ('DOWN', -53), ('RIGHT', -64), ('UP', -37), ('LEFT', 99), ('RIGHT', -5), ('RIGHT', -83), ('DOWN', -55), ('UP', 81), ('LEFT', -18)], 261, True), 
    ([('LEFT', -43), ('UP', -62), ('UP', 43), ('DOWN', 60), ('RIGHT', 85), ('DOWN', 70), ('UP', 20), ('LEFT', -96), ('UP', 86), ('DOWN', 2), ('DOWN', -57), ('LEFT', -70), ('DOWN', 4), ('DOWN', -36), ('LEFT', 99), ('UP', 18), ('DOWN', 24), ('DOWN', -18), ('LEFT', 30), ('RIGHT', 43), ('DOWN', 94), ('DOWN', 68), ('RIGHT', 65), ('RIGHT', 71), ('LEFT', 79), ('LEFT', -21), ('LEFT', -99), ('UP', 0), ('UP', 30), ('LEFT', -58), ('LEFT', 59), ('LEFT', 22), ('UP', 35), ('UP', -21), ('LEFT', 87), ('RIGHT', 77), ('UP', 4), ('LEFT', 86), ('UP', -55), ('UP', 57), ('UP', 42), ('DOWN', 15), ('RIGHT', -32), ('DOWN', 4), ('DOWN', 48), ('RIGHT', 37), ('RIGHT', 55), ('DOWN', -67), ('RIGHT', 61), ('RIGHT', -80), ('UP', 65), ('DOWN', -26), ('LEFT', 67), ('LEFT', 40), ('RIGHT', 27), ('UP', 8), ('LEFT', 63), ('UP', -45), ('RIGHT', -96), ('LEFT', 14), ('LEFT', -72), ('UP', 90), ('UP', -51), ('RIGHT', 74), ('UP', -29), ('UP', -27), ('UP', -41), ('RIGHT', 42), ('DOWN', 19), ('RIGHT', 76), ('UP', 33)], 319, True), 

    # Hidden Testcases
    ([('DOWN', -23), ('DOWN', 24), ('RIGHT', -7), ('RIGHT', 15), ('RIGHT', 77), ('UP', 74), ('LEFT', 4), ('UP', 7), ('DOWN', -24), ('LEFT', 32), ('DOWN', -22), ('RIGHT', -62), ('UP', 81), ('DOWN', -21), ('LEFT', -68), ('LEFT', -94), ('UP', -37), ('DOWN', -3), ('RIGHT', -79), ('LEFT', 35), ('RIGHT', -2), ('RIGHT', 21), ('DOWN', -97), ('RIGHT', -12), ('LEFT', -12), ('LEFT', -98), ('DOWN', -26), ('UP', 88), ('UP', 23), ('LEFT', 92), ('RIGHT', 23)], '155d1cf609cedded2fbc27a4646de87ce7f7de2913b1e5a1bbf148a6df483e19', False), 
    ([('UP', 70), ('LEFT', 7), ('LEFT', -38), ('LEFT', 9), ('LEFT', 11), ('LEFT', -60), ('DOWN', 95), ('RIGHT', 79), ('UP', 58), ('DOWN', -96), ('LEFT', -30), ('UP', -84), ('RIGHT', -51), ('DOWN', -46), ('UP', -15), ('DOWN', 76), ('DOWN', -99), ('RIGHT', 4), ('DOWN', -96), ('RIGHT', -70), ('DOWN', 45), ('RIGHT', 72), ('RIGHT', 51), ('RIGHT', -59), ('LEFT', -78), ('UP', -35), ('DOWN', 85), ('LEFT', -22), ('DOWN', -36), ('RIGHT', 45), ('RIGHT', 93), ('DOWN', -66)], 'b98880883fd8d975260f1807fa46a5156fcc4cc82bf6d657a417d8bb4e42cd55', False), 
    ([('RIGHT', -78), ('DOWN', -23), ('RIGHT', 77), ('DOWN', 35), ('UP', -75), ('RIGHT', -76), ('UP', 35), ('LEFT', 55), ('RIGHT', -20), ('DOWN', -79), ('LEFT', -59), ('LEFT', 21), ('UP', -9), ('DOWN', -40), ('LEFT', -60), ('LEFT', 93), ('DOWN', 85), ('DOWN', 52), ('RIGHT', -49), ('LEFT', 52), ('UP', -30), ('RIGHT', 22), ('UP', -73), ('DOWN', -41), ('DOWN', -93), ('LEFT', 89), ('DOWN', 71), ('UP', -61), ('DOWN', 45), ('DOWN', -51), ('UP', -10), ('UP', -8), ('UP', 40), ('UP', 7)], '2289b221b39605c3494e7290856218e931c00af556cf7a07827108193b276511', False), 
    ([('RIGHT', -93), ('DOWN', 92), ('LEFT', -12), ('DOWN', -10), ('LEFT', 79), ('RIGHT', 69), ('DOWN', 49), ('RIGHT', 67), ('RIGHT', -43), ('DOWN', 15), ('DOWN', -56), ('DOWN', -33), ('UP', 32), ('UP', 0), ('DOWN', -60), ('RIGHT', -40), ('RIGHT', -78), ('LEFT', -48), ('UP', -32), ('LEFT', 18), ('DOWN', -47), ('LEFT', 85), ('DOWN', -50), ('UP', -44), ('LEFT', 38), ('LEFT', -20), ('UP', 32), ('DOWN', -84), ('DOWN', -77), ('DOWN', 32), ('RIGHT', -8), ('DOWN', 70), ('RIGHT', 0), ('RIGHT', -59), ('DOWN', -74), ('RIGHT', 16), ('LEFT', 21), ('RIGHT', 86), ('UP', -62), ('LEFT', 80), ('DOWN', -13), ('UP', 37), ('UP', 76), ('DOWN', 56), ('RIGHT', 94), ('DOWN', 16), ('RIGHT', -59), ('LEFT', 23), ('DOWN', 57), ('LEFT', 65), ('UP', -6), ('UP', 45), ('LEFT', 70), ('RIGHT', -3), ('UP', 82), ('LEFT', 55), ('UP', -60)], 'f89f8d0e735a91c5269ab08d72fa27670d000e7561698d6e664e7b603f5c4e40', False), 
    ([('UP', -20), ('LEFT', 56), ('DOWN', -90), ('RIGHT', -29), ('LEFT', -29), ('DOWN', -78), ('DOWN', 61), ('UP', -83), ('RIGHT', -95), ('LEFT', -34), ('UP', 39), ('LEFT', -59), ('LEFT', 85), ('DOWN', -19), ('DOWN', 59), ('DOWN', 68), ('RIGHT', 34), ('DOWN', -12), ('RIGHT', 31), ('DOWN', 76), ('RIGHT', -5)], '1d0ebea552eb43d0b1e1561f6de8ae92e3de7f1abec52399244d1caed7dbdfa6', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("movements,result,testcase",q2_testcases)
def test_q2(movements, result, testcase):
    if testcase == True:
        assert total_distance(movements) == result
    else:
        assert hashcode(total_distance(movements)) == result