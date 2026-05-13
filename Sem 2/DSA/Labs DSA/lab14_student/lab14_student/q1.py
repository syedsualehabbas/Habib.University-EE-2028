import math
def IsEmpty(queue):
    """
    Checks if the queue is empty.

    Args:
        queue (list): The queue to check.

    Returns:
        bool: True if the queue is empty, False otherwise.
    """

    return queue == []

def EnQueue(queue, item, priority):
    """
    Adds or updates an item with the specified priority in the queue.

    Args:
        queue (list): A list of (item, priority) tuples.
        item (any): The item to add or update.
        priority (int): The item's priority.

    Returns:
        None
    """

    count = 0
    for i, _ in queue:
        if i == item:
            queue[count] = item, priority
            return None
        count += 1
    queue.append((item, priority))


def DeQueue(queue):
    """
    Removes and returns the key with the minimum priority.

    Args:
        queue (list): A list of (key, priority) tuples.

    Returns:
        any: The key with the minimum priority.
    """

    # WRITE YOUR CODE HERE
    check=math.inf
    for i in queue:
        if i[1]<check:
            check=i[1]
    for i in queue:
        if i[1]==check:
            queue.pop(queue.index(i))
            return i[0]
    


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    queue = []
    EnQueue(queue,'A',1)
    EnQueue(queue,'B',2)
    EnQueue(queue,'C',3)
    EnQueue(queue,'D',4)
    EnQueue(queue,'E',5)
    EnQueue(queue,'F',6)
    EnQueue(queue,'G',7)
    print(queue)            # Should print: [('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5), ('F', 6), ('G', 7)]
    print(DeQueue(queue))   # Should print: A
    print(queue)            # Should print: [('B', 2), ('C', 3), ('D', 4), ('E', 5), ('F', 6), ('G', 7)]
    print(DeQueue(queue))   # Should print: B
    print(queue)            # Should print: [('C', 3), ('D', 4), ('E', 5), ('F', 6), ('G', 7)]

    print('-------------------------------------------------------------------')

    queue = []
    EnQueue(queue, 'A', 10)
    EnQueue(queue, 'B', 2)
    EnQueue(queue, 'C', 5)
    
    print(queue)            # Should print: [('A', 10), ('B', 2), ('C', 5)]
    print(DeQueue(queue))   # Should print: B
    print(queue)            # Should print: [('A', 10), ('C', 5)]
    print(DeQueue(queue))   # Should print: C
    print(queue)            # Should print: [('A', 10)]

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q1.py