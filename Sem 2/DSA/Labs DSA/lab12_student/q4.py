from Helper_Functions import *

def nodes_of_level(G,level):
    """
    Returns a list of nodes on the given level in the graph G.

    Parameters
    ----------
    G : dict
        A directed graph represented as an adjacency list.
    level : int
        The level in the graph to find the nodes for.

    Returns
    -------
    list
        A list of nodes that are on the given level.
    """
    
    # WRITE YOUR CODE HERE
    lst=listOfNodes(G)
    s=lst[0]
    queue=Initialize(len(G))
    enQueue(queue,(s,0))
    visited=[]
    visited.append(s)
    out=[]

    while not is_empty(queue):
        a, count=deQueue(queue)
        if count==level:
            out.append(a)
        elif count<level:
            for i,j in G[a]:
                if i not in visited:
                    enQueue(queue,(i, count+1))
                    visited.append(i)

    return out


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

    print(sorted(nodes_of_level(G, 1)))     # SHOULD PRINT: [1, 2]

    print(sorted(nodes_of_level(G, 2)))     # SHOULD PRINT: [3, 4, 5, 6]

    print(sorted(nodes_of_level(G, 3)))     # SHOULD PRINT: [7]

    G = {
            'Dallas': [('Austin', 200), ('Denver', 780), ('Washington', 1300)],
            'Austin': [('Houston', 160), ('Chicago', 900)],
            'Washington': [('Atlanta', 600)],
            'Denver': [],
            'Atlanta': [],
            'Chicago': [],
            'Houston': []
        }
    
    print(sorted(nodes_of_level(G, 1)))     # SHOULD PRINT: ['Austin', 'Denver', 'Washington']

    print(sorted(nodes_of_level(G, 2)))     # SHOULD PRINT: ['Atlanta', 'Chicago', 'Houston']


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q4.py