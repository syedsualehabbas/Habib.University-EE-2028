import csv
filename="supply_chain.csv"

def addVertices(G, vertices):
    """Add vertices to the graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    vertices :
        A list of vertices to be added to the graph
    """

    # provide implementation here
    pass

def addEdges(G, edges):
    """Add edges to the graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    edges :
        A list of edges to be added to the graph
    """
    # provide implementation here
    pass


def list_of_vertices(G):
    """
    Reads a CSV file and generates a list of vertices.

    Each vertex is represented as a tuple containing:
    - Warehouse ID (str)
    - Transit Trust Rating (float)

    Parameters:
    filename (str): The path to the CSV file containing supply chain data.

    Returns:
    list: A list of tuples representing vertices.
    """
    # provide implementation here
    lst=[]
    for i in G:
        lst.append(i[0])
    return lst

def list_of_edges(filename):
    """
    Reads a CSV file and generates a list of edges.

    Each edge represents a connection from an Outbound Nexus warehouse 
    to an Inbound Hub warehouse. The edge is represented as a tuple containing:
    - Outbound Nexus Warehouse ID (str)
    - Inbound Hub Warehouse ID (str)
    - Shipment Time (int)
    - Shipment Cost (float)
    - Shipping Method (str)

    Parameters:
    filename (str): The path to the CSV file containing supply chain data.

    Returns:
    list: A list of tuples representing edges.
    """

    # provide implementation here
    pass

def create_supply_chain(filename):
    """
    Constructs the supply chain graph from a CSV file.

    The supply chain is represented as an adjacency map where:
    - The keys are vertices (tuples containing Warehouse ID and Transit Trust Rating).
    - The values are lists of tuples representing the edges. 
      Each edge is defined by:
      - Inbound Hub Warehouse ID (str)
      - A tuple containing (Shipment Time, Shipment Cost, Shipping Method).

    Parameters:
    filename (str): The path to the CSV file containing supply chain data.

    Returns:
    dict: A graph represented as an adjacency map.
    """

    # provide implementation here
    L = []
    G={}
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile)
    
        for i in csv_reader:
            L.append(i)

    for i in (L[1::]):
        if (i[0],eval(i[5])) in G:
            G[(i[0],eval(i[5]))].append((i[1],(eval(i[2]),eval(i[3]),i[4])))
        else:
            G[(i[0],eval(i[5]))]=[(i[1],(eval(i[2]),eval(i[3]),i[4]))]
        
   
   
    return G

