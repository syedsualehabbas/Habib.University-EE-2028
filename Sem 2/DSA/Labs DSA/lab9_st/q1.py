def create_hashtable(size):
    """
    Creates a hash table with the given size, initialized with None values.

    Parameters:
    size (int): The number of slots in the hash table.

    Returns:
    tuple: A tuple containing two lists (keys and values), each of length 'size', initialized to None.
    """

    # WRITE YOUR CODE HERE
    return ([None]*size, [None]*size)
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print(create_hashtable(5))
    ''' Shoud print:
    ([None, None, None, None, None], [None, None, None, None, None])
    '''

    print(create_hashtable(15))
    ''' Should print: 
    ([None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])
    '''

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q1.py