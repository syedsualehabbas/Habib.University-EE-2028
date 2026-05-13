# import matplotlib.pyplot as plt   # (OPTIONAL) Uncomment this if you have installed matplotlib.
import copy
def row_counter(image):
    count=0
    for i in range(len(image)):
        count+=1
    return count


def init_matrix(rows: int, cols: int) -> list[list[int]]:
    """
    Creates a 2D array (matrix) based on the input rows and columns.

    Parameter(s):
    - rows (int): Specifies the rows of the 2D array to be created.
    - cols (int): Specifies the columns of the 2D array to be created.

    Returns:
    - 2D array (int): This is the 2D array that is created using the input rows and cols.
    """
    return [[0 for _ in range(cols)] for _ in range(rows)]


def detect_edges(
    image: list[list[int]], filter: list[list[int]], stride: int
) -> list[list[int]]:
    """
    Detects edges in the input image by convolving the image with the filter.

    Parameter(s):
    - image (2D array): This is the input image that will be processed.
    - filter (2D array): This is the filter that will be used to process the input image.
    - stride (int): Provides the offset for the filter during the convolution process.

    Returns:
    - processed_image (2D array): This is the processed image obtained after performing convolution (will contain edges).
    """
    rows=len(image)      #getting rows and cols of image
    cols=len(image[0])
    a=row_counter(filter)
    # print(a)
    # lst=init_matrix(rows, cols)  #creating an temporary array to store values of image (this array's size is bigger than image, so that filter doens't go out)
    # rows_lst=len(lst)
    # cols_lst=len(lst[0])   #getting rows and cos of lst
    filter_extreme=(a//2)
    # for i in range(filter_extreme,rows_lst-filter_extreme):
    #     for j in range(filter_extreme,cols_lst-filter_extreme):
    #         lst[i][j]=image[i][j]  #inserting values from image to our new array, with size greater than image
    # return (filter_extreme)
    new_image=init_matrix(rows-2*(filter_extreme),cols-2*(filter_extreme))   #creating another array for calculations and final return
    for i in range(filter_extreme,rows-filter_extreme):
        for j in range(filter_extreme,cols-filter_extreme,stride):
            sum=0
            b=-filter_extreme  #calculating the difference in extreme row and filter after every loop
            for i_filter in range(a):
                c=-filter_extreme  #calculating the difference in extreme column after every loop
                for j_filter in range(a):
                    sum+= filter[i_filter][j_filter]*image[i+b][j+c]  
                    c+=1
                b+=1
            new_image[i-filter_extreme][j-filter_extreme]=abs(sum)
    return new_image



################################################################

#FOR THE IMAGE DIRECTLY CALLED INTO DETECT_EDGES:- (NOT WORKING)
"""
*********************************************************************************************************
            # for i_filter in range(filter_size):
            #     for j_filter in range(filter_size):
            #         print(sum)
            #         if i-i_filter<0 or j-j_filter<0 :
            #             sum+=0
            #         else:
            #             sum+=abs(filter[i_filter][j_filter]*image[i_filter-i][j_filter-j])
            # new_image[i][j]=sum
            # sum=0
********************************************************************************************************
"""               
##FOR THE VIRTUAL IMAGE I MADE OF SIZE (ROW+FILTER_SIZE//2) AND (COLUMS+FILTER_SIZE//2):- (NOT WORKING)
"""
********************************************************************************************************

    # for i_image in range(1+filter_size//2,len(image)-filter_size//2):
    #     for j_image in range(filter_size//2,len(image[0])-filter_size//2,stride):
    #         sum=0
    #         for i_filter in range(filter_size):
    #             for j_filter in range(filter_size):
                #     sum+=abs((filter[i_filter][j_filter])*(image[i_filter][j_filter]))
                # new_image[i_image][j_image]=sum
            
    # return new_image
********************************************************************************************************
"""
def main(filename: str) -> list[list[int]]:
    #I did not remove anything that i tried in this question, i've comment down everything, so you ca see how many times i tried this ;)

    with open(filename) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
        stride = int(lines[0])
        rows, columns = list(map(int, lines[1].split()))
        
        image=[]
        for i in range(2, 2+rows):
            image.append(list(map(int,lines[i].split())))

    # orignal_image=copy.deepcopy(image)
    # print(image)
    # print(orignal_image)

    filter_size=int(lines[rows+2][0])
    # print(filter_size)
    vertical_filter=[]
    for i in range(rows+3,rows+3+filter_size):
        vertical_filter.append(list(map(int,lines[i].split())))
    # print(vertical_filter)
    horizontal_filter=[]
    for i in range(rows+3+filter_size,len(lines)):
        horizontal_filter.append(list(map(int,lines[i].split())))
    # print(horizontal_filter)
    # print(image)
    # print(vertical_filter)
    # print(horizontal_filter)
    # print(stride)

#creating a virtual image to work on so that filter doesnt exceed the lengths
    for i in range(rows):
        for j in range(filter_size//2):
            image[i].insert(0,0)
            image[i].append(0)
    for i in range(filter_size//2):
        a=[0]*(columns+2*(filter_size//2))
    for i in range(filter_size//2):
        image.insert(0,a)
        image.append(a)

    # print(vertical_filter)

    
    a=detect_edges(image,vertical_filter,stride)
    # print(a)
    b=detect_edges(image,horizontal_filter,stride)
    # print(b)
    finalarray=init_matrix(rows,columns)
    for i in range(len(finalarray)):
        for j in range(len(finalarray[0])):
            finalarray[i][j]=a[i][j]+b[i][j]
            # print(finalarray)
    # return finalarray
    print(finalarray)

"""  #DOES WORK
******************************************************************************
"""
    
# (
#         "inputs/test1.txt",
#         [
#             [0, 0, 0, 0, 0, 0],
#             [510, 765, 765, 765, 765, 510],
#             [765, 1020, 765, 765, 1020, 765],
#             [765, 1020, 765, 765, 1020, 765],
#             [510, 765, 765, 765, 765, 510],
#         ],
#     ),
#     (
#         "inputs/test2.txt",
#         [
#             [0, 0, 0, 0, 0, 0],
#             [510, 0, 765, 0, 765, 0],
#             [765, 0, 765, 0, 1020, 0],
#             [765, 0, 765, 0, 1020, 0],
#             [510, 0, 765, 0, 765, 0],
#         ],
#     ),
#     (
#         "inputs/test3.txt",
#         [
#             [1020, 1275, 1275, 1275, 1275, 1020],
#             [2040, 2550, 2550, 2550, 2550, 2040],
#             [1530, 1785, 1530, 1530, 1785, 1530],
#             [1530, 1785, 1530, 1530, 1785, 1530],
#             [2040, 2550, 2550, 2550, 2550, 2040],
#         ],
#     ),
#     (
#         "inputs/test4.txt",
#         [
#             [1020, 0, 0, 0, 1275, 0],
#             [2040, 0, 0, 0, 2550, 0],
#             [1530, 0, 0, 0, 1785, 0],
#             [1530, 0, 0, 0, 1785, 0],
#             [2040, 0, 0, 0, 2550, 0],
#         ],
#     ),
    
if __name__ == "__main__":
    main("C:/Users/Administrator/Desktop/sem 2/DSA/Homework/hw1_st-main/hw1_st-main/matrix/inputs/test1.txt")