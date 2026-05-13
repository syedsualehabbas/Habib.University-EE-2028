from helper_functions import *

vertices=["Washington", "Austin", "Dallas","Denver", "Atlanta", "Chicago", "Houston"]
edges=[("Washington","Atlanta", 600), ("Austin", "Dallas", 200), ("Dallas","Austin", 200), ("Dallas","Chicago", 900), ("Dallas", "Denver", 780),("Austin", "Houston", 160),("Washington", "Dallas", 1300),("Denver", "Atlanta", 1400), ("Denver", "Chicago", 1000), ("Atlanta", "Washington", 600), ("Atlanta", "Houston", 800),("Chicago", "Denver", 1000),("Houston", "Atlanta", 800)]


def create_airport_graph():
    """Create an adjacency list representation of the airport graph.

    Returns
    -------
        The adjacency list representation of the airport graph
    """

    # WRITE YOUR CODE HERE
    G = {}
    for i in vertices:
        G[i]=[]
    for j in edges:
        G[j[0]].append(((j[1]),j[2]))
    return G

    
    pass


def max_inbound_outbound_airport(G) -> tuple[str, str]:
    """
    Finds the airport with the highest number of inbound and outbound flights.

    Args:
        G (dict): The adjacency list representation of the graph.

    Returns:
        tuple[str, str]: A tuple containing:
            - The airport with the maximum inbound flights.
            - The airport with the maximum outbound flights.
    """

    # WRITE YOUR CODE HERE
    total_in_out=in_out_degree(G)
    out_count=0
    in_count=0
    
    for k,v in total_in_out.items():
        if v[0]>in_count:
            in_max= k
            in_count=v[0]
        if v[1] >out_count:
            out_max= k
            out_count =v[1]
    return in_max, out_max
    pass


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
    {
        'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 
        'Austin': [('Dallas', 200), ('Houston', 160)], 
        'Washington': [('Dallas', 1300), ('Atlanta', 600)], 
        'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 
        'Atlanta': [('Washington', 600), ('Houston', 800)], 
        'Chicago': [('Denver', 1000)], 
        'Houston': [('Atlanta', 800)]
    }
    '''

    max_inbound, max_outbound = max_inbound_outbound_airport(G)
    print("MAXIMUM IN-BOUND:", max_inbound)     #   SHOULD PRINT: Atlanta

    print("MAXIMUM OUT-BOUND:", max_outbound)   #   SHOULD PRINT: Dallas


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q2.py