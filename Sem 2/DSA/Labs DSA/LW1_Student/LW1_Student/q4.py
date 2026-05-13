def remove_user(users_data, user_name):
    """
    Removes a user and their connections from users data.

    Parameters:
    users_data (dict): Dictionary of users with (phone_number, friends_list).
    username (str): The user to remove.

    Returns:
    None: Updated users_data in place.
    """

    # WRITE YOUR CODE HERE

    for k,v in users_data.items():
        if k==user_name:
            users_data.pop(k)
            break
    for k,v in users_data.items():
        for i in v:
            if type(i)==list:
                for name in i:
                    if name==user_name:
                        i.remove(name)

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    users_data = {
        'Alice': ('123-456-7890', ['Bob', 'Charlie']),
        'Bob': ('987-654-3210', ['Alice', 'David']),
        'Charlie': ('111-222-3333', ['Alice']),
        'David': ('555-666-7777', ['Bob'])
        }
    user_name = 'Alice'
    remove_user(users_data, user_name)
    print(users_data)
    # Should print: {
    #   'Bob': ('987-654-3210', ['David']),
    #   'Charlie': ('111-222-3333', []),
    #   'David': ('555-666-7777', ['Bob'])
    #   }
    
    users_data = {
        'Alice': ('123-456-7890', []), 
        'Bob': ('987-654-3210', ['Alice']), 
        'Charlie': ('111-222-3333', ['Alice']), 
        'David': ('555-666-7777', ['Bob'])
        }
    user_name = 'Alice'
    remove_user(users_data, user_name)
    print(users_data)
    # Should print: {
    #   'Bob': ('987-654-3210', []),
    #   'Charlie': ('111-222-3333', []),
    #   'David': ('555-666-7777', ['Bob'])
    #   }

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q4.py