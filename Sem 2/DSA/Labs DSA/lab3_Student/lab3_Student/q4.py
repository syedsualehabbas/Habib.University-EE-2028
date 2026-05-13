# Tip: Import and use Insert function created in q2. (from q2 import *)
from q2 import *


def InsertAtStart(list, element):
    """
    Insert the given element at the beginning of the list, shifting existing elements to make room.

    Parameters:
    - list (list): The list to insert the element into.
    - element: The element to insert at the start of the list.

    Returns:
    str: A string indicating the result of the insertion.
         - "List is full" if the list is already full and no insertion is possible.
         - "Element inserted successfully" if the insertion is successful.
    """

    # WRITE YOUR CODE HERE
    return Insert(list,0,element)
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    lst = Initialize(2)
    print(InsertAtStart(lst, "a"))  # Should print: "Element inserted successfully"
    print(lst)  # Should print: ['a', None]
    print()

    print(InsertAtStart(lst, "b"))  # Should print: "Element inserted successfully"
    print(lst)  # Should print: ['b', 'a']
    print()

    print(InsertAtStart(lst, "c"))  # Should print: "List is full"
    print(lst)  # Should print: ['b', 'a']

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


# Testing For all testcases
# In order to test your function, type the following command on the terminal:
# pytest test_q4.py
