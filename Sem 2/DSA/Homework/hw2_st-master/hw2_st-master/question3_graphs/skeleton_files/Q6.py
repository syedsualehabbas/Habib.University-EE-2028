from Q4 import *

def search_warehouse(graph, wh):
    """
    Checks if a warehouse exists in the supply chain graph.

    This function iterates through the graph to determine if a warehouse with the given ID exists.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID to search for.

    Returns:
    bool: True if the warehouse exists in the graph, False otherwise.
    """

    # WRITE YOUR CODE HERE
    if wh in list_of_vertices(graph):
        return True
    return False

def add_supply_link(graph, warehouse_o, warehouse_i, weight):
    """
    Adds or updates a supply link between two warehouses in the supply chain graph.

    If both warehouses exist, the function adds a direct connection between them with the given weight.
    If a connection already exists, it updates the weight of the connection, and prints an appropriate message,
    as shown in the examples below.
    If either warehouse does not exist in the graph, it prints an error message and does not modify the graph.
    If the connection is added successfully, it updates the graph and prints a success message, as shown in 
    the examples below.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    warehouse_o (str): The alphanumeric warehouse ID of the origin warehouse.
    warehouse_i (str): The alphanumeric warehouse ID of the destination warehouse.
    weight (tuple): A tuple (Shipment Time, Shipment Cost, Shipping Method) representing the weight of the edge.

    Returns:
    None

    Example:
    >>> add_supply_link(graph, "W1", "W5", (2, 50, "Ground"))
    (Creates a new connection if it does not exist, and prints the message)
    Supply link added successfully

    >>> add_supply_link(graph, "W1", "W11", (3, 40, "Sea"))
    (Updates the existing connection between W1 and W11, and prints the message)
    Supply link updated successfully

    >>> add_supply_link(graph, "W24", "W11", (4, 60, "Land"))
    (Does not modify the graph, and prints an error message)
    W24 is not in the supply chain
    """

    # WRITE YOUR CODE HERE
    if warehouse_i not in list_of_vertices(graph):
        print(f"{warehouse_i} is not in the supply chain")
    if warehouse_o not in list_of_vertices(graph):
        print(f"{warehouse_o} is not in the supply chain")  
    for k in graph:
        if k[0]==warehouse_o:
            if is_connected(graph,warehouse_o, warehouse_i):
                for i in range(len(graph[k])):
                    if graph[k][i][0]==warehouse_i:
                        b=list(graph[k][i])
                        b[1]=weight
                    graph[k][i]=b
                    print("Supply link updated successfully")
                    break
                    

            else:
                graph[k].append((warehouse_i,weight))
                print("supply link added successfully")


    
    pass
    

def main():
    G = create_supply_chain('supply_chain.csv')
    add_supply_link(G, "W1", "W5", (2, 50, "Ground"))
    """
    Expected Output:
    Supply link added successfully
    """
    
    add_supply_link(G, "W1", "W11", (3, 40, "Sea"))
    """
    Expected Output:
    Supply link updated successfully
    """
    
    add_supply_link(G, "W24", "W11", (3, 33.33, "Air"))
    """
    Expected Output:
    W24 is not in the supply chain
    """
    
if __name__ == "__main__":
    main()
