def sort_matrix_by_columnNumber(matrix, col):
    """
    Sorts matrix rows by a specified column using Selection Sort.

    Parameters:
    matrix (list of lists): 2D list to be sorted.
    columnNumber (int): Column index to sort by.

    Returns:
    list of lists: Sorted matrix.
    """

    # WRITE YOUR CODE HERE
    for i in range(len(matrix)):  
        min=i
        for j in range(i+1,len(matrix)): 
            if matrix[j][col]<matrix[min][col]:
                min=j
        matrix[i],matrix[min]=matrix[min],matrix[i]
    return matrix

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print(sort_matrix_by_columnNumber(
        [
            [5, 8, 1], 
            [6, 7, 3], 
            [5, 4, 9]
        ], 0))
    ''' Should print:
        [
            [5 , 8 , 1],
            [5 , 4 , 9],
            [6 , 7 , 3]
        ]
    '''

    print(sort_matrix_by_columnNumber(
        [
            ['square', 'rectangle', 'triangle'], 
            ['chair', 'table', 'house'], 
            ['motor cycle', 'car', 'truck']
        ], 2))
    ''' Should print:
        [
            ['chair', 'table', 'house'],
            ['square', 'rectangle', 'triangle'],
            ['motor cycle', 'car', 'truck']
        ]
    '''

    print(sort_matrix_by_columnNumber([[65, 73, 42, 72, 80, 93, 4, 78, 34, 35], [13, 20, 34, 57, 20, 96, 1, 76, 15, 91], [27, 5, 40, 74, 37, 96, 65, 21, 79, 64], [0, 74, 13, 51, 81, 78, 64, 47, 81, 42], [34, 56, 33, 54, 94, 77, 51, 11, 56, 30], [12, 91, 93, 73, 98, 29, 18, 84, 99, 74], [43, 16, 62, 78, 70, 50, 51, 86, 10, 39], [54, 44, 74, 2, 39, 6, 47, 80, 95, 7], [83, 52, 49, 73, 24, 88, 81, 11, 99, 59], [100, 60, 97, 90, 23, 71, 52, 79, 13, 71]], 0))
    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q4.py