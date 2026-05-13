def finding_multiple(lst, item):
    """
    Finds all indices of an item in a sorted list using binary and linear search.
    
    Args:
    lst (list): Sorted list of items.
    item (any): Item to search for.
    
    Returns:
    list: Indices of the item, or an empty list if not found.
    """

    # WRITE YOUR CODE HERE
    index=[]
    low=0
    high=len(lst)-1
    while low<=high:
        mid=(low+high)//2
        if lst[mid]==item:
            for i in range(mid-1,low-1,-1):
                if lst[i]==item:
                    index.append(i)
                else:
                    break
            for j in range(mid, high+1):
                if lst[j]==item:
                    index.append(j)
                else:
                    break
            return index

        elif lst[mid]<item:
            low=mid+1
        elif lst[mid]>item:
            high= mid-1
    
    return []

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print(sorted(finding_multiple([0, 1, 2, 8, 13, 17, 17, 17, 17, 19, 32, 42], 17)))
    # Shoud print: [5, 6, 7, 8]

    print(sorted(finding_multiple([0, 1, 2, 8, 13, 17, 17, 17, 17, 19, 32, 42], 34)))
    # Should print: []
     
    print(sorted(finding_multiple([0, 1, 2, 8, 13, 17, 17, 17, 17, 19, 32, 42], 19)))
    # Should print: [9] 

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################
    # print(sorted(finding_multiple([0, 1, 2, 8, 13, 17, 17, 17, 17, 19, 32, 42], 19,)))


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q5.py