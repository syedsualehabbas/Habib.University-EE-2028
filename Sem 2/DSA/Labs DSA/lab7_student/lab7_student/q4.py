def binary_search_recursive_modified(lst, item, low, high):
    """
    Recursively searches for an item. Returns the index if found, 
    or inserts the item at the correct position and returns the new index.
    
    Args:
    lst (list): Sorted list.
    item (any): Item to search for or insert.
    low (int): Starting index of the search range.
    high (int): Ending index of the search range.

    Returns:
        int: Index of item (found or inserted).
    """

    # WRITE YOUR CODE HERE
    if low<=high:
        mid=(low+high)//2
        if lst[mid]==item:
            return mid
        elif lst[mid]<item:
            low=mid+1
            return binary_search_recursive_modified(lst, item, low, high)
        elif lst[mid]>item:
            high=mid-1
            return binary_search_recursive_modified(lst, item, low, high)
    else:
        lst.insert(low,item)
        return low
#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_recursive_modified(lst, 8, 0, 8))   # Should print: 3
    print(lst)                          # Should print: [0, 1, 2, 8, 13, 17, 19, 32, 42]

    lst = [0, 1, 2, 3, 8, 13, 17, 19, 32, 42]
    print(binary_search_recursive_modified(lst, -1, 0, 9))  # Should print: 0
    print(lst)                          # Should print: [-1, 0, 1, 2, 3, 8, 13, 17, 19, 32, 42]

    lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_recursive_modified(lst, 13, 0, 8))  # Should print: 4
    print(lst)                          # Should print: [0, 1, 2, 8, 13, 17, 19, 32, 42]

    lst = [0, 1, 2, 5, 8, 13, 15, 17, 19, 20, 32, 42]
    print(binary_search_recursive_modified(lst, 14, 0, 11)) # Should print: 6
    print(lst)                          # Should print: [0, 1, 2, 5, 8, 13, 14, 15, 17, 19, 20, 32, 42]

    lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_recursive_modified(lst, 0, 0, 8))   # Should print: 0
    print(lst)                          # Should print: [0, 1, 2, 8, 13, 17, 19, 32, 42]

    lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_recursive_modified(lst, 2, 0, 8))   # Should print: 2
    print(lst)                          # Should print: [0, 1, 2, 8, 13, 17, 19, 32, 42]

    lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_recursive_modified(lst, 1, 0, 8))   # Should print: 1
    print(lst)                          # Should print: [0, 1, 2, 8, 13, 17, 19, 32, 42]
    
    lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_recursive_modified(lst, 17, 0, 8))  # Should print: 5
    print(lst)                          # Should print: [0, 1, 2, 8, 13, 17, 19, 32, 42]

    lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_recursive_modified(lst, 19, 0, 8))  # Should print: 6
    print(lst)                          # Should print: [0, 1, 2, 8, 13, 17, 19, 32, 42]

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q4.py