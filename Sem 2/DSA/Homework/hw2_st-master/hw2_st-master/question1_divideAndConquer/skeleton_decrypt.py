# Decrypt the data using the logic of the Karatsuba algorithm.
# Args:
#   data: List of list consisting of leaves
# Returns:
#   A tuple containing the original two numbers.
def reverse_karatsuba(data, level=0) -> tuple:
    if type(data)==list:
        data[0]=reverse_karatsuba(data[0],level)
        data[2]=reverse_karatsuba(data[2],level)
        if type(data[0])==tuple and type(data[2])==tuple:
            level+=1
            a=str(data[2][0])+str(data[0][0])
            a=int(a)
            b=str(data[2][1])+str(data[0][1])
            b=int(b)
            c=data[0][2]*((10)**(level))
            return (a,b,c)
        else:
            return data
    return data

################################################################
    # if type(data[0])==tuple and type(data[2])==tuple:
    #     a=data[0][0]+(data[2][0]*10)
    #     b=data[0][1]+(data[2][1]*10)
    #     c=data[0][2]*10
    #     return (a,b,c)
    # # if type(data[0])!=tuple and type(data[2])!=tuple:
    # #     data[0]=reverse_karatsuba(data[0], level=0)
    # #     data[2]=reverse_karatsuba(data[2],level=0)
    # if type(data[0])!=tuple:
    #     data[0]= reverse_karatsuba(data[0], level=0)
    # if type(data[2])!=tuple:
    #     data[2]= reverse_karatsuba(data[2],level=0)
#################################################################




# This function reads data from a specified file and decrypt data using the logic of the Karatsuba algorithm.
# Args:
#   filename: The name of the file containing input data.
# Returns:
#   A list of tuples, each tuple representing coordinates (x, y).
def main(filename) -> list[tuple[int, int]]:
    lst=[]
    with open(filename) as f:
        lines=f.readlines()
    num=int(lines[0])
    data=()
    for i in range(1,num+1):
        first=eval(lines[i])
        data=data+(first,)
    for i in data:
        a=reverse_karatsuba(i,level=0)
        a=(a[0:3],)+(a[0]*a[1]*a[2],)
        lst.append(a)
    return lst

print(main('hw2_st-master\question1_divideAndConquer\input_decrypt.txt'))


