# Tip: Import and use created Stack functions from q1. (from q1 import *)
from q1 import *
from q3 import *
def Infix_to_Postfix(expression):
    """
    Converts an infix expression to a postfix expression.

    Parameters:
    expression (str): The input infix expression as a string.

    Returns:
    str: The corresponding postfix expression as a string.

    Note:
        1. Only Stack ADT Operations are to be used in your implementation:
            ( Initialize() , push() , pop() , top() and is_empty() ).
        2. Use Stack ADT operations on the Stack only.
        3. Infix to Postfix Conversion Simulator: 
            https://raj457036.github.io/Simple-Tools/prefixAndPostfixConvertor.html
    """
    
    # WRITE YOUR CODE HERE
    op_stk=Initialize(len(expression))
    lst=[]
    a=expression.split()
    for i in a:
        if i.isalpha():
            lst.append(i)
        elif i == "(":
            push(op_stk,i)
        elif i==")":
            if is_empty(op_stk)==False:
                while top(op_stk)!="(":
                    lst.append(pop(op_stk))
                    if is_empty(op_stk)==True:
                        break
            pop(op_stk)
        elif i in "*/":
            if is_empty(op_stk)==False:
                while  top(op_stk) in "*/": 
                    lst.append(pop(op_stk))
                    if is_empty(op_stk)==True:
                        break
            push(op_stk,i)
        elif i in "+-":
            if is_empty(op_stk)==False:
                while top(op_stk) in "+-*/" and top(op_stk)!="(":
                    lst.append(pop(op_stk))
                    if is_empty(op_stk)==True:
                        break
            push(op_stk,i)
    while is_empty(op_stk)==False:
        lst.append(pop(op_stk))
    return " ".join(lst)
        


        
        



        



                
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print(Infix_to_Postfix("( A + B ) * ( C + D )"))
    # Should print "A B + C D + *"

    print(Infix_to_Postfix("A * B + C * D"))
    # Should print "A B * C D * +"

    print(Infix_to_Postfix("A * B + C"))
    # Should print "A B * C +"

    print(Infix_to_Postfix("A * ( B + C )"))
    # Should print "A B C + *"

    print(Infix_to_Postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    # Should print "A B + C * D E - F G + * -"

    print(Infix_to_Postfix("( ( ( A + B ) * C ) - ( ( D - E ) * ( F + G ) ) )"))
    # Should print: "A B + C * D E - F G + * -"

    print(Infix_to_Postfix("( P + Q ) * ( M - N )"))
    # Should print: "P Q + M N - *"

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q5.py