def insertion_sort(arr):
    """
    Sorts a list in ascending order using Insertion Sort.
    
    Iteratively inserts each element into the sorted portion of the list, 
    printing the list after each insertion.

    Parameters:
    arr (list): List of elements (numbers or strings) to sort.

    Returns:
    None: Sorts the list in place and prints the state after each iteration.

    Steps:
        Step 1 => If it is the first element, it is already sorted.
        Step 2 => Pick next element
        Step 3 => Compare with all elements in the sorted sub-list
        Step 4 => Shift all the elements in the sorted sub-list that is greater than the value to be sorted
        Step 5 => Insert the value
        Step 6 => Repeat until list is sorted
    """

    
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
        print(arr)




#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    insertion_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])
    ''' Should print:
    [26, 54, 93, 17, 77, 31, 44, 55, 20]
    [26, 54, 93, 17, 77, 31, 44, 55, 20]
    [17, 26, 54, 93, 77, 31, 44, 55, 20]
    [17, 26, 54, 77, 93, 31, 44, 55, 20]
    [17, 26, 31, 54, 77, 93, 44, 55, 20]
    [17, 26, 31, 44, 54, 77, 93, 55, 20]
    [17, 26, 31, 44, 54, 55, 77, 93, 20]
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    '''
    print()

    insertion_sort(['Aisha', 'Nadia', 'Waqar', 'Saleha', 'Hasan', 'Shahid', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj'])
    ''' Should print:
    ['Aisha', 'Nadia', 'Waqar', 'Saleha', 'Hasan', 'Shahid', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj']
    ['Aisha', 'Nadia', 'Waqar', 'Saleha', 'Hasan', 'Shahid', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj']
    ['Aisha', 'Nadia', 'Saleha', 'Waqar', 'Hasan', 'Shahid', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj']
    ['Aisha', 'Hasan', 'Nadia', 'Saleha', 'Waqar', 'Shahid', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj']
    ['Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shahid', 'Waqar', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj']
    ['Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Waqar', 'Abdullah', 'Umair', 'Taj']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Waqar', 'Umair', 'Taj']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Umair', 'Waqar', 'Taj']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']
    '''
    print()

    insertion_sort([4, 1, 3, 9, 7])
    ''' Should print:
    [1, 4, 3, 9, 7]
    [1, 3, 4, 9, 7]
    [1, 3, 4, 9, 7]
    [1, 3, 4, 7, 9]
    '''
    print()

    insertion_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    ''' Should print:
    [9, 10, 8, 7, 6, 5, 4, 3, 2, 1]
    [8, 9, 10, 7, 6, 5, 4, 3, 2, 1]
    [7, 8, 9, 10, 6, 5, 4, 3, 2, 1]
    [6, 7, 8, 9, 10, 5, 4, 3, 2, 1]
    [5, 6, 7, 8, 9, 10, 4, 3, 2, 1]
    [4, 5, 6, 7, 8, 9, 10, 3, 2, 1]
    [3, 4, 5, 6, 7, 8, 9, 10, 2, 1]
    [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    '''

    insertion_sort([12, 8, -6, 2, 4, 5, 3, 7, 4, 2])
    ''' Should print:
    [8, 12, -6, 2, 4, 5, 3, 7, 4, 2]
    [-6, 8, 12, 2, 4, 5, 3, 7, 4, 2]
    [-6, 2, 8, 12, 4, 5, 3, 7, 4, 2]
    [-6, 2, 4, 8, 12, 5, 3, 7, 4, 2]
    [-6, 2, 4, 5, 8, 12, 3, 7, 4, 2]
    [-6, 2, 3, 4, 5, 8, 12, 7, 4, 2]
    [-6, 2, 3, 4, 5, 7, 8, 12, 4, 2]
    [-6, 2, 3, 4, 4, 5, 7, 8, 12, 2]
    [-6, 2, 2, 3, 4, 4, 5, 7, 8, 12]
    '''
    print()

    insertion_sort(['FunForFun', 'Practice.FunForFun', 'FunforFun'])
    ''' Should print:
    ['FunForFun', 'Practice.FunForFun', 'FunforFun']
    ['FunForFun', 'FunforFun', 'Practice.FunForFun']
    '''
    print()

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q2.py