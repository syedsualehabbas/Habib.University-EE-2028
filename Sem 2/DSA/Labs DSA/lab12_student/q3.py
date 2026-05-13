from Helper_Functions import *

def BFS(G,root):
    """
    Performs BFS on graph G starting from node s.

    Parameters
    ----------
    G : dict
        A directed graph represented as an adjacency list.
    s : node
        The starting node for BFS.

    Returns
    -------
    list
        A list of nodes in the order they were visited.
    """

    # WRITE YOUR CODE HERE
    queue=Initialize(len(G))
    enQueue(queue,root)
    visited=[]
    visited.append(root)
    while not is_empty(queue):
        x=deQueue(queue)
        for i in G[x]:
            if i[0] not in visited:
                enQueue(queue,i[0])
                visited.append(i[0])

    return visited

    pass


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    G = {
            's': [(1, 1), (2, 1)], 
            1: [(3, 1), (4, 1), (5, 1)],
            2: [(6, 1)],
            3: [],
            4: [],
            5: [],
            6: [(7, 1)],
            7: []
        }
    print(BFS(G, 's'))    # SHOULD PRINT:     ['s', 1, 2, 3, 4, 5, 6, 7]

    G = {
            'BOS': [('JFK', 1), ('MIA', 1), ('SFO', 1)], 
            'ORD': [('MIA', 1), ('DFW', 1)], 
            'JFK': [('BOS', 1), ('SFO', 1), ('MIA', 1), ('DFW', 1)], 
            'DFW': [('ORD', 1), ('SFO', 1), ('LAX', 1)], 
            'MIA': [('DFW', 1), ('LAX', 1)], 
            'SFO': [('LAX', 1)], 
            'LAX': [('ORD', 1)] 
        }
    print(BFS(G, 'BOS'))    # SHOULD PRINT:   ['BOS', 'JFK', 'MIA', 'SFO', 'DFW', 'LAX', 'ORD']  
    print(BFS(G, 'MIA'))    # SHOULD PRINT:   ['MIA', 'DFW', 'LAX', 'ORD', 'SFO']
    print(BFS(G, 'JFK'))    # SHOULD PRINT:   ['JFK', 'BOS', 'SFO', 'MIA', 'DFW', 'LAX', 'ORD']


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q3.py