import math

def addNodes(G, nodes) -> None:
    """Add nodes to the graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    nodes :
        A list of nodes to be added to the graph
    """

    # WRITE YOUR CODE HERE
    for i in nodes:
        G[i]=[]

        
    pass


def addEdges(G, edges, directed: bool = False) -> None:
    """Add edges to the graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    edges :
        A list of edges to be added to the graph
    directed : bool, optional
        A boolean value to determine if the graph is directed or not, by default False
    """

    # WRITE YOUR CODE HERE
    for i in edges:
        G[i[0]].append((i[1],i[2]))
        if directed==False:
            G[i[1]].append((i[0],i[2])) 
        



def listOfNodes(G):
    """Get the list of nodes in a graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary

    Returns
    -------
        A list of nodes in the graph
    """

    # WRITE YOUR CODE HERE
    lst=[]
    for k in G.keys():
        lst.append(k)
    return lst
    pass


def listOfEdges(G, directed: bool = False):
    """Get the list of edges in a graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    directed : bool, optional
        A boolean value to determine if the graph is directed or not, by default False

    Returns
    -------
        A list of edges in the graph
    """

    # WRITE YOUR CODE HERE
    lst=[]
    for k,v in G.items():
        for j in v:
            if (j[0],k,j[1]) not in lst:
                lst.append((k,j[0],j[1]))
            elif directed==True:
                lst.append((k,j[0],j[1]))

    return lst

    pass


def getNeighbours(G, node):
    """Get the neighbours of a node in a graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node whose neighbours are

    Returns
    -------
        A list of neighbours of the node
    """

    # WRITE YOUR CODE HERE
    lst=[]
    for k,v in G.items():
        if k==node:
            for i in range(len(v)):
                lst.append(v[i][0])

    return lst

    pass


def getNearestNeighbor(G, node):
    """Get the nearest neighbor of a node in a graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node whose nearest neighbor

    Returns
    -------
        The nearest neighbor of the node
    """

    # WRITE YOUR CODE HERE
    nearest=math.inf
    index=math.inf
    if G[node]==[]:
        return math.inf
    for i in G[node]:
        if i[1]<nearest:
            nearest=i[1]
            index=i

    return index[0]

    pass


def removeNode(G, node) -> None:
    """Remove a node from the graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node to be removed from the graph
    """

    # WRITE YOUR CODE HERE
    G.pop(node)
    for k in G.keys():
        for i in G[k]:
            if i[0]==node:
                G[k].remove(i)
        
    
    pass


def removeNodes(G, nodes) -> None:
    """Remove nodes from the graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    nodes :
        A list of nodes to be removed from the graph
    """

    # WRITE YOUR CODE HERE
    for node in nodes:
        G.pop(node)
        for k in G.keys():
            for i in G[k]:
                if i[0]==node:
                    G[k].remove(i)

    pass


def displayGraph(G) -> None:
    """Display the graph in a human-readable format

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    """

    # WRITE YOUR CODE HERE
    print(G)


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
# Visible Testcases are available in main_helper_functions.py               #
#############################################################################

if __name__ == "__main__":
    import main_helper_functions
    main_helper_functions.main()

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_helperfunctions.py