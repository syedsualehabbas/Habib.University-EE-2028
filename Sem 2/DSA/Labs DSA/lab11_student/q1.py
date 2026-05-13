from helper_functions import *
vertices=[1,2,3,4]
edges=[(1,2),(2,4),(3,1),(3,2),(4,3),(4,4)]
def create_directed_graph():
    """
    Creates a directed graph using an adjacency list representation.

    Returns:
        dict: A dictionary representing the adjacency list of the directed graph.
    """

    # WRITE YOUR CODE HERE
    G = {}
    for node in vertices:
        G[node] = []
    for i in edges:
        G[i[0]].append(((i[1]),1))
    return G

    


def print_graph(G):
    """
    Prints the adjacency list representation of the directed graph.

    Args:
        G (dict): The adjacency list representation of the graph.

    Returns:
        None
    """
    
    # WRITE YOUR CODE HERE
    print(G)
    pass


def in_neighbors(G):
    """
    Computes the in-neighbors of each node.

    Args:
        G (dict): The adjacency list representation of the graph.

    Returns:
        dict: A dictionary where keys are nodes and values are lists of in-neighbors.
    """
    
    # WRITE YOUR CODE HERE
    dict1={}
    for i in vertices:
        dict1[i]=getInNeighbors(G,i)
    return dict1



def out_neighbors(G):
    """
    Computes the out-neighbors of each node.

    Args:
        G (dict): The adjacency list representation of the graph.

    Returns:
        dict: A dictionary where keys are nodes and values are lists of out-neighbors.
    """

    # WRITE YOUR CODE HERE
    dict1={}
    for i in vertices:
        dict1[i]=getOutNeighbors(G,i)
    return dict1


def generate_adjacency_matrix(G):
    """
    Generates and returns the adjacency matrix representation of the graph.

    Args:
        G (dict): The adjacency list representation of the graph.

    Returns:
        list: A 2D list representing the adjacency matrix of the graph.
    """
    
    # WRITE YOUR CODE HERE
    return adjlst_to_adj_matrix(G)


def check_degree_sums(G):
    """
    Checks whether the sum of in-degrees, the sum of out-degrees, 
    and the total number of edges in the graph are equal.

    Args:
        G (dict): The adjacency list representation of the graph.

    Returns:
        bool: True if sum of in-degrees == sum of out-degrees == total number of edges, otherwise False.
    """
    
    # WRITE YOUR CODE HERE
    a =out_neighbors(G)
    b=0 
    for i in a.values():
        for j in i:
            b+=1
    
    c=in_neighbors(G)
    d=0 
    for k in c.values():
        for l in k:
            d+=1

    return d==b
    pass


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    print("GRAPH")
    G = create_directed_graph()

    print_graph(G)
    '''
    SHOULD PRINT:
    {1: [(2, 1)], 2: [(4, 1)], 3: [(1, 1), (2, 1)], 4: [(3, 1), (4, 1)]}
    '''

    print("IN NEIGHBORS")
    print(in_neighbors(G))
    '''
    SHOULD PRINT:
    { 1: [3], 2: [1, 3], 3: [4], 4: [2, 4] }
    '''
    
    print("OUT NEIGHBORS")
    print(out_neighbors(G))
    '''
    SHOULD PRINT:
    { 1: [2], 2: [4], 3: [1, 2], 4: [3, 4] }
    '''

    print("ADJACENCY MATRIX")
    print(generate_adjacency_matrix(G))
    '''
    SHOULD PRINT:
    [[-1, 1, -1, -1], [-1, -1, -1, 1], [1, 1, -1, -1], [-1, -1, 1, 1]]
    '''

    print("Sum of the in-degrees of all nodes, "
    "the sum of the out-degrees of all nodes "
    "and the total number of edges are all equal: ")
    
    print(check_degree_sums(G))
    '''
    SHOULD PRINT:
    True
    '''

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q1.py