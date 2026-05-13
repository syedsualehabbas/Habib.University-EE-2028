# Tip: Import and use created helper function from q1 where applicable. (from q1 import *)
from q1 import *


def Insert(list, index, value):
    """
    Insert the given value at the specified index in the list, shifting existing elements to make room.

    Parameters:
    - list (list): The list to insert the value into.
    - index (int): The index at which to insert the value.
    - value: The value to insert into the list.

    Returns:
    str: A string indicating the result of the insertion.
        - "List is full" if the list is already full and no insertion is possible.
        - "Invalid Index" if the provided index is outside the valid range.
                * The valid index range is between 0 and NumberOfElements(list)
        - "Element inserted successfully" if the insertion is successful.
    """

    # WRITE YOUR CODE HERE
    
    if not IsFull(list):
        if index>NumberOfElements(list) or index<0:
            return "Invalid Index"
        for i in range(NumberOfElements(list),index,-1):
            list[i]=list[i-1]
        list[index]=value
        return "Element inserted successfully"

    return "List is full"

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    lst = Initialize(3)

    print(Insert(lst, 0, "a"))  # Should print: "Element inserted successfully"
    print(lst)  # Should print: ['a', None, None]
    print()

    print(Insert(lst, 2, "b"))  # Should print: "Invalid Index"
    print(lst)  # ['a', None, None]
    print()

    print(Insert(lst, 1, "b"))  # Should print: "Element inserted successfully"
    print(lst)  # ['a', 'b', None]
    print()

    print(Insert(lst, 4, "e"))  # Should print: "Invalid Index"
    print(lst)  # Shoud print: ['a', 'b', None]
    print()

    print(Insert(lst, 2, "c"))  # Should print: "Element inserted successfully"
    print(lst)  # Should print: ['a', 'b', 'c']
    print()

    print(Insert(lst, 3, "d"))  # Should print: "List is full"
    print(lst)  # Should print: ['a', 'b', 'c']
    print()

    #####################################################################

    lst = ["a", "b", None]
    print(Insert(lst, 1, "c"))  # Should print: "Element inserted successfully"
    print(lst)  # Should print: ['a', 'c', 'b']
    print()

    #####################################################################

    lst = ["a", "b", None]
    print(Insert(lst, 0, "c"))  # Should print: "Element inserted successfully"
    print(lst)  # Should print: ['c', 'a', 'b']
    print()

    #####################################################################

    lst = ["a", "c", None, None]
    print(Insert(lst, 0, "b"))  # Should print: "Element inserted successfully"
    print(lst)  # Should print: ['b', 'a', 'c', None]
    print()

    #####################################################################

    lst = ["a", None]
    print(Insert(lst, 0, "b"))  # Should print: "Element inserted successfully"
    print(lst)  # Should print: ['b', 'a']
    print()

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


# Testing For all testcases
# In order to test your function, type the following command on the terminal:
# pytest test_q2.py
