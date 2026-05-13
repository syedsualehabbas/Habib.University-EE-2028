# Tip: Import and use created Queue functions from q2. (from q2 import *)
from q2 import *

def stutter(A, n):
    """
    Replaces every element in the queue with n copies of itself.
    
    Parameters:
    A (queue): The input queue represented as a list.
    n (int): The number of copies to replace each element with.
    
    Returns:
    list: The modified queue with each element replaced by n copies of itself.

    Note:
        1. Only Queue ADT Operations are to be used in your implementation:
            ( Initialize() , enqueue() , dequeue() , front() and is_empty() ).
        2. You are allowed to make a new queue to store up the results.
        3. You are not allowed to use stack or list.
    """

    # WRITE YOUR CODE HERE
    que=Initialize(len(A)*n)
    while is_empty(A)!=True:
        b=deQueue(A)
        for j in range(n):
            enQueue(que,b)
    return que

    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print(stutter([1, 2, 3], 2))
    # Should print: [1, 1, 2, 2, 3, 3]

    print(stutter(['a', 'b', 'c'], 3))
    # Should print: ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']

    print(stutter(["queue"], 10))
    # Should print: ['queue', 'queue', 'queue', 'queue', 'queue', 'queue', 'queue', 'queue', 'queue', 'queue']

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q4.py