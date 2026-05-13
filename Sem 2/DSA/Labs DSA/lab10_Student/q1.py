from helper_functions import *
def create_graph():
    """Create an adjacency list representation of the graph.
    
    Returns
    -------
        The adjacency list representation of the graph.
    """

    # WRITE YOUR CODE HERE
    G={}
    addNodes(G,[1,2,3,4,5])
    addEdges(G, [(1, 2, 1), (1, 5, 1), (2, 1, 1), (2, 3, 1), (2, 4, 1), (2, 5, 1), (3, 2, 1), (3, 4, 1), (4, 2, 1), (4, 3, 1), (4, 5, 1), (5, 1, 1), (5, 2, 1), (5, 4, 1)])
    return G
    pass


def get_list_of_nodes(G):
    """Get the list of nodes in the graph.

    Parameters
    ----------
    G :
        The adjacency list representation of the graph.

    Returns
    -------
        The list of nodes in the graph
    """
    
    # WRITE YOUR CODE HERE
    return listOfNodes(G)
    pass


def get_list_of_edges(G):
    """Get the list of edges in the graph.

    Parameters
    ----------
    G :
        The adjacency list representation of the graph.

    Returns
    -------
    List[EdgeType]
        The list of edges in the graph
    """

    # WRITE YOUR CODE HERE
    return listOfEdges(G, directed=False)
    pass


def get_all_neighbours(G):
    """Get the list of neighbours of each node in the graph.

    Parameters
    ----------
    G :
        The adjacency list representation of the graph.

    Returns
    -------
        The list of neighbours of each node in the graph.
    """
    
    # WRITE YOUR CODE HERE
    lst={}
    nodes=get_list_of_nodes(G)
    for node in nodes:
        a=node
        lst[a]=getNeighbours(G,a)
    return lst




#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    G = create_graph()

    print("GRAPH")
    displayGraph(G)
    '''
    SHOULD PRINT:
    {1: [(2, 1), (5, 1)], 2: [(1, 1), (3, 1), (4, 1), (5, 1)], 3: [(2, 1), (4, 1)], 
     4: [(2, 1), (3, 1), (5, 1)], 5: [(1, 1), (2, 1), (4, 1)]}
    '''
    
    print()

    print("LIST OF NODES")
    print(listOfNodes(G))
    '''
    SHOULD PRINT:
    [1, 2, 3, 4, 5]
    '''

    print()

    print("LIST OF EDGES")
    print(listOfEdges(G))
    '''
    SHOULD PRINT:
    [(1, 2, 1), (1, 5, 1), (2, 3, 1), (2, 4, 1), (2, 5, 1), (3, 4, 1), (4, 5, 1)]
    '''

    print()

    print("NEIGHBOURS FOR EACH NODE IN A GRAPH")
    print(get_all_neighbours(G))
    '''
    SHOULD PRINT:
    {1: [2, 5], 2: [1, 3, 4, 5], 3: [2, 4], 4: [2, 3, 5], 5: [1, 2, 4]}
    '''

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q1.py