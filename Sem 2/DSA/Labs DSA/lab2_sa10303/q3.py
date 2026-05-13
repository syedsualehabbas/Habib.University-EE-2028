# Hint: Import initialize_matrix function from q1. (from q1 import initialize_matrix)
from q1 import initialize_matrix

def matrix_transpose(X):
    """
    Returns the transpose of matrix A.

    Parameters:
    A (list): The matrix to transpose.

    Returns:
    list: The transposed matrix.
    
    Note: 
        * Utilize your initialize matrix function from q1.py for initializing the resultant matrix.
        * You are not allowed to use any built-in list functions.
    """

    # WRITE YOUR CODE HERE
    matrix=initialize_matrix(len(X[0]),len(X))
    for i in range(len(matrix)):
        for j in range(len(X)):
            matrix[i][j]=X[j][i]
    return matrix
        

    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print(matrix_transpose([
        [12, 7], 
        [4, 5], 
        [3, 8]
    ]))
    # Should print: [
    #   [12, 4, 3],
    #   [7, 5, 8]
    # ]

    print(matrix_transpose([
        [12, 4, 3],
        [7, 5, 8]
    ]))
    # Should print: [
    #   [12, 7],
    #   [4, 5],
    #   [3, 8]
    # ]

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q3.py