def main():

    vertices = list_of_vertices(filename)
    print(vertices)

    """
    Expected Output:
    [('W1', 76.14), ('W10', 94.39), ('W11', 70.81), ('W12', 76.02), ('W13', 73.13), 
     ('W14', 93.7), ('W15', 86.31), ('W16', 73.24), ('W17', 82.5), ('W18', 94.33), 
     ('W19', 91.9), ('W2', 78.09), ('W20', 89.33), ('W3', 82.95), ('W4', 73.83), 
     ('W5', 87.41), ('W6', 77.81), ('W7', 86.43), ('W8', 86.2), ('W9', 91.85)]
    """

    edges = list_of_edges(filename)
    print(edges)

    """
    Expected Output:
    [('W1', 'W11', 2, 757.96, 'Sea'), ('W1', 'W4', 11, 913.21, 'Air'), ('W10', 'W16', 1, 418.59, 'Sea'), 
     ('W10', 'W11', 9, 556.73, 'Sea'), ('W11', 'W1', 5, 339.96, 'Ground'), ('W12', 'W7', 9, 582.59, 'Ground'), 
     ('W12', 'W9', 8, 485.8, 'Sea'), ('W12', 'W2', 12, 974.87, 'Ground'), ('W13', 'W20', 6, 195.26, 'Sea'), 
     ('W13', 'W17', 15, 284.62, 'Ground'), ('W13', 'W6', 12, 552.92, 'Ground'), ('W13', 'W14', 11, 536.73, 'Sea'), 
     ('W13', 'W12', 2, 661.32, 'Sea'), ('W14', 'W1', 6, 851.19, 'Air'), ('W14', 'W10', 4, 821.98, 'Air'), 
     ('W14', 'W17', 5, 66.43, 'Ground'), ('W14', 'W15', 1, 75.66, 'Ground'), ('W14', 'W18', 6, 738.24, 'Sea'), 
     ('W14', 'W12', 12, 689.56, 'Sea'), ('W15', 'W5', 3, 320.43, 'Sea'), ('W15', 'W19', 1, 596.11, 'Sea'), 
     ('W15', 'W10', 15, 368.41, 'Ground'), ('W15', 'W4', 2, 654.81, 'Ground'), ('W15', 'W12', 7, 509.52, 'Sea'), 
     ('W16', 'W10', 14, 521.95, 'Air'), ('W16', 'W11', 5, 884.69, 'Air'), ('W16', 'W2', 4, 827.64, 'Air'), 
     ('W16', 'W7', 1, 805.83, 'Ground'), ('W16', 'W8', 11, 122.25, 'Air'), ('W16', 'W14', 15, 193.98, 'Ground'), 
     ('W17', 'W16', 14, 923.49, 'Air'), ('W17', 'W11', 2, 255.71, 'Ground'), ('W17', 'W18', 7, 526.41, 'Ground'), 
     ('W17', 'W19', 6, 888.75, 'Sea'), ('W18', 'W8', 10, 836.67, 'Ground'), ('W18', 'W14', 1, 779.06, 'Ground'), 
     ('W18', 'W3', 11, 761.62, 'Air'), ('W18', 'W7', 2, 861.84, 'Ground'), ('W18', 'W17', 8, 896.6, 'Sea'), 
     ('W18', 'W13', 11, 725.71, 'Air'), ('W19', 'W17', 7, 830.31, 'Ground'), ('W19', 'W11', 7, 580.12, 'Ground'), 
     ('W19', 'W9', 10, 82.76, 'Ground'), ('W19', 'W13', 4, 945.58, 'Ground'), ('W19', 'W3', 6, 997.17, 'Air'), 
     ('W19', 'W4', 14, 439.68, 'Sea'), ('W2', 'W18', 7, 765.5, 'Sea'), ('W2', 'W19', 7, 494.7, 'Air'), 
     ('W2', 'W5', 13, 655.03, 'Ground'), ('W2', 'W7', 13, 876.33, 'Air'), ('W20', 'W12', 13, 491.64, 'Air'), 
     ('W20', 'W9', 8, 767.89, 'Air'), ('W20', 'W18', 7, 722.67, 'Ground'), ('W20', 'W3', 7, 373.31, 'Ground'), 
     ('W20', 'W5', 10, 930.21, 'Air'), ('W20', 'W17', 1, 546.54, 'Ground'), ('W3', 'W11', 4, 248.07, 'Ground'), 
     ('W3', 'W19', 8, 488.74, 'Ground'), ('W4', 'W17', 4, 205.89, 'Ground'), ('W4', 'W15', 15, 489.96, 'Air'), 
     ('W4', 'W3', 15, 347.5, 'Ground'), ('W4', 'W2', 6, 944.41, 'Ground'), ('W5', 'W4', 10, 316.61, 'Air'), 
     ('W5', 'W13', 12, 502.91, 'Air'), ('W5', 'W1', 15, 490.32, 'Air'), ('W5', 'W2', 2, 740.04, 'Air'), 
     ('W6', 'W4', 10, 256.43, 'Ground'), ('W6', 'W19', 2, 887.58, 'Sea'), ('W7', 'W19', 3, 642.02, 'Sea'), 
     ('W7', 'W8', 10, 965.04, 'Air'), ('W7', 'W11', 14, 732.91, 'Sea'), ('W7', 'W15', 14, 88.06, 'Sea'), 
     ('W7', 'W17', 12, 749.38, 'Ground'), ('W8', 'W12', 10, 177.52, 'Sea'), ('W8', 'W18', 13, 281.47, 'Air'), 
     ('W8', 'W6', 14, 256.28, 'Ground'), ('W8', 'W11', 9, 262.95, 'Air'), ('W8', 'W9', 1, 619.01, 'Ground'), 
     ('W9', 'W16', 9, 446.04, 'Ground'), ('W9', 'W8', 2, 138.6, 'Sea'), ('W9', 'W6', 9, 738.54, 'Ground'), 
     ('W9', 'W12', 1, 915.7, 'Ground'), ('W9', 'W3', 12, 199.8, 'Air'), ('W9', 'W10', 4, 488.08, 'Sea')]
    """

    supply_chain = create_supply_chain(filename)
    print(supply_chain)

    """
    Expected Output:
    {('W1', 76.14): [('W11', (2, 757.96, 'Sea')), ('W4', (11, 913.21, 'Air'))], 
     ('W10', 94.39): [('W16', (1, 418.59, 'Sea')), ('W11', (9, 556.73, 'Sea'))],  
     ('W11', 70.81): [('W1', (5, 339.96, 'Ground'))], 
     ('W12', 76.02): [('W7', (9, 582.59, 'Ground')), ('W9', (8, 485.8, 'Sea')), ('W2', (12, 974.87, 'Ground'))], 
     ('W13', 73.13): [('W20', (6, 195.26, 'Sea')), ('W17', (15, 284.62, 'Ground')), ('W6', (12, 552.92, 'Ground')), 
                         ('W14', (11, 536.73, 'Sea')), ('W12', (2, 661.32, 'Sea'))], 
    ('W14', 93.7): [('W1', (6, 851.19, 'Air')), ('W10', (4, 821.98, 'Air')), ('W17', (5, 66.43, 'Ground')), 
                        ('W15', (1, 75.66, 'Ground')), ('W18', (6, 738.24, 'Sea')), ('W12', (12, 689.56, 'Sea'))], 
    ('W15', 86.31): [('W5', (3, 320.43, 'Sea')), ('W19', (1, 596.11, 'Sea')), ('W10', (15, 368.41, 'Ground')), 
                        ('W4', (2, 654.81, 'Ground')), ('W12', (7, 509.52, 'Sea'))], 
    ('W16', 73.24): [('W10', (14, 521.95, 'Air')), ('W11', (5, 884.69, 'Air')), ('W2', (4, 827.64, 'Air')), 
                        ('W7', (1, 805.83, 'Ground')), ('W8', (11, 122.25, 'Air')), ('W14', (15, 193.98, 'Ground'))], 
    ('W17', 82.5): [('W16', (14, 923.49, 'Air')), ('W11', (2, 255.71, 'Ground')), ('W18', (7, 526.41, 'Ground')), 
                        ('W19', (6, 888.75, 'Sea'))], 
    ('W18', 94.33): [('W8', (10, 836.67, 'Ground')), ('W14', (1, 779.06, 'Ground')), ('W3', (11, 761.62, 'Air')), 
                        ('W7', (2, 861.84, 'Ground')), ('W17', (8, 896.6, 'Sea')), ('W13', (11, 725.71, 'Air'))], 
    ('W19', 91.9): [('W17', (7, 830.31, 'Ground')), ('W11', (7, 580.12, 'Ground')), ('W9', (10, 82.76, 'Ground')), 
                        ('W13', (4, 945.58, 'Ground')), ('W3', (6, 997.17, 'Air')), ('W4', (14, 439.68, 'Sea'))], 
    ('W2', 78.09): [('W18', (7, 765.5, 'Sea')), ('W19', (7, 494.7, 'Air')), ('W5', (13, 655.03, 'Ground')), 
                        ('W7', (13, 876.33, 'Air'))], 
    ('W20', 89.33): [('W12', (13, 491.64, 'Air')), ('W9', (8, 767.89, 'Air')), ('W18', (7, 722.67, 'Ground')), 
                        ('W3', (7, 373.31, 'Ground')), ('W5', (10, 930.21, 'Air')), ('W17', (1, 546.54, 'Ground'))], 
    ('W3', 82.95): [('W11', (4, 248.07, 'Ground')), ('W19', (8, 488.74, 'Ground'))], 
    ('W4', 73.83): [('W17', (4, 205.89, 'Ground')), ('W15', (15, 489.96, 'Air')), ('W3', (15, 347.5, 'Ground')), 
                        ('W2', (6, 944.41, 'Ground'))], 
    ('W5', 87.41): [('W4', (10, 316.61, 'Air')), ('W13', (12, 502.91, 'Air')), ('W1', (15, 490.32, 'Air')), 
                        ('W2', (2, 740.04, 'Air'))], 
    ('W6', 77.81): [('W4', (10, 256.43, 'Ground')), ('W19', (2, 887.58, 'Sea'))], 
    ('W7', 86.43): [('W19', (3, 642.02, 'Sea')), ('W8', (10, 965.04, 'Air')), ('W11', (14, 732.91, 'Sea')), 
                        ('W15', (14, 88.06, 'Sea')), ('W17', (12, 749.38, 'Ground'))], 
    ('W8', 86.2): [('W12', (10, 177.52, 'Sea')), ('W18', (13, 281.47, 'Air')), ('W6', (14, 256.28, 'Ground')), 
                        ('W11', (9, 262.95, 'Air')), ('W9', (1, 619.01, 'Ground'))], 
    ('W9', 91.85): [('W16', (9, 446.04, 'Ground')), ('W8', (2, 138.6, 'Sea')), ('W6', (9, 738.54, 'Ground')), 
                        ('W12', (1, 915.7, 'Ground')), ('W3', (12, 199.8, 'Air')), ('W10', (4, 488.08, 'Sea'))]}
    """

if __name__ == "__main__":
    main()
