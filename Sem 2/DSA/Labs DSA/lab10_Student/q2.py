from helper_functions import *


def create_airport_graph():
    """Create an adjacency list representation of the airport graph.

    Returns
    -------
        The adjacency list representation of the airport graph
    """

    # WRITE YOUR CODE HERE
    G = {}
    addNodes(G, ["Austin", "Atlanta", "Chicago", "Dallas", "Denver", "Houston", "Washington"])
    addEdges(G, [("Austin","Dallas",200),("Atlanta","Washington",600),("Atlanta","Houston",800),("Austin","Houston",160),("Chicago","Denver",1000),("Dallas","Austin",200),("Denver","Atlanta",1400),("Denver","Chicago",1000),("Dallas","Denver",780),("Dallas","Chicago",900),("Washington","Dallas",1300),("Washington","Atlanta",600),("Houston","Atlanta",800)],directed=True)
    return G


def one_way_connection(G):
    """Obtain the list of one-way connections in the graph.

    Parameters
    ----------
    G :
        The adjacency list representation of the graph.

    Returns
    -------
        The list of one-way connections in the graph.
    """

    # WRITE YOUR CODE HERE
    list_edges = listOfEdges(G, directed=True)
    edges_copy= list_edges[:]
    for i in edges_copy:
        if (i[1],i[0],i[2]) in edges_copy:
            if i in list_edges:
                list_edges.remove(i)
                list_edges.remove((i[1],i[0],i[2]))
    lst=[]
    for j in list_edges:
        lst.append((j[0],j[1]))
    return lst


def nearest_airport(G, A):
    """Find the nearest airport to a given airport.

    Parameters
    ----------
    G :
        The adjacency list representation of the graph.
    A :
        The airport for which the nearest airport is to be found.

    Returns
    -------
        The nearest airport to the given airport.
    """

    # WRITE YOUR CODE HERE
    return getNearestNeighbor(G, A)


def not_more_than_one_intermediate(G, node):
    """Find the airports connected to a given airport with not more than one
    intermediate airport.

    Parameters
    ----------
    G :
        The adjacency list representation of the graph.
    node :
        The airport for which the connected airports are to be found.

    Returns
    -------
        The airports connected to the given airport with not more than one intermediate
        airport.
    """

    # WRITE YOUR CODE HERE
    nodes = listOfNodes(G)
    lst=[]
    for i in nodes:
        a = getNeighbours(G ,i)
        if node in a and i != node:
            lst.append(i)
        for j in a:
            b = getNeighbours(G,j)
            if node in b and i != node:
                lst.append(i)
    return lst


def alien_attack(G):
    """Aliens have attacked, remove Washington, add a path from Atlanta to Dallas and
    return the updated graph.

    Parameters
    ----------
    G :
        The adjacency list representation of the graph.

    Returns
    -------
        The updated adjacency list representation of the graph.
    """

    # WRITE YOUR CODE HERE
    removeNode(G, "Washington")
    addEdges(G,[("Atlanta","Dallas",1700)])
    return G


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    print("GRAPH")
    G = create_airport_graph()
    displayGraph(G)
    '''
    SHOULD PRINT:
    {'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 'Austin': [('Dallas', 200), ('Houston', 160)], 
    'Washington': [('Dallas', 1300), ('Atlanta', 600)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 
    'Atlanta': [('Washington', 600), ('Houston', 800)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}
    '''

    print()
    print("ONE WAY CONNECTION")
    print(one_way_connection(G))
    '''
    SHOULD PRINT:
    [('Dallas', 'Denver'), ('Dallas', 'Chicago'), ('Austin', 'Houston'), ('Washington', 'Dallas'), ('Denver', 'Atlanta')]
    '''

    print()
    print("NEAREST AIRPORT")
    for i in listOfNodes(G):
        print(i,":", nearest_airport(G, i))
    '''
    SHOULD PRINT:
    Dallas : Austin
    Austin : Houston
    Washington : Atlanta
    Denver : Chicago
    Atlanta : Washington
    Chicago : Denver
    Houston : Atlanta
    '''

    print()
    print("CONNECTED WITH NOT MORE THAN ONE INTERMEDIATE AIRPORT")
    print("Dallas :", not_more_than_one_intermediate(G, "Dallas"))
    '''
    SHOULD PRINT:
    Dallas : ['Austin', 'Washington', 'Atlanta']
    '''

    print()
    print("REMOVING WASHINGTON, ADDING PATH FROM ATLANTA TO DALLAS AND DISPLAYING A GRAPH")
    removeNode(G, "Washington")
    addEdges(G,[("Atlanta","Dallas",1700)])
    displayGraph(G)
    '''
    SHOULD PRINT:
    {
        'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900), ('Atlanta', 1700)], 
        'Austin': [('Dallas', 200), ('Houston', 160)], 
        'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 
        'Atlanta': [('Houston', 800), ('Dallas', 1700)], 
        'Chicago': [('Denver', 1000)], 
        'Houston': [('Atlanta', 800)]
    }
    '''

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q2.py