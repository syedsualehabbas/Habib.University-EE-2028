def createlist(Size):
    return {
        'Size':Size,
        'data':[None]*Size,
        'n':0   #number of elements
    }
def is_full(list):
    if list['Size']==list['n']:
        return False
print(is_full(createlist(4)))