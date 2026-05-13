from HelperFunctions import *
from q2 import GetShortestPath
    
def GetShortestPathGrid(grid, source, destination):
    """
    # WRITE YOUR CODE HERE
    """
    g = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            g[(i, j)] = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i+1<len(grid) and grid[i+1][j]!=-1:
                g[(i,j)].append(((i+1, j),1))
            if i-1>-1 and grid[i-1][j]!=-1:
                g[(i,j)].append(((i-1, j), 1))
            if j+1<len(grid[0]) and grid[i][j+1]!=-1:
                g[(i, j)].append(((i, j+1), 1))
            if j-1>-1 and grid[i][j-1]!=-1:
                g[(i, j)].append(((i, j-1),1))
    
    print(g)
    return GetShortestPath(g, source, destination)

    pass


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    grid =[[1, 1, 1], [-1, 1, 1], [1, -1, 1]]
    source = (0, 0)
    destination = (2, 2)
    print(GetShortestPathGrid(grid, source, destination))
    ''' Should print ANY ONE of the below shortest paths:
    [((0, 0), (0, 1), 1), ((0, 1), (1, 1), 1), ((1, 1), (1, 2), 1), ((1, 2), (2, 2), 1)]
    [((0, 0), (0, 1), 1), ((0, 1), (0, 2), 1), ((0, 2), (1, 2), 1), ((1, 2), (2, 2), 1)]
    '''

    grid = [[1, 1], [-1, 1]]
    source = (0, 0)
    destination = (1, 1)
    print(GetShortestPathGrid(grid, source, destination))
    ''' Should print:
    [((0, 0), (0, 1), 1), ((0, 1), (1, 1), 1)]
    '''

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q3.py