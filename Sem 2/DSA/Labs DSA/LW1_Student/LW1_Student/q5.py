def update_record(employee_records, ID, record_title, data):
    """
    Updates an employee record.

    Parameters:
    employee_records (list): List of tuples (ID, Position, Salary, Experience).
    ID (int): Employee ID.
    record_title (str): Field to update ("Position", "Salary", "Experience").
    data (str or int): New data.

    Returns:
    str: Message ("Record updated", "ID cannot be updated", "Record not found").
    """

    # WRITE YOUR CODE HERE
    # for i in employee_records:
    #     if i[0]==ID:
    #         flag=True
    #         if record_title=="ID":
    #             return "ID cannot be updated"
    #         if record_title=="Position":






    f=False
    if record_title=="ID":
        return "ID cannot be updated"
    for i in range(len(employee_records)):
        a=list(employee_records[i])
        
        if a[0]==ID:
            f=True
            if record_title=="Position":
                a[1]=data
                employee_records[i]=tuple(a)
                return 'Record updated'
            elif record_title=="Salary":
                a[2]=int(data)
                employee_records[i]=tuple(a)
                return 'Record updated'
            elif record_title=="Experience":
                a[3]=int(data)
                employee_records[i]=tuple(a)
                return 'Record updated'
    

    if f==False:
        return "Record not found"
            
        



#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    employee_records = [
        ('E001', 'Manager', 80000, 5), 
        ('E002', 'Developer', 60000, 2), 
        ('E003', 'Analyst', 50000, 1), 
        ('E004', 'Designer', 70000, 3)
        ]

    print(update_record(employee_records, 'E001', 'ID', 'E005'))
    # Should print: 'ID cannot be updated'
    print(employee_records)
    # Should print: [
    #   ('E001', 'Manager', 80000, 5), 
    #   ('E002', 'Developer', 60000, 2), 
    #   ('E003', 'Analyst', 50000, 1), 
    #   ('E004', 'Designer', 70000, 3)
    #   ]

    print(update_record(employee_records, 'E001', 'Position', 'Senior Manager'))
    # Should print: 'Record updated'
    print(employee_records)
    # Should print: [
    #   ('E001', 'Senior Manager', 80000, 5), 
    #   ('E002', 'Developer', 60000, 2), 
    #   ('E003', 'Analyst', 50000, 1), 
    #   ('E004', 'Designer', 70000, 3)
    #   ]

    employee_records = [
        ('E001', 'Manager', 80000, 5), 
        ('E002', 'Developer', 60000, 2), 
        ('E003', 'Analyst', 50000, 1), 
        ('E004', 'Designer', 70000, 3)
        ]
    print(update_record(employee_records, 'E005', 'Salary', 55000))
    # Should print: 'Record not found'
    print(employee_records)
    # Should print: [
    #   ('E001', 'Manager', 80000, 5), 
    #   ('E002', 'Developer', 60000, 2), 
    #   ('E003', 'Analyst', 50000, 1), 
    #   ('E004', 'Designer', 70000, 3)
    #   ]
    
    print(update_record(employee_records, 'E002', 'Position', 'Senior Developer'))
    # Should print: 'Record updated'
    print(employee_records)
    # Should print: [
    #   ('E001', 'Manager', 80000, 5), 
    #   ('E002', 'Senior Developer', 60000, 2), 
    #   ('E003', 'Analyst', 50000, 1), 
    #   ('E004', 'Designer', 70000, 3)
    #   ] 


    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q5.py