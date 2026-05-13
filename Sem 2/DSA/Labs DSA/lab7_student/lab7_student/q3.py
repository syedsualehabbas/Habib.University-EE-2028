def binary_search_recursive(lst, item, low, high):
    """
        Performs a recursive binary search to find an item's index in a sorted list.
        
        Args:
        lst (list): Sorted list to search in.
        item (any): Item to search for.
        low (int): Starting index of the search range.
        high (int): Ending index of the search range.
        
        Returns:
        int: Index of the item if found, otherwise -1.
    """

    # WRITE YOUR CODE HERE
    if low<=high:
        mid=(low+high)//2
        if lst[mid]==item:
            return mid
        elif lst[mid]<item:
            low=mid+1
            return binary_search_recursive(lst, item, low, high)
        elif lst[mid]>item:
            high= mid-1
            return binary_search_recursive(lst,item, low, high)
    else:
        return -1
    

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print(binary_search_recursive([0, 1, 2, 8, 13, 17, 19, 32, 42], 8, 0, 8))
    # Should print: 3
     
    print(binary_search_recursive([0, 1, 2, 3, 8, 13, 17, 19, 32, 42], -1, 0, 9))
    # Should print: -1
    
    print(binary_search_recursive([0, 1, 2, 8, 13, 17, 19, 32, 42], 13, 0, 8))
    # Should print: 4
     
    print(binary_search_recursive([0, 1, 2, 5, 8, 13, 15, 17, 19, 20, 32, 42], 14, 0, 11))
    # Should print: -1
     
    print(binary_search_recursive([0, 1, 2, 8, 13, 17, 19, 32, 42], 0, 0, 8))
    # Should print: 0
     
    print(binary_search_recursive([0, 1, 2, 8, 13, 17, 19, 32, 42], 2, 0, 8))
    # Should print: 2

    print(binary_search_recursive([0, 1, 2, 8, 13, 17, 19, 32, 42], 1, 0, 8))
    # Should print: 1
     
    print(binary_search_recursive([0, 1, 2, 8, 13, 17, 19, 32, 42], 17, 0, 8))
    # Should print: 5
     
    print(binary_search_recursive([0, 1, 2, 8, 13, 17, 19, 32, 42], 19, 0, 8))
    # Should print: 6 

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q3.py