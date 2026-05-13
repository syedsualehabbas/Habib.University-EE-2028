from q1 import create_hashtable
from q2 import hash_function, collision_resolver

def put(hashtable, key, data, size):
    """
    Inserts a key-value pair into the hash table. If the key already exists, 
    it updates the value. In case of a collision, it resolves the collision 
    using linear probing.

    Args:
        key (any): The key to insert into the table.
        value (any): The value associated with the key to insert.

    Returns:
        None: The table is modified in place. If the table is full, no action is taken.
    """

    # WRITE YOUR CODE HERE
    tombstone=[]
    hashvalue=hash_function(key, size)
    if hashtable[0][hashvalue]==None:
        hashtable[0][hashvalue]=key
        hashtable[1][hashvalue]=data
    else:
        if hashtable[0][hashvalue]==key:
            hashtable[1][hashvalue]=data
        else:
            newhash=hashvalue
            i=1
            while hashtable[0][newhash]!=None and hashtable[0][newhash]!=key:
                if hashtable[0][newhash]=="#":
                    tombstone.append(newhash)

                newhash=collision_resolver(key,size,i)
                i+=1
                if newhash==hashvalue:
                    break

            if hashtable[0][newhash]==None:
                if tombstone==[]:
                    hashtable[0][newhash]=key
                    hashtable[1][newhash]=data
                else:
                    hashtable[0][tombstone[0]]=key
                    hashtable[1][tombstone[0]]=data

            elif hashtable[0][newhash]==key:
                hashtable[1][newhash]=data
            elif tombstone!=[]:
                hashtable[0][tombstone[0]]=key
                hashtable[1][tombstone[0]]=data

                        




    

    pass


def get(hashtable, key, size):
    """
    Retrieves the value associated with a given key from the hash table.
    In case of collisions, it checks subsequent spots using linear probing.

    Args:
        key (any): The key whose value is to be retrieved.

    Returns:
        any: The value associated with the key, or None if the key is not found.
    """

    # # WRITE YOUR CODE HERE
    start=hash_function(key,size)
    pos=start
    i=1
    while hashtable[0][pos]!=None:
        if key==hashtable[0][pos]:
            return hashtable[1][pos]
        else:
            pos=collision_resolver(key,size,i)
            i+=1
            if pos==start:
                break
    return None
    # pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":

    ########################################################################################
    H = create_hashtable(10)
    put(H, 5, 3, 10)
    print(H)
    ''' Should print:
    ([None, None, None, None, None, 5, None, None, None, None], 
     [None, None, None, None, None, 3, None, None, None, None])
    '''
    print(get(H, 5, 10))    # Should print: 3
    print()
    
    ########################################################################################
    H = create_hashtable(10)
    put(H, "hello", 10, 10)
    put(H, "world", 19, 10)

    print(H)
    ''' Should print:
    ([None, None, 'hello', 'world', None, None, None, None, None, None], 
     [None, None, 10, 19, None, None, None, None, None, None])
    '''
    print(get(H, "hello", 10))        # Should print: 10
    print(get(H, "world", 10))        # Should print: 19
    print(get(H, "olleh", 10))        # Should print: None
    print(get(H, "ALPHA", 10))        # Should print: None
    print()

    ########################################################################################

    H = create_hashtable(10)
    put(H, 0, 1, 10)
    put(H, 1, 2, 10)
    put(H, 42, 5, 10)

    print(H)
    ''' Should print:
    ([0, 1, 42, None, None, None, None, None, None, None],
     [1, 2, 5, None, None, None, None, None, None, None])
    '''
    print(get(H, 0, 10))            # Should print: 1
    print(get(H, 1, 10))            # Should print: 2
    print(get(H, 42, 10))           # Should print: 5
    print(get(H, 10, 10))           # Should print: None
    print(get(H, 11, 10))           # Should print: None
    print()

    ########################################################################################

    H = create_hashtable(25)
    put(H, 2, 14, 25)
    put(H, 3, 12, 25)

    print(H)
    ''' Should print:
    ([None, None, 2, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 
     [None, None, 14, 12, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])
    '''

    print(get(H, 2, 25))             # Should print: 14
    print(get(H, 3, 25))             # Should print: 12
    print(get(H, 27, 25))            # Should print: None
    print(get(H, 28, 25))            # Should print: None
    print()

    ########################################################################################

    keys = ['cat', 'bat', 'rat', 'fat', 'hat', 'mat']
    H = create_hashtable(5)
    put(H, 'cat', 'c', 5)
    put(H, 'bat', 'b', 5)
    put(H, 'rat', 'r', 5)
    put(H, 'fat', 'f', 5)
    put(H, 'hat', 'h', 5)
    put(H, 'mat', 'm', 5)

    print(H)
    ''' Should print:
    (['fat', 'bat', 'cat', 'rat', 'hat'],
     ['f', 'b', 'c', 'r', 'h'])
    '''

    print(get(H, 'cat', 5))         # Should print: c
    print(get(H, 'bat', 5))         # Should print: b
    print(get(H, 'rat', 5))         # Should print: r
    print(get(H, 'fat', 5))         # Should print: f
    print(get(H, 'hat', 5))         # Should print: h
    print(get(H, 'mat', 5))         # Should print: None
    print(get(H, 'pat', 5))         # Should print: None

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q3.py