from Q9 import *
from stack import *

def count_all_supply_chain_connections(graph, warehouse_o, warehouse_i):
    """
    Finds the count of all connections between the origin and the destination warehouses using DFS.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    warehouse_o (str): The alphanumeric warehouse ID of the origin vertex.
    warehouse_i (str): The alphanumeric warehouse ID of the destination vertex.

    Returns:
    int: The count of all paths connecting the two warehouses. 
    If there is no such warehouse in the graph, it returns None
    If both warehouse_o and warehouse_i refer to the same warehouse, then the count should be 0
    """
    # WRITE YOUR CODE HERE
    count=0
    if warehouse_i not in list_of_vertices(graph) or warehouse_o not in list_of_vertices(graph):
        return None
    if warehouse_o==warehouse_i:
        return count
    pass
    


def main():
    G = create_supply_chain('supply_chain.csv')
    print(count_all_supply_chain_connections(G, "W4", "W10"))
    """ Expected Output: 16148 """

    print(count_all_supply_chain_connections(G, "W1", "W11"))
    """ Expected Output: 74597 """
    
    print(count_all_supply_chain_connections(G, "W4", "W4"))
    """ Expected Output: 0 """
    
    print(count_all_supply_chain_connections(G, "W24", "W10"))
    """ Expected Output: None """


if __name__ == "__main__":
    main()
