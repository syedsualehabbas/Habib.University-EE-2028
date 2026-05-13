def last_name_first(t):
    """
    Reorders each tuple in `t` so the last name comes first.

    Parameters:
    t (list of tuples): List of name tuples.

    Returns:
    None: Modifies the list in place.
    """

    # WRITE YOUR CODE HERE
    for name in t:
        a=t.index(name)
        name=(name[-1],)+name[0:len(name)-1]
        t[a]=name



#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    t = [
        ('Ahmed', 'Dawood'), 
        ('Haroon', 'Hussain', 'Fawad', 'Rasheed'), 
        ('Muhammad', 'Faisal', 'Amin')
    ]
    last_name_first(t)
    print(t)
    # Should print: [
    #   ('Dawood', 'Ahmed'),
    #   ('Rasheed', 'Haroon', 'Hussain', 'Fawad'),
    #   ('Amin', 'Muhammad', 'Faisal')
    # ] 
        
    t = [
        ('Haroon', 'Hussain', 'Fawaz', 'Rasheed'),
        ('Ahmed', 'Dawood'),
        ('Haroon', 'Hussain', 'Fawad', 'Rasheed'),
        ('Aamir', 'Dawood'),
        ('Muhammad', 'Mohsin', 'Amin'),
        ('Muhammad', 'Faisal', 'Amin')
    ]

    last_name_first(t)
    print(t)
    # Should print: [
    #   ('Rasheed', 'Haroon', 'Hussain', 'Fawaz'),
    #   ('Dawood', 'Ahmed'), 
    #   ('Rasheed', 'Haroon', 'Hussain', 'Fawad'), 
    #   ('Dawood', 'Aamir'),
    #   ('Amin', 'Muhammad', 'Mohsin'),
    #   ('Amin', 'Muhammad', 'Faisal')
    # ]

    t = [
        ('Zara',), ('Lara',), ('Mara',), 
        ('Fara',), ('Sara',), ('Kara',), 
        ('Tara',), ('Hara',), ('Dara',)
    ]

    last_name_first(t)
    print(t)
    # Should print: [
    #   ('Zara',), ('Lara',), ('Mara',), 
    #   ('Fara',), ('Sara',), ('Kara',), 
    #   ('Tara',), ('Hara',), ('Dara',)
    # ]
    
    t = [('Bloody', 'Mary'), ('Bloody', 'Mary'), ('Bloody', 'Mary')]

    last_name_first(t)
    print(t)
    # Should print: [('Mary', 'Bloody'), ('Mary', 'Bloody'), ('Mary', 'Bloody')]

    t = [('Haroon', 'Hussain', 'Fawad', 'Rasheed')]
    last_name_first(t)
    print(t)
    # Should print: [('Rasheed', 'Haroon', 'Hussain', 'Fawad')]

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q1.py