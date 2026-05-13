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
def partitionlowFunction(matrix,low,high,column):
    pivot= low
    matrix[low],matrix[pivot]=matrix[pivot],matrix[low]
    return partitionfunction(matrix,low,high,column)
def quick_sort_rectangles(matrix, low, high, column):
    if low<high:
        part=partitionlowFunction(matrix,low,high,column)
        print(matrix)
        quick_sort_rectangles(matrix,low,part-1,column)
        quick_sort_rectangles(matrix,part+1,high,column)
        
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    quick_sort_rectangles(
        [
            {"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"},
            {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"},
            {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"},
            {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}
        ], 0, 3, "Length")
    ''' Should print:
        [
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}
        ]

        [
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}
        ]
    '''

    print()

    quick_sort_rectangles(
        [
            {"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"},
            {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"},
            {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"},
            {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}
        ], 0, 3, "ID")
    ''' Should print:
        [
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'},
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}
        ]

        [
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'},
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}
        ]

        [
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'},
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}
        ]
    '''

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q3.py