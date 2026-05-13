# Hint: Import initialize_matrix function from q1. (from q1 import initialize_matrix)
from q1 import initialize_matrix


def matrix_subtraction(X, Y):
    """
    Subtracts matrix B from matrix A element-wise.

    Parameters:
    A (list): First matrix.
    B (list): Second matrix.

    Returns:
    list: Resulting matrix, or an error message if dimensions don't match.

    Note: 
        * Utilize your initialize matrix function from q1.py for initializing the resultant matrix.
        * You are not allowed to use any built-in list functions.
    """

    # WRITE YOUR CODE HERE
    matrix1=initialize_matrix(len(X),len(X[0]))

    if len(X)!=len(Y) or len(X[0])!=len(Y[0]):
        return "Matrices A and B don't have the same dimension required for matrix subtraction."
    else:
        for i in range(len(X)):
            for j in range(len(X[0])):
                a=X[i][j]-Y[i][j]
                matrix1[i][j]=a
    return matrix1





    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print(matrix_subtraction(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ], 
        [   [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
    ))
    # Should print: [
    #       [-8, -6, -4], 
    #       [-2, 0, 2], 
    #       [4, 6, 8]
    #   ]

    print(matrix_subtraction(
        [
            [12, 7, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            [5, 8, 1],
            [6, 7, 3],
            [4, 5, 9]
        ]
    ))
    # Should print: [
    #   [7, -1, 2], 
    #   [-2, -2, 3], 
    #   [3, 3, 0]
    # ]

    print(matrix_subtraction(
        [
            [1],
            [2]
        ], 
        [   [3, 5],
            [4, 6]
        ]
    ))
    # Should print: "Matrices A and B don't have the same dimension required for matrix subtraction.", True), 


    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q2.py