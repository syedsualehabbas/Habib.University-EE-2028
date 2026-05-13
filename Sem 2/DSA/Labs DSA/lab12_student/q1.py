from Helper_Functions import *

def DFS(G,s):
    """
    Performs DFS on graph G starting from node s.

    Parameters
    ----------
    G : dict
        A directed graph as an adjacency list.
    s : any
        The starting node for the DFS traversal.

    Returns
    -------
    list
        A list of nodes in the order they were visited.
    """

    # WRITE YOUR CODE HERE
    stack=Initialize(len(G))
    push(stack,s)
    visited=[]
    visited.append(s)
    while not is_empty(stack):
        a=pop(stack)
        if a not in visited:
            visited.append(a)
        for i in G[a]:
            if i[0] not in visited:
                push(stack,i[0])
    return visited


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    G = {
        0: [(1, 1), (2, 1)], 
        1: [(2, 1), (3, 1)], 
        2: [(4, 1)], 
        3: [(4, 1), (5, 1)], 
        4: [(5, 1)], 
        5: []
    }
    print(DFS(G, 0))
    # Should print: [0, 2, 4, 5, 1, 3]

    print(DFS(G, 1))
    # Should print: [1, 3, 5, 4, 2]

    G = {
            'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 
            'ORD': [('MIA', 1), ('DFW', 1)], 
            'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 
            'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 
            'MIA': [('DFW', 1), ('LAX', 1)], 
            'SFO': [('LAX', 1)], 
            'LAX': [('ORD', 1)] 
    }
    print(DFS(G, "BOS"))
    # SHOULD PRINT: ['BOS', 'SFO', 'LAX', 'ORD', 'DFW', 'MIA', 'JFK']

    print(DFS(G, "MIA")) 
    # SHOULD PRINT: ['MIA', 'LAX', 'ORD', 'DFW', 'SFO']

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q1.py