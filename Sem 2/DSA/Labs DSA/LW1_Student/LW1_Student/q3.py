
import math
def compute_profit(stock_info):
    """
    Calculates total profit or loss from stock transactions.

    Parameters:
    stocks (list of tuples): Each tuple contains (purchase date, purchase price, shares, symbol, current price).

    Returns:
    float: Total profit or loss, rounded to two decimal places.
    """
    
    # WRITE YOUR CODE HERE
    a=0
    for i in stock_info:
        a=a+(i[2]*(i[4]-i[1]))
    a=round(a,2)
    return a





#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print(compute_profit([
        ('25-Jan-2001', 43.5, 25, 'CAT', 92.45), 
        ('25-Jan-2001', 42.8, 50, 'DD', 51.19), 
        ('25-Jan-2001', 42.1, 75, 'EK', 34.87), 
        ('25-Jan-2001', 37.58, 100, 'GM', 37.58)
    ]))
    # Should print: 1101.0

    print(compute_profit([
        ('25-Jan-2001', 43.5, 25, 'CAT', 92.45), 
        ('25-Jan-2001', 42.8, 50, 'DD', 51.19)
    ]))
    # Should print: 1643.25

    print(compute_profit([
        ('25-Jan-2001', 43.5, 25, 'CAT', 92.45), 
        ('25-Jan-2001', 42.8, 50, 'DD', 51.19), 
        ('25-Jan-2001', 42.1, 75, 'EK', 34.87), 
        ('25-Jan-2001', 37.58, 100, 'GM', 37.58), 
        ('25-Jan-2001', 43.5, 25, 'CAT', 92.45), 
        ('25-Jan-2001', 42.8, 50, 'DD', 51.19), 
        ('25-Jan-2001', 42.1, 75, 'EK', 34.87), 
        ('25-Jan-2001', 37.58, 100, 'GM', 37.58)
    ]))
    # Should print: 2202.0

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q3.py