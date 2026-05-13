import math
import copy
def initialize_matrix(n: int) -> list[list[int]]:
    """
    A  function that takes an integer n as an argument and returns a 2D array of size n x n with each cell containing None values.
    """
    return [[0 for _ in range(n)] for _ in range(n)]


def length(arr: list[int]) -> int:
    """
    A function that takes a single-dimensional array, arr, as an argument and returns the count of valid data items in it, i.e., the non-None values.
    """
    count=0
    for i in arr:
        if i!=None:
            count+=1
    return count


def divide_chunks(arr: list[int], chunk_size: int) -> list[list[int]]:
    """
    A fruitful function that takes an array and chunk size as arguments and divides the array into chunks of size k.
    """
    hello=copy.deepcopy(arr)    #as we cannot slice an array, so creating a copy of main array in nested list named hello
    lst=[]
    for i in range(0,len(arr),chunk_size):   #skipping chunksize in each loop because all the left over values will be added in the first chunk
        lst.append(hello[i:chunk_size+i])    #slicing he nested list
    return lst                               #returning the list with chunks
    
def selection_sort(arr: list[int]) -> None:
    """
    A void function that takes an array and sorts it in descending order using the selection sort algorithm.
    This is an in-place function, meaning the original array that was passed as a reference will be updated with the
    sorted values.

    The function should not return anything.
    """

    for i in range(length(arr)):  
        max=i                    #setting up a max value
        for j in range(i+1,length(arr)): #loop running from minimum value till the last
            if arr[j]>arr[max]:
                max=j           #if max value is found change exchange both the values
        arr[max],arr[i]=arr[i],arr[max]


def consolidate(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    A fruitful function that combines two sorted arrays into one sorted array using a two-pointer approach,
    in a descending order.

    The function returns the updated, sorted array
    """
    i=0
    j=0               #using two pointer method so initializing two pointers
    lst=[]           
    while i<length(arr1) and j<length(arr2):  #the loop will run until both of the lists are not empty
        print(lst , i ,j)
        if arr1[i]>arr2[j]:           #if the arr1's top value is greater, add it to the list, else add the value from arr2
            lst.append(arr1[i])
            i+=1
        else:
            lst.append(arr2[j])
            j+=1

    while i<length(arr1):    #if any elements left in any of the list, these two loops will empty them
        lst.append(arr1[i])
        i+=1
    while j<length(arr2):
        lst.append(arr2[j])
        j+=1
    return lst



def fusion_sort(arr: list[int]) -> list[int]:
    """
    A fruitful function that implements the “Fusion Sort” algorithm described above to sort the valid data items
    in a descending order, while preserving the positions of invalid items.

    The function returns the updated, sorted array
    """
    
    none_count=0
    for i in arr:
        if i==None:
            none_count+=1
    
    print(arr)
    chunk_size=math.ceil(math.sqrt(length(arr)))
    print(chunk_size)
    arr=divide_chunks(arr[:length(arr)],chunk_size)
    
    print(arr)
    for i in range(length(arr)):
        selection_sort(arr[i])         #sorts each array chunk one by one
    lst=arr[0]
    for i in range(1,length(arr)):
        lst = consolidate(lst, arr[i])          #join all the arrays into one array main decending order
    for i in range(none_count):
        lst.append(None)
    return lst
    

    



def main(filename) -> list[int]:
    """
    - Take input from the given filename one line at a time
    - Apply fusion sorting algorithm to get the sorted arrays and returns the output, sorted array.
    """
    
    with open(filename) as f:
        lines = f.readlines()
        arr=[]
        for line in lines :
            
            line = line.strip () 
            line=line[1:-1]
            line = line.split (", ") 
            for i in line:
                if i.isnumeric():
                    arr.append(int(i))
                else:
                    arr.append(None)
        
        if length(arr)==0:       #if there is no element in the array, directly return the array, no need to sort
            return arr
        return fusion_sort(arr) #else run the code
               
if __name__ == "__main__":
    main("Inputs/sorting03.txt")

