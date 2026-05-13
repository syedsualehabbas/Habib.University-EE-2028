def bubble_sort(arr):
    """
    Sorts a list in ascending order using the Bubble Sort algorithm.
    
    Repeatedly compares adjacent elements and swaps them if they are in the wrong order.
    After each pass through the list, the state of the list is printed.

    Parameters:
    arr (list): List of elements (numbers or strings) to sort.
    
    Returns:
    None: The list is sorted in place and printed after each iteration.

    Steps:
        Step 1 => If the list has only one element, return it as it's already sorted.
        Step 2 => Loop len(arr)-1 times, comparing and swapping adjacent elements.
        Step 3 => After each pass, the largest unsorted element is in its correct position.
    """

    # WRITE YOUR CODE HERE
    if len(arr)==1:
        print(arr)
        return
    for i in range(1,len(arr)):
        for j in range(len(arr)-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        print(arr)


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    bubble_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])
    ''' Should print:
    [26, 54, 17, 77, 31, 44, 55, 20, 93]
    [26, 17, 54, 31, 44, 55, 20, 77, 93]
    [17, 26, 31, 44, 54, 20, 55, 77, 93]
    [17, 26, 31, 44, 20, 54, 55, 77, 93]
    [17, 26, 31, 20, 44, 54, 55, 77, 93]
    [17, 26, 20, 31, 44, 54, 55, 77, 93]
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    '''
    print()

    bubble_sort(['Aisha', 'Nadia', 'Waqar', 'Saleha', 'Hasan', 'Shahid', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj'])
    ''' Should print:
    ['Aisha', 'Nadia', 'Saleha', 'Hasan', 'Shahid', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj', 'Waqar']
    ['Aisha', 'Nadia', 'Hasan', 'Saleha', 'Shah Jamal', 'Abdullah', 'Shahid', 'Taj', 'Umair', 'Waqar']
    ['Aisha', 'Hasan', 'Nadia', 'Saleha', 'Abdullah', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']
    ['Aisha', 'Hasan', 'Nadia', 'Abdullah', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']
    ['Aisha', 'Hasan', 'Abdullah', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']
    ['Aisha', 'Abdullah', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']
    '''
    print()

    bubble_sort([4, 1, 3, 9, 7])
    ''' Should print:
    [1, 3, 4, 7, 9]
    [1, 3, 4, 7, 9]
    [1, 3, 4, 7, 9]
    [1, 3, 4, 7, 9]
    '''
    print()

    bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    ''' Should print:
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]
    [8, 7, 6, 5, 4, 3, 2, 1, 9, 10]
    [7, 6, 5, 4, 3, 2, 1, 8, 9, 10]
    [6, 5, 4, 3, 2, 1, 7, 8, 9, 10]
    [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
    [4, 3, 2, 1, 5, 6, 7, 8, 9, 10]
    [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]
    [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    '''
    print()

    bubble_sort([12, 8, -6, 2, 4, 5, 3, 7, 4, 2])
    ''' Should print:
    [8, -6, 2, 4, 5, 3, 7, 4, 2, 12]
    [-6, 2, 4, 5, 3, 7, 4, 2, 8, 12]
    [-6, 2, 4, 3, 5, 4, 2, 7, 8, 12]
    [-6, 2, 3, 4, 4, 2, 5, 7, 8, 12]
    [-6, 2, 3, 4, 2, 4, 5, 7, 8, 12]
    [-6, 2, 3, 2, 4, 4, 5, 7, 8, 12]
    [-6, 2, 2, 3, 4, 4, 5, 7, 8, 12]
    [-6, 2, 2, 3, 4, 4, 5, 7, 8, 12]
    [-6, 2, 2, 3, 4, 4, 5, 7, 8, 12]
    '''
    print()

    bubble_sort(['FunForFun', 'Practice.FunForFun', 'FunforFun'])
    ''' Should print:
    ['FunForFun', 'FunforFun', 'Practice.FunForFun']
    ['FunForFun', 'FunforFun', 'Practice.FunForFun']
    '''
    print()

    bubble_sort([37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54])
    ''' Should print:
    [23, 0, 17, 12, 37, 31, 46, 72, 88, 54, 100]
    [0, 17, 12, 23, 31, 37, 46, 72, 54, 88, 100]
    [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]
    [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]
    [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]
    [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]
    [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]
    [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]
    [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]
    [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]
    '''
    print()

    bubble_sort([2])
    ''' Should print:
    [2]
    '''
    

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q3.py