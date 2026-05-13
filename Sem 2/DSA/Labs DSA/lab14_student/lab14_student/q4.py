from HelperFunctions import *
from q2 import GetShortestPath

def GetShortestDistanceBetweenCities(source, destination):
    """
    Computes the shortest path between two cities using Dijkstra's algorithm.

    Reads the adjacency matrix from `connections.csv` and returns the shortest 
    path from `source` to `destination` as a list of tuples (start_city, end_city, distance), 
    or -1 if no path exists.

    Args:
        source (str): The starting city.
        destination (str): The destination city.

    Returns:
        list or int: Shortest path as a list of tuples (start_city, end_city, distance), 
                     or -1 if no path exists.
    """

    a=csv_to_adj_list('connections.csv')
    s=GetShortestPath(a,source, destination)
    return s


def csv_to_adj_list(filename: str):

    # WRITE YOUR CODE HERE
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile)
        lst=[]
        g={}
        for i in csv_reader:
            lst.append(i)
        
    nodes=lst[0]
    matrix=lst[1::]
    for i in matrix:
        a=[]
        for j in range(len(i)):
            if i[j]!="-1" and nodes[j]!=i[0] and j!=0:
                a.append((nodes[j],int(i[j])))
            g[i[0]]= a
    return g
    pass


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    print(GetShortestDistanceBetweenCities("Islamabad",'Nathiagali'))   
    '''Should print:
    [('Islamabad', 'Murree', 49), ('Murree', 'Nathiagali', 36)]
    '''

    print(GetShortestDistanceBetweenCities('Islamabad', 'Naran'))
    ''' Should print: 
    [('Islamabad', 'Murree', 49), ('Murree', 'Nathiagali', 36), ('Nathiagali', 'Abbottabad', 34), 
     ('Abbottabad', 'Mansehra', 23), ('Mansehra', 'Balakot', 37), ('Balakot', 'Kaghan', 59), 
     ('Kaghan', 'Naran', 22)]
    '''
    
    print(GetShortestDistanceBetweenCities("Islamabad", "Murree"))
    ''' Should print:
    [('Islamabad', 'Murree', 49)]
    '''

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q4.py