import math

def total_distance(movements):
    """
    Computes the robot's distance from the origin after moving according to the instructions.

    Parameters:
    instructions (list of tuples): List of ('direction', distance) pairs.

    Returns:
    int: Rounded-up Euclidean distance from the origin.
    """

    # WRITE YOUR CODE HERE
    a=0
    b=0
    c=0
    d=0
    for distance in movements:
        if distance[0]=='UP':
            a=a+int(distance[1])
        if distance[0]=='RIGHT':
            b=b+int(distance[1])
        if distance[0]=='LEFT':
            c=c+int(distance[1])
        if distance[0]=='DOWN':
            d=d+int(distance[1])
    x=abs(a-d)
    y=abs(b-c)
    total=(x*x+y*y)**(1/2)
    o=math.ceil(total)
    return o


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    print(total_distance([
        ('UP', 5), 
        ('DOWN', 3), 
        ('LEFT', 3), 
        ('RIGHT', 2)
    ]))
    # Should print 3

    print(total_distance([
        ('RIGHT', 1), 
        ('DOWN', 0), 
        ('LEFT', -2),
        ('DOWN', -4)
    ]))
    # Should print 5

    print(total_distance([
        ('UP', 0)
    ]))
    # Should print 0

    print(total_distance([
        ('UP', 33), ('LEFT', -57), ('UP', -14), ('UP', -10), ('UP', -50), 
        ('DOWN', -6), ('RIGHT', 32), ('RIGHT', -16), ('UP', 55), ('LEFT', 33), 
        ('UP', 87), ('RIGHT', -37), ('RIGHT', 23), ('RIGHT', 25), ('UP', 92), 
        ('UP', 0), ('UP', 60), ('DOWN', -69), ('DOWN', 89), ('LEFT', -64), 
        ('UP', -9), ('UP', -71), ('UP', -28), ('UP', -81), ('LEFT', 43), 
        ('RIGHT', 30), ('LEFT', -80), ('DOWN', 66), ('RIGHT', -36), ('RIGHT', 37),
        ('LEFT', -91), ('DOWN', -68), ('UP', 69), ('LEFT', 39), ('LEFT', -99), 
        ('RIGHT', -56), ('LEFT', -40), ('DOWN', 7), ('UP', -61), ('LEFT', -75), 
        ('DOWN', -53), ('RIGHT', -64), ('UP', -37), ('LEFT', 99), ('RIGHT', -5), 
        ('RIGHT', -83), ('DOWN', -55), ('UP', 81), ('LEFT', -18)
    ]))
    # Should print 261

    print(total_distance([
        ('LEFT', -43), ('UP', -62), ('UP', 43), ('DOWN', 60), ('RIGHT', 85), 
        ('DOWN', 70), ('UP', 20), ('LEFT', -96), ('UP', 86), ('DOWN', 2), 
        ('DOWN', -57), ('LEFT', -70), ('DOWN', 4), ('DOWN', -36), ('LEFT', 99), 
        ('UP', 18), ('DOWN', 24), ('DOWN', -18), ('LEFT', 30), ('RIGHT', 43), 
        ('DOWN', 94), ('DOWN', 68), ('RIGHT', 65), ('RIGHT', 71), ('LEFT', 79), 
        ('LEFT', -21), ('LEFT', -99), ('UP', 0), ('UP', 30), ('LEFT', -58), 
        ('LEFT', 59), ('LEFT', 22), ('UP', 35), ('UP', -21), ('LEFT', 87), 
        ('RIGHT', 77), ('UP', 4), ('LEFT', 86), ('UP', -55), ('UP', 57), 
        ('UP', 42), ('DOWN', 15), ('RIGHT', -32), ('DOWN', 4), ('DOWN', 48), 
        ('RIGHT', 37), ('RIGHT', 55), ('DOWN', -67), ('RIGHT', 61), ('RIGHT', -80), 
        ('UP', 65), ('DOWN', -26), ('LEFT', 67), ('LEFT', 40), ('RIGHT', 27), 
        ('UP', 8), ('LEFT', 63), ('UP', -45), ('RIGHT', -96), ('LEFT', 14), 
        ('LEFT', -72), ('UP', 90), ('UP', -51), ('RIGHT', 74), ('UP', -29), 
        ('UP', -27), ('UP', -41), ('RIGHT', 42), ('DOWN', 19), ('RIGHT', 76), 
        ('UP', 33)
    ]))
    # Should print 319



    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q2.py