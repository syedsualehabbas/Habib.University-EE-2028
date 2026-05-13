# Tip: Import and use Remove function created in q3. (from q3 import *)
from q3 import *


def RemoveFromStart(list):
    """
    Remove the element at the beginning of the list, shifting subsequent elements to fill the gap.

    Parameters:
    - list (list): The list from which to remove an element.

    Returns:
    str: A string indicating the result of the removal.
         - "List is empty" if the list is empty, and no removal is possible.
         - "Element removed successfully" if the removal is successful.
    """

    # WRITE YOUR CODE HERE
    return Remove(list,0)


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    lst = Initialize(2)
    print(RemoveFromStart(lst))  # Should print: "List is empty"
    print(lst)  # Should print: [None, None]
    print()

    ######################################################

    lst = ["a", "b"]
    print(RemoveFromStart(lst))  # Should print: "Element removed successfully"
    print(lst)  # Should print: ["b", None]

    ######################################################

    lst = [10, 20, 40, 50, None]
    print(RemoveFromStart(lst))  # Should print: "Element removed successfully"
    print(lst)  # Should print: [20, 40, 50, None, None]

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


# Testing For all testcases
# In order to test your function, type the following command on the terminal:
# pytest test_q5.py
