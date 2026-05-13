# Hint: Import initialize_matrix function from q1. (from q1 import initialize_matrix)

from q1 import initialize_matrix
def matrix_multiplication(X, Y):
    """
    Multiplies two matrices A and B and returns the result.

    Parameters:
    A (list): The first matrix.
    B (list): The second matrix.

    Returns:
    list: The result of multiplying A and B.
        
    Note: 
        * Utilize your initialize matrix function from q1.py for initializing the resultant matrix.
        * You are not allowed to use any built-in list functiona.
    """

    # WRITE YOUR CODE HERE
    matrix=initialize_matrix(len(X),len(Y[0]))
    if len(X[0])!=len(Y):
        return "The number of columns in Matrix A does not equal the number of rows in Matrix B required for Matrix Multiplication."
    for i in range(len(X)):
        
        for j in range(len(Y[0])):
            a=0
            for k in range(len(Y)):
                a=a+X[i][k]*Y[k][j]
                matrix[i][j]=a

    return matrix




#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print(matrix_multiplication(
        [
            [12, 7, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            [5, 8, 1, 2], 
            [6, 7, 3, 0],
            [4, 5, 9, 1]
        ]
    ))
    # Should print: [
    #       [114, 160, 60, 27],
    #       [74, 97, 73, 14],
    #       [119, 157, 112, 23]
    #   ]

    print(matrix_multiplication(
        [
            [34, 1, 77],
            [2, 14, 8],
            [3, 17, 11]
        ],
        [
            [6, 8, 1],
            [9, 27, 5],
            [2, 43, 31]
        ]
    ))
    # Should print: [
    #       [367, 3610, 2426],
    #       [154, 738, 320],
    #       [193, 956, 429]
    #   ]

    print(matrix_multiplication(
        [
            [1, 2, 3],
            [4, 5, 6]
        ],
        [
            [7, 8],
            [9, 10],
            [11, 12]
        ]
    ))
    # Should print: [
    #       [58, 64],
    #       [139, 154]
    #   ]

    print(matrix_multiplication(
        [
            [7, 3],
            [2, 5],
            [6, 8],
            [9, 0]
        ],
        [
            [8, 14, 0, 3, -1],
            [7, 11, 5, 91, 3],
            [8, -4, 19, 5, 57]
        ]
    ))
    # Should print: 'The number of columns in Matrix A does not equal the number of rows in Matrix B required for Matrix Multiplication.', True), 

    print(matrix_multiplication(
        [
            [3, 4, 2]
        ],
        [
            [13, 9, 7, 15],
            [8, 7, 4, 6],
            [6, 4, 0, 3]
        ]
    ))
    # Should print: [
    #       [83, 63, 37, 75]
    #   ]

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q4.py