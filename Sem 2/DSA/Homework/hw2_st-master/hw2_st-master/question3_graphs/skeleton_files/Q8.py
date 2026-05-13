from Q7 import *


def remove_supply_link(graph, warehouse_o, warehouse_i):
    """
    Removes a supply link between two warehouses in the supply chain graph.

    If the specified origin or destination warehouse does not exist in the graph, 
    the function prints an error message. 
    If the origin is not linked with destination warehouse, this means there is no 
    connection to be removed, so print an appropriate error message (see examples below).
    Otherwise, it removes the direct connection from warehouse_o to warehouse_i, and 
    prints a success message, as shown in the example below.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    warehouse_o (str): The alphanumeric warehouse ID of the origin warehouse.
    warehouse_i (str): The alphanumeric warehouse ID of the destination warehouse.

    Returns:
    None

    Example:
    >>> remove_supply_link(graph, "W1", "W11")
    (Removes the direct connection from W1 to W11, and prints the message)
    Supply link removed successfully

    >>> remove_supply_link(G, "W1", "W5")
    (Does not modify the graph, and prints an error message)
    W5 is not linked to  W1

    >>> remove_supply_link(graph, "W24", "W1")
    (Does not modify the graph, and prints an error message)
    W24 is not in the supply chain
    """

     # WRITE YOUR CODE HERE
    if not search_warehouse(graph, warehouse_o):
        print(f"{warehouse_o} is not in the supply chain")
        return

    if not search_warehouse(graph, warehouse_i):
        print(f"{warehouse_i} is not in the supply chain")
        return
    if not is_connected(graph, warehouse_o, warehouse_i):
        print(f"{warehouse_i} is not linked to {warehouse_o}")
        return

    for i in graph:
        if i[0]==warehouse_o:
            for j in graph[i]:
                if j[0]==warehouse_i:
                    graph[i].pop(graph[i].index(j))
                    print("Supply link removed successfully")
            return


    pass

    

def main():
    G = create_supply_chain('supply_chain.csv')
    remove_supply_link(G, "W1", "W11")
    """
    Expected Output:
    Supply link removed successfully
    """
     
    remove_supply_link(G, "W1", "W5")
    """
    Expected Output:
    W5 is not linked to  W1
    """
     
    remove_supply_link(G, "W24", "W11")
    """
    Expected Output:
    W24 is not in the supply chain
    """
      
if __name__ == "__main__":
    main()
