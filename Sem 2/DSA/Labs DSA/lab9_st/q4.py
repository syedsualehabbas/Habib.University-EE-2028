from q3 import *

def delete(hashtable, key, size):
    """
    Deletes a key from the hash table using linear probing for collisions.

    Parameters:
    hash_table (list): The hash table.
    key (int or str): The key to delete.
    size (int): The table size.

    Returns:
    None: The table is modified in place. If the key is not found, no action is taken.
    """

    # WRITE YOUR CODE HERE
    hashvalue=hash_function(key,size)
    if hashtable[0][hashvalue]==key:
        hashtable[0][hashvalue]="#"
        hashtable[1][hashvalue]="#"
    else:
        newhash=hashvalue
        i=1
        while hashtable[0][newhash]!=key:
            newhash=collision_resolver(key,size,i)
            i+=1
            if newhash==hashvalue:
                break
        if hashtable[0][newhash]==key:
            hashtable[0][newhash]="#"
            hashtable[1][newhash]="#"


    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    ##################################################################

    H = create_hashtable(10)
    put(H, 5, 3, 10)
    print(H)
    ''' Should print:
    ([None, None, None, None, None, 5, None, None, None, None], 
     [None, None, None, None, None, 3, None, None, None, None])
    '''

    delete(H, 3, 10)
    print(H)
    ''' Should print:
    ([None, None, None, None, None, 5, None, None, None, None], 
     [None, None, None, None, None, 3, None, None, None, None])
    '''
        
    delete(H,5,10)
    print(H)
    ''' Should print:
    ([None, None, None, None, None, '#', None, None, None, None], 
     [None, None, None, None, None, '#', None, None, None, None])
    '''

    delete(H, 5, 10)
    print(H)
    ''' Should print:
    ([None, None, None, None, None, '#', None, None, None, None], 
     [None, None, None, None, None, '#', None, None, None, None])
    '''
    print()

    ##################################################################    
    H = create_hashtable(5)
    put(H, "Hello", "World", 5)
    print(H)
    ''' Should print:
    (['Hello', None, None, None, None], 
     ['World', None, None, None, None])
    '''

    delete(H, "World", 5)
    print(H)
    ''' Should print:
    (['Hello', None, None, None, None], 
     ['World', None, None, None, None])
    '''

    delete(H, "Hello", 5)
    print(H)
    ''' Should print:
    (['#', None, None, None, None],
     ['#', None, None, None, None])
    '''

    delete(H, "Hello", 5)
    print(H)
    ''' Should print:
    (['#', None, None, None, None],
     ['#', None, None, None, None])
    '''
    print()

    ##################################################################    
    H = create_hashtable(10)
    put(H, "temp", "data", 10)
    put(H, 98, 1, 10)
    put(H, 532, 324, 10)
    
    print(H)
    ''' Should print:
    ([None, None, 532, None, None, None, None, None, 'temp', 98], 
     [None, None, 324, None, None, None, None, None, 'data', 1])    
    '''

    delete(H, "temp", 10)
    print(H)
    ''' Should print:
    ([None, None, 532, None, None, None, None, None, '#', 98], 
     [None, None, 324, None, None, None, None, None, '#', 1])    
    '''

    delete(H, 89, 10)
    print(H)
    ''' Should print:
    ([None, None, 532, None, None, None, None, None, '#', 98], 
     [None, None, 324, None, None, None, None, None, '#', 1])    
    '''

    delete(H, 98, 10)
    print(H)
    ''' Should print:
    ([None, None, 532, None, None, None, None, None, '#', '#'], 
     [None, None, 324, None, None, None, None, None, '#', '#'])    
    '''

    delete(H, 532, 10)
    print(H)
    ''' Should print:
    ([None, None, '#', None, None, None, None, None, '#', '#'], 
     [None, None, '#', None, None, None, None, None, '#', '#'])    
    '''

    delete(H, 98, 10)
    print(H)
    ''' Should print:
    ([None, None, '#', None, None, None, None, None, '#', '#'], 
     [None, None, '#', None, None, None, None, None, '#', '#'])    
    '''
    print()
    
    ##################################################################    

    H = create_hashtable(10)
    put(H, "hello", 10, 10)
    put(H, "world", 19, 10)
    
    print(H)
    ''' Should print:
    ([None, None, 'hello', 'world', None, None, None, None, None, None], 
     [None, None, 10, 19, None, None, None, None, None, None])    
    '''

    delete(H, 19, 10)
    print(H)
    ''' Should print:
    ([None, None, 'hello', 'world', None, None, None, None, None, None], 
     [None, None, 10, 19, None, None, None, None, None, None])    
    '''
    
    delete(H, "world", 10)
    print(H)
    ''' Should print:
    ([None, None, 'hello', '#', None, None, None, None, None, None], 
     [None, None, 10, '#', None, None, None, None, None, None])    
    '''

    delete(H, "world", 10)
    print(H)
    ''' Should print:
    ([None, None, 'hello', '#', None, None, None, None, None, None], 
     [None, None, 10, '#', None, None, None, None, None, None])    
    '''

    delete(H, "hello", 10)
    print(H)
    ''' Should print:
    ([None, None, '#', '#', None, None, None, None, None, None], 
     [None, None, '#', '#', None, None, None, None, None, None])    
    '''

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q4.py