import csv
###########################################################################################
############################# PASTE YOUR LAB10 FUNCTIONS HERE #############################
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

##############################################################################################
############################# COMPLETE YOUR LAB11 FUNCTIONS HERE #############################


def in_out_degree(G):
    """In and out degree of a directed graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary

    Returns
    -------
        A dictionary containing the in and out degree of each node
    """

    # WRITE YOUR CODE HERE
    dict1={}
    for k in G.keys():
        a=0
        for i in G.keys():

            for j in range(len(G[i])):
                if G[i][j][0]==k:
                    a+=1


        dict1[k]=(a,len(G[k]))
    return dict1
    

    pass


def degree(G):
    """Degree of a directed graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary

    Returns
    -------
        A dictionary containing the degree of each node
    """

    # WRITE YOUR CODE HERE
    
    lst={}
    for i in G:
        lst[i]=len(G[i])
    return lst

    pass


def getInNeighbors(G, node):
    """In neighbors of a node in a directed graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node whose in neighbors

    Returns
    -------
        A list of in neighbors of the node
    """

    # WRITE YOUR CODE HERE
    lst=[]
    for i in G.keys():

        for j in range(len(G[i])):
            if G[i][j][0]==node:
                lst.append(i)
    return lst


def getOutNeighbors(G, node):
    """Out neighbors of a node in a directed graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node whose out neighbors

    Returns
    -------
        A list of out neighbors of the node
    """

    # WRITE YOUR CODE HERE
    lst=[]
    for i in G.keys():
        if i==node:
            for j in range(len(G[i])):
                lst.append(G[i][j][0])
    return lst


def isNeighbor(G, node1, node2):
    """Returns True if Node2 is a neighbor of Node1 in a directed graph G.

    Parameters
    ----------
    G : dict
        A directed graph as an adjacency list.
    Node1 : any
        The node to check outgoing edges from.
    Node2 : any
        The node to check as a neighbor of Node1.

    Returns
    -------
    bool
        True if there is an edge from Node1 to Node2, False otherwise.
    """

    # WRITE YOUR CODE HERE
    a=getNeighbours(G,node1)
    if node2 in a:
        return True
    return False


def initialize_matrix(rows, cols):
    """Initialize a matrix with -1

    Parameters
    ----------
    rows : int
        number of rows
    cols : int
        number of columns

    Returns
    -------
    list[list[int]]
        A matrix with -1
    """
    # WRITE YOUR CODE HERE
    return [[-1 for i in range(cols)] for j in range(rows)]
    pass


def adjlst_to_adj_matrix(G):
    """Convert adjacency list to adjacency matrix

    Parameters
    ----------
    G :
        A graph represented as a dictionary

    Returns
    -------
        An adjacency matrix of the graph
    """

    # WRITE YOUR CODE HERE
    dict1={key:i for i, key in enumerate(G)}
    a=initialize_matrix(len(G),len(G))
    b=0
    for k,v in G.items():
        for i in v:
            a[dict1[k]][dict1[i[0]]]=i[1]
    return a
        




    pass


def csv_to_adj_list(filename: str):
    """Convert CSV to adjacency list

    Parameters
    ----------
    filename : str
        The name of the CSV file

    Returns
    -------
        A graph represented as a dictionary
    """

    # WRITE YOUR CODE HERE
    with open('connections.csv') as csvfile:
        csv_reader = csv.reader(csvfile)
        lst=[]
        g={}
        for i in csv_reader:
            lst.append(i)
        
    nodes=lst[0]
    matrix=lst[1::]
    for i in matrix:
        a=[]
        for j in range(len(i)):
            if i[j]!="-1" and nodes[j]!=i[0] and j!=0:
                a.append((nodes[j],int(i[j])))
            g[i[0]]= a
    return g




            



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
# pytest tests/test_helper_functions.py