from Q10 import *

def calculate_average(graph, warehouse, option):
    """
    HELPER FUNCTION FOR THE find_bottlenecks function below
    
    Calculates the average shipment time or cost for outgoing shipments from a given warehouse.

    This function iterates through all direct connections of a warehouse and computes 
    the average value based on the chosen metric (either "time" or "cost").

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    warehouse (str): The alphanumeric warehouse ID whose shipment data is analyzed.
    option (str): Either "time" for Shipment Time or "cost" for Shipment Cost.

    Returns:
    float: The average shipment time or cost for the given warehouse.
    """
    if option=="time":
        a=0
    else:
        a=1
    sum=0
    for k in graph:
        if k[0]==warehouse:
            b=len(graph[k])
            for v in graph[k]:
                sum+=v[1][a]
            return sum/b
    return -1




def find_bottlenecks(graph, threshold, option):
    """
    Identifies warehouses that are causing bottlenecks in the supply chain.

    This function determines which warehouses have an average shipment time or cost 
    above the given threshold, indicating potential delays or high costs.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    threshold (float): The threshold value for identifying bottlenecks.
    option (str): Either "time" for Shipment Time or "cost" for Shipment Cost.

    Returns:
    list: A list of warehouse IDs that are causing bottlenecks.
    Returns an empty list if no bottleneck found
    """
    lst=[]
    for k in graph:
        if calculate_average(graph,k[0],option)>threshold:
            lst.append(k[0])

    return lst


def main():
    G = create_supply_chain('supply_chain.csv')
    print(find_bottlenecks(G, 5, "time"))
    """ Expected Output:
    ['W1', 'W12', 'W13', 'W14', 'W15', 'W16', 'W17', 'W18', 'W19', 'W2', 'W20', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9']
    """
    
    print(find_bottlenecks(G, 20, "time"))
    """ Expected Output:
    []
    """
    
    print(find_bottlenecks(G, 330.00, "cost"))
    """ Expected Output:
    ['W1', 'W10', 'W11', 'W12', 'W13', 'W14', 'W15', 'W16', 'W17', 'W18', 'W19', 'W2', 'W20', 'W3', 'W4', 'W5', 'W6', 'W7', 'W9']
    """
    
    print(find_bottlenecks(G, 1500.00, "cost"))
    """ Expected Output:
    []
    """


if __name__ == "__main__":
    main()
