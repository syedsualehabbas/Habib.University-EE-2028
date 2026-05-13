from Q12 import *

def find_best_warehouse(graph):
    """
    Identifies the best-performing warehouse based on the highest transit trust factor.

    This function iterates through the graph and finds the warehouse with the 
    maximum transit trust value.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency list, 
                  where each key is a warehouse and its value includes the transit trust factor.

    Returns:
    tuple: The warehouse with the highest transit trust factor. If the graph is empty, returns -1."
    """
    trust=-math.inf
    for k in graph:
        if k[1]>trust:
            trust=k[1]
    for k in graph:
        if k[1]==trust:
            return k
    return -1


def find_worst_warehouse(graph):
    """
    Identifies the worst-performing warehouse based on the lowest transit trust factor.

    This function iterates through the graph and finds the warehouse with the 
    minimum transit trust value.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency list, 
                  where each key is a warehouse and its value includes the transit trust factor.

    Returns:
    tuple: The warehouse with the lowest transit trust factor. If the graph is empty, returns -1.

    """
    trust=math.inf
    for k in graph:
        if k[1]<trust:
            trust=k[1]
    for k in graph:
        if k[1]==trust:
            return k
    return -1

def main():
    G = create_supply_chain('supply_chain.csv')
    print(find_best_warehouse(G))
    """
    Expected Output: ('W10', 94.39)
    """
    
    print(find_worst_warehouse(G))
    """ 
    Expected Output: ('W11', 70.81)
    """

if __name__ == "__main__":
    main()
