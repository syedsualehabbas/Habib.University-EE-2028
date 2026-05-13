from Q8 import *


def remove_warehouse(graph, warehouse):
    """
    Removes a warehouses from the supply chain graph, along with its connected supply links.

    If the specified warehouse does not exist in the graph, the function prints an error message. 
    Otherwise, removes the warehouse passed as argument, and all its connections from the graph,
    and the function prints a success message, as specified in the example below.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    warehouse (str): The alphanumeric warehouse ID of the warehouse to be removed.
    
    Returns:
    None

    Example:
    >>> remove_warehouse(G, "W1")
    (W1 has three edges, which will be removed first using remove_supply_link function from 
    the previous question, which will print its success messages, followed by removal of the 
    warehouse W1 itself from the graph, and then prints its success message)
    Supply link removed successfully
    Supply link removed successfully
    Supply link removed successfully
    W1 is successfully removed from the supply chain

    >>> remove_warehouse(G, "W24")
    (Does not modify the graph, and prints a message)
    W24 is not in the supply chain
    """

     # WRITE YOUR CODE HERE
    if warehouse not in list_of_vertices(graph):
        print(f"{warehouse} is not in supply chain")
        return
    
    target = None
    for k in graph:
        if k[0]!=warehouse:
            for i in graph[k]:
                if i[0] == warehouse:
                    remove_supply_link(graph, k[0],i[0])
        if k[0]==warehouse: 
            target = k
    # print(graph)
    del graph[target]    
    print(f"{warehouse} is successfully removed from the supply chain")
    # print(graph)
                    

       
    


def main():
    G = create_supply_chain('supply_chain.csv')
    remove_warehouse(G, "W1")
    """
    Expected Output:
    Supply link removed successfully
    Supply link removed successfully
    Supply link removed successfully
    W1 is successfully removed from the supply chain
    """
     
    remove_warehouse(G, "W24")
    """
    Expected Output:
    W24 is not in the supply chain
    """

if __name__ == "__main__":
    main()
