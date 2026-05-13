
def partitionfunction(lst,low,high):
    pivot = low
    i=low+1
    for j in range(low+1,high+1):
        if lst[j]<=lst[pivot]:
            lst[i],lst[j]=lst[j],lst[i]
            i+=1
    lst[pivot],lst[i-1]=lst[i-1],lst[pivot]
    pivot=i-1
    return pivot
def partitionMidFunction(lst,low,high):
    pivot=(low+high)//2
    lst[low],lst[pivot]=lst[pivot],lst[low]
    return partitionfunction(lst,low,high)
def quick_sort(lst,low,high):
    if low<high:
        part=partitionMidFunction(lst,low,high)
        print(lst)
        quick_sort(lst,low,part-1)
        quick_sort(lst,part+1,high)
        

    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    quick_sort([5, 9, 2, 1, 6, 3, 0], 0, 6)
    ''' Should print:
    [0, 1, 2, 5, 6, 3, 9]
    [0, 1, 3, 5, 2, 6, 9]
    [0, 1, 2, 3, 5, 6, 9]
    [0, 1, 2, 3, 5, 6, 9]
    '''
    
    print()

    quick_sort([21, 36, 11, 9, 6, 42, 39], 0, 6)
    ''' Should print:
    [6, 9, 11, 21, 36, 42, 39]
    [6, 9, 11, 21, 36, 42, 39]
    [6, 9, 11, 21, 36, 42, 39]
    [6, 9, 11, 21, 36, 39, 42]
    '''
    
    print()

    quick_sort([10, 7, 8, 9, 1, 5], 0, 5)
    ''' Should print:
    [5, 7, 1, 8, 10, 9]
    [1, 5, 7, 8, 10, 9]
    [1, 5, 7, 8, 10, 9]
    [1, 5, 7, 8, 9, 10]
    '''
    
    print()

    quick_sort([54, 26, 93, 17, 77, 31, 44, 55, 20], 0, 8)
    ''' Should print:
    [20, 26, 17, 54, 31, 44, 55, 77, 93]
    [44, 26, 17, 20, 31, 54, 55, 77, 93]
    [17, 26, 44, 20, 31, 54, 55, 77, 93]
    [17, 31, 26, 20, 44, 54, 55, 77, 93]
    [17, 20, 26, 31, 44, 54, 55, 77, 93]
    '''
    
    print()

    quick_sort(['Aisha', 'Nadia', 'Waqar', 'Saleha', 'Hasan', 'Shahid', 'Shah Jamal', 'Abdullah', 'Umair', 'Taj'], 0, 9)
    ''' Should print:
    ['Abdullah', 'Aisha', 'Hasan', 'Saleha', 'Nadia', 'Shahid', 'Shah Jamal', 'Waqar', 'Umair', 'Taj']
    ['Abdullah', 'Aisha', 'Hasan', 'Saleha', 'Nadia', 'Shahid', 'Shah Jamal', 'Waqar', 'Umair', 'Taj']
    ['Abdullah', 'Aisha', 'Hasan', 'Saleha', 'Nadia', 'Shah Jamal', 'Shahid', 'Waqar', 'Umair', 'Taj']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Waqar', 'Umair', 'Taj']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Taj', 'Shahid', 'Umair', 'Waqar']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']
    ['Abdullah', 'Aisha', 'Hasan', 'Nadia', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar']
    '''
    
    print()

    quick_sort([4, 1, 3, 9, 7], 0, 4)
    ''' Should print:
    [1, 3, 4, 9, 7]
    [1, 3, 7, 4, 9]
    [1, 3, 4, 7, 9]
    '''
    
    print()

    quick_sort([12, 8, -6, 2, 4, 5, 3, 7, 4, 2], 0, 9)
    ''' Should print:
    [2, -6, 2, 3, 4, 4, 8, 7, 12, 5]
    [2, -6, 2, 3, 4, 4, 8, 7, 12, 5]
    [-6, 2, 2, 3, 4, 4, 8, 7, 12, 5]
    [-6, 2, 2, 3, 4, 4, 8, 7, 12, 5]
    [-6, 2, 2, 3, 4, 4, 5, 7, 12, 8]
    [-6, 2, 2, 3, 4, 4, 5, 7, 8, 12]
    '''
    
    print()

    quick_sort(['FunForFun', 'Practice.FunForFun', 'FunforFun'], 0, 2)
    ''' Should print:
    ['FunforFun', 'FunForFun', 'Practice.FunForFun']
    ['FunForFun', 'FunforFun', 'Practice.FunForFun']
    '''
    
    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q1.py