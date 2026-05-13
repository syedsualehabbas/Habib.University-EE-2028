
def partitionfunction(matrix,low,high,column):
    pivot = low
    i=low+1
    for j in range(low+1,high+1):
        if matrix[j][column]<=matrix[pivot][column]:
            matrix[i],matrix[j]=matrix[j],matrix[i]
            i+=1
    matrix[pivot],matrix[i-1]=matrix[i-1],matrix[pivot]
    pivot=i-1
    return pivot
def partitionhighFunction(matrix,low,high,column):
    pivot= high
    matrix[low],matrix[pivot]=matrix[pivot],matrix[low]
    return partitionfunction(matrix,low,high,column)
def quick_sort_by_column_number(matrix, low, high, column):
    if low<high:
        part=partitionhighFunction(matrix,low,high,column)
        print(matrix)
        quick_sort_by_column_number(matrix,low,part-1,column)
        quick_sort_by_column_number(matrix,part+1,high,column)
        
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    quick_sort_by_column_number(
        [
            ['square', 'rectangle', 'triangle'], 
            ['chair', 'table', 'house'], 
            ['motor cycle', 'car', 'truck']
        ], 0, 2, 1)
    ''' Should print:
        [
            ['motor cycle', 'car', 'truck'],
            ['chair', 'table', 'house'],
            ['square', 'rectangle', 'triangle']
        ]
        
        [
            ['motor cycle', 'car', 'truck'],
            ['square', 'rectangle', 'triangle'],
            ['chair', 'table', 'house']
        ]
    '''

    print()

    quick_sort_by_column_number(
        [
            [75, 28, 12],
            [63, 37, 23],
            [84, 15, 49]
        ], 0, 2, 1)
    
    ''' Should print:
        [
            [84, 15, 49],
            [63, 37, 23],
            [75, 28, 12]
        ]
        
        [
            [84, 15, 49],
            [75, 28, 12],
            [63, 37, 23]
        ]
    '''

    print()

    quick_sort_by_column_number([['square', 'rectangle', 'triangle'], ['chair','table', 'house'], ['motor cycle', 'car', 'truck']], 0, 2, 2)

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q2.py