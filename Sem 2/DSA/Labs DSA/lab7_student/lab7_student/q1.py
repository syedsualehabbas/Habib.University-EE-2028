def binary_search_iterative(lst,item):
    """
    Perform an iterative binary search on a sorted list.

    Args:
    lst (list): A sorted list to search in.
    item (comparable): The item to find.

    Returns:
    int: The index of the item if found, else -1.
    """

    # WRITE YOUR CODE HERE
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
    
    return -1


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print(binary_search_iterative([0, 1, 2, 8, 13, 17, 19, 32, 42], 8))
    # Should print: 3

    print(binary_search_iterative([0, 1, 2, 3, 8, 13, 17, 19, 32, 42], -1))
    # Should print: -1

    print(binary_search_iterative([0, 1, 2, 8, 13, 17, 19, 32, 42], 13))
    # Should print: 4
     
    print(binary_search_iterative([0, 1, 2, 5, 8, 13, 15, 17, 19, 20, 32, 42], 14))
    # Should print: -1
     
    print(binary_search_iterative([0, 1, 2, 8, 13, 17, 19, 32, 42], 0))
    # Should print: 0
     
    print(binary_search_iterative([0, 1, 2, 8, 13, 17, 19, 32, 42], 2))
    # Should print: 2
     
    print(binary_search_iterative([0, 1, 2, 8, 13, 17, 19, 32, 42], 1))
    # Should print: 1

    print(binary_search_iterative([0, 1, 2, 8, 13, 17, 19, 32, 42], 17))
    # Should print: 5

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q1.py