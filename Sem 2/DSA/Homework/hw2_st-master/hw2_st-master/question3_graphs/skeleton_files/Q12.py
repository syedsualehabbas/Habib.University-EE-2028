from Q11 import *

def total_edges(graph):
    """
    HELPER FUNCTION to be used in graph_density function below.
    
    Computes the total number of edges in the supply chain graph.

    This function iterates through all vertices in the graph and sums up the 
    number of outbound connections to determine the total edge count.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency list.

    Returns:
    int: The total number of edges in the graph.
    """
    count=0
    for k in graph:
        count+=len(graph[k])
    return count
    

def total_vertices(graph):
    """
    HELPER FUNCTION to be used in graph_density function below.
    
    Computes the total number of vertices (warehouses) in the supply chain graph.

    This function simply returns the number of nodes (keys) in the graph.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency list.

    Returns:
    int: The total number of vertices in the graph.

    """
    return len(graph)

def graph_density(graph):
    """
    Calculates the graph density and categorizes the connectivity of the supply chain.

    Graph density (GD) is computed using the formula:
    - GD = E / (V * (V - 1)) for directed graphs
    - GD = 2E / (V * (V - 1)) for undirected graphs 
    
    Based on the density value, the function prints:
    - "Disconnected Graph" if GD == 0
    - "Fully Connected Graph" if GD == 1
    - "Relatively Sparse Graph" if GD < 0.5
    - "Relatively Dense Graph" if GD > 0.5

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.

    Returns:
    None: Prints the calculated graph density, and an appropriate message based on it. 
    """
    E=total_edges(graph)
    V=total_vertices(graph)
    GD=E/(V*(V-1))
    print(GD)
    if GD==0:
        print("Disconnected Graph")
    elif GD==1:
        print("Fully Connected Graph")
    elif GD<=0.5:
        print("Relatively Sparse Graph")
    elif GD>0.5:
        print("Relatively Dense Graph")


def main():
    G = create_supply_chain('supply_chain.csv')
    graph_density(G)

    """ Expected Output: 
    0.22105263157894736
    Relatively Sparse Graph
    """


if __name__ == "__main__":
    main()
