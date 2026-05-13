from Helper_Functions import *

def check_cycles(G,lst):
    '''
    Returns True if the list of nodes forms a directed cycle in G.

    Parameters
    ----------
    G : dict
        Directed graph as an adjacency list.
    lst : list
        List of nodes to check for a cycle.

    Returns
    -------
    bool
        True if lst forms a directed cycle, False otherwise."
    '''

    # WRITE YOUR CODE HERE
    stack=Initialize(len(lst)-1)
    for i in range(len(lst)-1,-1,-1):
        if lst[i] not in G:
            return False
        if lst[i]!=0:
            push(stack,lst[i])
    a=lst[0]
    while not is_empty(stack):
        b=0
        for i in G[a]:
            if top(stack)==i[0]:
                b+=1
                break    
        if b==0:
            return False
        a=pop(stack)
    b=0
    for i in G[a]:
        if lst[0]==i[0]:
            b+=1
            break
    if b==0:
        return False
        
    return True
            


                    


    pass


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    G = {
            'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 
            'Austin': [('Dallas', 200), ('Houston', 160)], 
            'Washington': [('Dallas', 1300), ('Atlanta', 600)], 
            'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 
            'Atlanta': [('Washington', 600), ('Houston', 800)], 
            'Chicago': [('Denver', 1000)], 
            'Houston': [('Atlanta', 800)]
        }
    
    print(check_cycles(G, ['Dallas','Denver','Atlanta','Washington']))  # SHOULD PRINT:     True


    G = {
            'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 
            'ORD': [('MIA', 1), ('DFW', 1)], 
            'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 
            'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 
            'MIA': [('DFW', 1), ('LAX', 1)], 
            'SFO': [('LAX', 1)], 'LAX': [('ORD', 1)] 
        }
    print(check_cycles(G, ['BOS', 'MIA', 'JFK']))   # SHOULD PRINT :    False
    print(check_cycles(G, ['JFK','MIA','DFW']))     # SHOULD PRINT :    False


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q2.py