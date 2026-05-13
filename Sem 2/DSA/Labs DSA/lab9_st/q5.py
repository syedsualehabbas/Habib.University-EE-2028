from q4 import *

def main(to_put,to_delete,to_get,size): # returns tuple(list,hash table)
    """
    Simulates a hash table with operations to put, delete, and get values.
    
    Parameters:
    table_size (int): The size of the hash table.
    to_put (list of tuples): List of key-value pairs to insert into the hash table.
    to_delete (list): List of keys to delete from the hash table.
    to_get (list): List of keys to retrieve values for.

    Returns:
    tuple: A tuple containing a list of values associated with keys in to_get
           and the final hash table after all operations.
    """

    # WRITE YOUR CODE HERE
    hashtable=create_hashtable(size)
    lst=[]
    for i in range(len(to_put)):
        put(hashtable, to_put[i][0], to_put[i][1],size)
    for i in range(len(to_delete)):
        delete(hashtable, to_delete[i],size)
    for i in range(len(to_get)):
        get(hashtable, to_get[i],size)
        lst.append(get(hashtable,to_get[i],size))
        
    return (lst,hashtable)

    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":

    ##############################################################
    size = 5
    to_put = [(1 ,2) ,(" key "," value ")]
    to_delete = [1]
    to_get = [" key "]
    print(main (to_put , to_delete , to_get , size))
    ''' Shoud print:
    (   
        [' value '], 
        ([None, '#', None, ' key ', None], 
         [None, '#', None, ' value ', None])
    )
    '''

    ##############################################################
    size = 10
    to_put = [("temp", "data"),(98, 1),(532, 324)]
    to_delete = [532]
    to_get = ["temp"]
    print(main (to_put , to_delete , to_get , size))
    ''' Shoud print:
    (
        ['data'], 
        ([None, None, '#', None, None, None, None, None, 'temp', 98], 
         [None, None, '#', None, None, None, None, None, 'data', 1])
    )    
    '''

    ##############################################################
    size = 10
    to_put = [("temp", "data"),(98, 1),(532, 324)]
    to_delete = [532, 98, 532]
    to_get = ["temp", 98]
    print(main (to_put , to_delete , to_get , size))
    ''' Shoud print:
    (   ['data', None], 
        ([None, None, '#', None, None, None, None, None, 'temp', '#'], 
        [None, None, '#', None, None, None, None, None, 'data', '#'])
    )
    '''

    ##############################################################
    size = 10
    to_put = [('hello', 10), ('world', 19)]
    to_delete = ['hello']
    to_get = ["hello"]
    print(main (to_put , to_delete , to_get , size))
    ''' Shoud print:
    (   
        [None], 
        ([None, None, '#', 'world', None, None, None, None, None, None], 
         [None, None, '#', 19, None, None, None, None, None, None])
    )
    '''

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q5.py