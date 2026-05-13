def selection_sort(arr):
    """
    Sorts a list in ascending order using Selection Sort.
    
    Repeatedly selects the smallest element from the unsorted part and swaps it 
    with the first unsorted element. Prints the list after each iteration.
    
    Parameters:
    arr (list): List of elements (numbers or strings) to be sorted.
    
    Returns:
    None: Sorts the list in place and prints the state after each iteration.

    Steps:
        Step 1 => Set MIN to location 0
        Step 2 => Search the minimum element in the list
        Step 3 => Swap with value at location MIN
        Step 4 => Increment MIN to point to next element
        Step 5 => Repeat until list is sorted
    """
    
    for i in range(len(arr)):  
        min=i
        for j in range(i+1,len(arr)): 
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
        
        print(arr)
    


    # WRITE YOUR CODE HERE
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    selection_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])
    ''' Should print:
    [17, 26, 93, 54, 77, 31, 44, 55, 20]
    [17, 20, 93, 54, 77, 31, 44, 55, 26]
    [17, 20, 26, 54, 77, 31, 44, 55, 93]
    [17, 20, 26, 31, 77, 54, 44, 55, 93]
    [17, 20, 26, 31, 44, 54, 77, 55, 93]
    [17, 20, 26, 31, 44, 54, 77, 55, 93]
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    '''
    print()

    selection_sort(['Aisha', 'Nadia', 'Waqar', 'Saleha', 'Hasan', 'Shahid', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj'])
    ''' Should print:
    ['Abdullah', 'Nadia', 'Waqar', 'Saleha', 'Hasan', 'Shahid', 'Shah Jamal', 'Aisha', 'Umair', 'Taj']
    ['Abdullah', 'Aisha', 'Waqar', 'Saleha', 'Hasan', 'Shahid', 'Shah Jamal', 'Nadia', 'Umair', 'Taj']
    ['Abdullah', 'Aisha', 'Hasan', 'Saleha', 'Waqar', 'Shahid', 'Shah Jamal', 'Nadia', 'Umair', 'Taj']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Waqar', 'Shahid', 'Shah Jamal', 'Saleha', 'Umair', 'Taj']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shahid', 'Shah Jamal', 'Waqar', 'Umair', 'Taj']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Waqar', 'Umair', 'Taj']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Waqar', 'Umair', 'Taj']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']
    '''
    print()

    selection_sort([4, 1, 3, 9, 7])
    ''' Should print:
    [1, 4, 3, 9, 7]
    [1, 3, 4, 9, 7]
    [1, 3, 4, 9, 7]
    [1, 3, 4, 7, 9]
    [1, 3, 4, 7, 9]
    '''
    print()

    selection_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    ''' Should print:
    [1, 9, 8, 7, 6, 5, 4, 3, 2, 10]
    [1, 2, 8, 7, 6, 5, 4, 3, 9, 10]
    [1, 2, 3, 7, 6, 5, 4, 8, 9, 10]
    [1, 2, 3, 4, 6, 5, 7, 8, 9, 10]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    '''
    print()

    selection_sort([12, 8, -6, 2, 4, 5, 3, 7, 4, 2])
    ''' Should print:
    [-6, 8, 12, 2, 4, 5, 3, 7, 4, 2]
    [-6, 2, 12, 8, 4, 5, 3, 7, 4, 2]
    [-6, 2, 2, 8, 4, 5, 3, 7, 4, 12]
    [-6, 2, 2, 3, 4, 5, 8, 7, 4, 12]
    [-6, 2, 2, 3, 4, 5, 8, 7, 4, 12]
    [-6, 2, 2, 3, 4, 4, 8, 7, 5, 12]
    [-6, 2, 2, 3, 4, 4, 5, 7, 8, 12]
    [-6, 2, 2, 3, 4, 4, 5, 7, 8, 12]
    [-6, 2, 2, 3, 4, 4, 5, 7, 8, 12]
    [-6, 2, 2, 3, 4, 4, 5, 7, 8, 12]
    '''
    print()

    selection_sort(['FunForFun', 'Practice.FunForFun', 'FunforFun'])
    ''' Should print:
    ['FunForFun', 'Practice.FunForFun', 'FunforFun']
    ['FunForFun', 'FunforFun', 'Practice.FunForFun']
    ['FunForFun', 'FunforFun', 'Practice.FunForFun']
    '''
    print()

    selection_sort([37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54])
    ''' Should print:
    [0, 23, 37, 17, 12, 72, 31, 46, 100, 88, 54]
    [0, 12, 37, 17, 23, 72, 31, 46, 100, 88, 54]
    [0, 12, 17, 37, 23, 72, 31, 46, 100, 88, 54]
    [0, 12, 17, 23, 37, 72, 31, 46, 100, 88, 54]
    [0, 12, 17, 23, 31, 72, 37, 46, 100, 88, 54]
    [0, 12, 17, 23, 31, 37, 72, 46, 100, 88, 54]
    [0, 12, 17, 23, 31, 37, 46, 72, 100, 88, 54]
    [0, 12, 17, 23, 31, 37, 46, 54, 100, 88, 72]
    [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]
    [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]
    [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]
    '''
    print()

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q1.py