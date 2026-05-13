from Q4 import *

def get_cheapest_outgoing_supply_route(graph, wh):
    """
    Finds the cheapest outgoing supply route from a given warehouse.

    This function searches for all outgoing connections from the given warehouse
    and determines the route with the lowest shipment cost.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID of the origin warehouse.

    Returns:
    tuple: A tuple containing (origin warehouse, destination warehouse) 
           representing the cheapest outgoing supply route.
    None: If the warehouse has no outgoing supply routes or does not exist in the graph.
    """

    # WRITE YOUR CODE HERE
    time=(math.inf)
    lst=[wh]
    for k,v in graph.items():
        if k[0]==wh:
            for i in v:
                if i[1][1]<time:
                    time=i[1][1]
            for i in v:
                if time==i[1][1]:
                    lst.append(i[0])
    if len(lst)>1:
        return tuple(lst)
    return None
    
            
def get_cheapest_incoming_supply_route(graph, wh):
    """
    Finds the cheapest incoming supply route for a given warehouse.

    This function searches for all incoming connections to the given warehouse
    and determines the route with the lowest shipment cost.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID of the destination warehouse.

    Returns:
    tuple: A tuple containing (origin warehouse, destination warehouse) 
           representing the cheapest incoming supply route.
    None: If the warehouse has no incoming supply routes or does not exist in the graph.
    """

    # WRITE YOUR CODE HERE
    value=math.inf
    time=None
    for k,v in graph.items():
        for i in v:
            if i[0]==wh:
                if i[1][1]<value:
                    value=i[1][1]
                    time=k[0],i[0]
    if time!= None:
        return tuple(time)
    return None


################################################################
    #     if k[0]!=wh:
    #         for i in v:
    #             if i[0]==wh:
    #                 lst.append(k)
    # for i in lst:
    #     print("This is ", i)
    #     if i[1]<time:
    #         time=i[1]

    # for i in lst:
    #     if i[1]==time:
    #         ans.append(i[0])
#################################################################

def get_expensive_outgoing_supply_route(graph, wh):
    """
    Finds the most expensive outgoing supply route from a given warehouse.

    This function searches for all outgoing connections from the given warehouse
    and determines the route with the highest shipment cost.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID of the origin warehouse.

    Returns:
    tuple: A tuple containing (origin warehouse, destination warehouse) 
           representing the most expensive outgoing supply route.
    None: If the warehouse has no outgoing supply routes or does not exist in the graph.
    """
    # WRITE YOUR CODE HERE
    time=-(math.inf)
    lst=[wh]
    for k,v in graph.items():
        if k[0]==wh:
            for i in v:
                if i[1][1]>time:
                    time=i[1][1]
            for i in v:
                if time==i[1][1]:
                    lst.append(i[0])
    if len(lst)>1:
        return tuple(lst)
    return None
            
def get_expensive_incoming_supply_route(graph, wh):
    """
    Finds the most expensive incoming supply route for a given warehouse.

    This function searches for all incoming connections to the given warehouse
    and determines the route with the highest shipment cost.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID of the destination warehouse.

    Returns:
    tuple: A tuple containing (origin warehouse, destination warehouse) 
           representing the most expensive incoming supply route.
    None: If the warehouse has no incoming supply routes or does not exist in the graph.
    """

    value=-(math.inf)
    time=None
    for k,v in graph.items():
        for i in v:
            if i[0]==wh:
                if i[1][1]>value:
                    value= i[1][1]
                    time=(k[0],i[0])
    if time!= None:
        return time
    return None



def main():
    G = create_supply_chain('supply_chain.csv')
 
    route = get_cheapest_outgoing_supply_route(G, "W14")
    print(route)

    """
    Expected Output:
    ('W14', 'W17')
    """
    
    route = get_cheapest_outgoing_supply_route(G, "W24")
    print(route)

    """
    Expected Output:
    None
    """

    route = get_expensive_outgoing_supply_route(G, "W14")
    print(route)

    """
    Expected Output:
    ('W14', 'W1')
    """

    route = get_expensive_outgoing_supply_route(G, "W24")
    print(route)

    """
    Expected Output:
    None
    """

    route = get_cheapest_incoming_supply_route(G, "W14")
    print(route)

    """
    Expected Output:
    ('W16', 'W14')
    """

    route = get_cheapest_incoming_supply_route(G, "W24")
    print(route)

    """
    Expected Output:
    None
    """

    route = get_expensive_incoming_supply_route(G, "W14")
    print(route)

    """
    Expected Output:
    ('W18', 'W14')
    """

    route = get_expensive_incoming_supply_route(G, "W24")
    print(route)

    """
    Expected Output:
    None
    """

if __name__ == "__main__":
    main()
