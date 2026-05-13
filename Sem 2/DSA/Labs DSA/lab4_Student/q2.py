from listADT import *

# ** Tip: Try using ListADT helper functions  where applicable.

def enQueue(lst, item):
    """
    Adds an element to the end of the queue.
    
    Parameters:
    lst (list): The queue represented as a list.
    item (any): The item to be added to the queue.
    
    Returns:
    None
    """

    # WRITE YOUR CODE HERE
    Insert(lst, NumberOfElements(lst),item)
    pass


def deQueue(lst):
    """
    Removes and returns the element at the front of the queue.
    
    Parameters:
    lst (list): The queue represented as a list.
    
    Returns:
    any: The item that was removed from the front of the queue.
    """

    # WRITE YOUR CODE HERE
    a=Get(lst,0)
    RemoveFromStart(lst)
    return a


def front(lst):
    """
    Returns the element at the front of the queue without removing it.
    
    Parameters:
    lst (list): The queue represented as a list.
    
    Returns:
    any: The element at the front of the queue.
    """

    # WRITE YOUR CODE HERE
    return Get(lst,0)
    pass


def is_empty(lst):
    """
    Checks if the queue is empty.
    
    Parameters:
    lst (list): The queue represented as a list.
    
    Returns:
    bool: True if the queue is empty, False otherwise.
    """

    # WRITE YOUR CODE HERE
    return IsEmpty(lst)
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    Queue = Initialize(5)   # Initialize a queue of size 5

    print(is_empty(Queue))  # As queue is empty, it should print: True

    enQueue(Queue, 5)
    print(Queue)            # Should print: [5, None, None, None, None]

    print(is_empty(Queue))  # As queue is not empty, it should print: False

    enQueue(Queue, 7)
    print(Queue)            # Should print: [5, 7, None, None, None]

    print(front(Queue))     # As 5 is on front of the queue, it should print: 5

    print(deQueue(Queue))   # Should remove the integer 5 from queue and print: 5

    print(Queue)            # Should print the entire queue: [7, None, None, None, None]

    print(front(Queue))     # As 7 is on front of the queue, it should print: 7

    print(deQueue(Queue))   # Should remove the integer 7 from queue and print: 7

    print(Queue)            # Should print: [None, None, None, None, None]

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q2.py