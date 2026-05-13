from HelperFunctions import *
from q1 import *

def GetShortestPath(graph, source, destination):
    """
    Finds the shortest path from source to destination using Dijkstra's algorithm.

    Args:
        graph (dict): A dictionary of nodes and their neighbors with edge weights.
        source (any): The starting node.
        destination (any): The target node.

    Returns:
        list: A list of (prev_node, node, weight) tuples representing the shortest path, or -1 if no path exists.
    """

    # WRITE YOUR CODE HERE
    output=[]
    queue=[]
    dist={}
    prev={}
    for v in graph:
        prev[v]=None
        if v == source:
            dist[v]=0
            EnQueue(queue,v,0)
        else:
            dist[v]=math.inf
            EnQueue(queue,v,math.inf)
    # print(queue)
    # print(f"this is pre v {prev}")
    # print(f"this is dist {dist}")
    while queue!=[]:
        min=DeQueue(queue)
        # neighbors=GetNeighbors(graph, min)
        for i in graph[min]:
            if i[1]+dist[min]<dist[i[0]]:
                dist[i[0]]=i[1]+dist[min]
                prev[i[0]]=((min,i[1]))
                EnQueue(queue, i[0], dist[i[0]])
    print(dist, prev)
    ans=check_path(prev, source, destination, output)
    if ans==[] or ans==None:
        return -1
    ans.reverse()
    return ans


    
def check_path(prev, source, destination, result):
    if destination==source:
        return result
    if prev[destination]:
        c=prev[destination]
        a=c[0],destination,c[1]
        result.append(a)
        return check_path(prev, source, c[0], result)
    return

#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    graph = {
        'A': [('D', 2), ('E', 6), ('B', 7)], 
        'B': [('C', 3), ('A', 7)], 
        'C': [('B', 3), ('D', 2), ('G', 2)], 
        'D': [('A', 2), ('C', 2), ('F', 8)], 
        'E': [('A', 6), ('F', 9)], 
        'F': [('D', 8), ('E', 9), ('G', 4)], 
        'G': [('C', 2), ('F', 4)]
    }

    print(GetShortestPath(graph, 'A', 'G'))
    ''' Should print:
    [('A', 'D', 2), ('D', 'C', 2), ('C', 'G', 2)]
    '''

    print(GetShortestPath(graph, 'A', 'C'))
    ''' Should print:
    [('A', 'D', 2), ('D', 'C', 2)]
    '''

    print(GetShortestPath(graph, 'A', 'D'))
    ''' Should print:
    [('A', 'D', 2)]
    '''


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q2.py