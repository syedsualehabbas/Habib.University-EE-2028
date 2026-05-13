def sort_rectangles(rectangle_records, record_title):
    """
    Sorts the rectangle records by the specified key using Insertion Sort.

    Parameters:
    rectangle_records (list of dict): List of rectangle dictionaries to be sorted.
    record_title (str): Key to sort by (e.g., "ID", "Length", "Breadth", "Color").

    Returns:
    list of dict: Sorted rectangle records.
    """

    # WRITE YOUR CODE HERE
    for i in range(1,len(rectangle_records)):
        temp=rectangle_records[i]
        j=i-1
        while j>=0 and rectangle_records[j][record_title]>temp[record_title]:
            rectangle_records[j+1]=rectangle_records[j]
            j-=1
        rectangle_records[j+1]=temp
    return rectangle_records

    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print(sort_rectangles(
        [
            {"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"},
            {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"},
            {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"},
            {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}
        ], "ID"))
    ''' Should print:
        [
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'},
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'},
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'},
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}
        ]
    '''

    print(sort_rectangles(
        [
            {"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"},
            {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"},
            {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"},
            {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}
        ], "Length"))
    ''' Should print:
        [
            {'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}, 
            {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'}, 
            {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'}, 
            {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}
        ]
    '''

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q5.py