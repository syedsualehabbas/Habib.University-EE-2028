def binary_search_iterative_modified(lst,item):
    """
    Search for 'item' in a sorted list 'lst'.
    Return its index if found; otherwise, insert and return the index.

    Args:
        lst (list): Sorted list.
        item (int): Item to search for.

    Returns:
        int: Index of 'item' (found or inserted).

    """
    left=0
    right=len(lst)-1
    while left<=right:
        mid=(left+right)//2
        if lst[mid]==item:
            return mid
        elif lst[mid]<item:
            left=mid+1
        elif lst[mid]>item:
            right=mid-1
        else:
            right=mid-1
    lst.insert(left,item)
    return left






    pass

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_iterative_modified(lst, 8))     # Should print: 3
    print(lst)                          # Should print: [0, 1, 2, 8, 13, 17, 19, 32, 42]

    lst = [0, 1, 2, 3, 8, 13, 17, 19, 32, 42]
    print(binary_search_iterative_modified(lst, -1))    # Should print: 0
    print(lst)                          # Should print: [-1, 0, 1, 2, 3, 8, 13, 17, 19, 32, 42]

    lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_iterative_modified(lst, 13))    # Should print: 4
    print(lst)                          # Should print: [0, 1, 2, 8, 13, 17, 19, 32, 42]

    lst = [0, 1, 2, 5, 8, 13, 15, 17, 19, 20, 32, 42]
    print(binary_search_iterative_modified(lst, 14))    # Should print: 6
    print(lst)                          # Should print: [0, 1, 2, 5, 8, 13, 14, 15, 17, 19, 20, 32, 42]

    lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_iterative_modified(lst, 0))     # Should print: 0
    print(lst)                          # Should print: [0, 1, 2, 8, 13, 17, 19, 32, 42]

    lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_iterative_modified(lst, 2))     # Should print: 2
    print(lst)                          # Should print: [0, 1, 2, 8, 13, 17, 19, 32, 42]

    lst =  [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_iterative_modified(lst, 1))     # Should print: 1
    print(lst)                          # Should print: [0, 1, 2, 8, 13, 17, 19, 32, 42]

    lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search_iterative_modified(lst, 17))    # Should print: 5
    print(lst)                          # Should print: [0, 1, 2, 8, 13, 17, 19, 32, 42]

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q2.py