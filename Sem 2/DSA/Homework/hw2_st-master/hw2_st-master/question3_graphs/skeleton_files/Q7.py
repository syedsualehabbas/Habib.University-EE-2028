from Q6 import *
def add_warehouse(graph, warehouse_o, tr_trust, warehouse_i, weight):
    """
    Adds a new warehouse to the supply chain graph, having one new link with an existing warehouse.

    If the warehouse already exists in the graph, it prints an error message.
    If the destination warehouse, i.e., warehouse_i does not exist, the new warehouse cannot be added, so it 
    prints an error message accordingly.
    Otherwise, it creates a new entry for the warehouse with the given transit trust percentage 
    and an initial connection to another warehouse, and prints a success message, as shown in the example below.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    warehouse_o (str): The alphanumeric warehouse ID of the new warehouse to be added.
    tr_trust (float): The transit trust percentage of the new warehouse.
    warehouse_i (str): The alphanumeric warehouse ID of the connecting warehouse to the new one.
    weight (tuple): A tuple (Shipment Time, Shipment Cost, Shipping Method) representing the weight of the edge.

    Returns:
    None

    Example:
    >>> add_warehouse(G, "W21", 100.0, "W1", (3, 129.96, "Ground"))
    (Creates a new warehouse with one connection, if it does not exist, and prints the message)
    The warehouse was added successfully

    >>> add_warehouse(G, "W11", 100.00, "W1", (4, 99.96, "Air"))
    (Does not modify the graph, and prints an error message)
    The warehouse already exists

    >>> add_warehouse(G, "W24", 100.00, "W25", (4, 99.96, "Sea"))
    (Does not modify the graph, and prints an error message)
    The destination warehouse does not exist
    """

# WRITE YOUR CODE HERE
    if warehouse_o in list_of_vertices(graph):
        print("The warehouse already exists")
        return
    if warehouse_i not in list_of_vertices(graph):
        print("The destination warehouse does not exist")
        return
    addVertices(graph,[(warehouse_o,tr_trust)])
    addEdges(graph, [(warehouse_o,warehouse_i)+weight])
    print("The warehouse was added successfully")
    return
    
       
    


def main():
    G = create_supply_chain('supply_chain.csv')
    add_warehouse(G, "W21", 100.0, "W1", (3, 129.96, "Ground"))
    """
    Expected Output:
    The warehouse was added successfully
    """
   
    add_warehouse(G, "W11", 100.00, "W1", (4, 99.96, "Air"))
    """
    Expected Output:
    The warehouse already exists
    """
   
    add_warehouse(G, "W24", 100.00, "W25", (4, 99.96, "Sea"))
    """
    Expected Output:
    The destination warehouse does not exist
    """


if __name__ == "__main__":
    main()
