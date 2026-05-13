def Initialize(n):
    """
    Create and return a new list of size n,
    with all elements initialized to None.

    Parameters:
    - n (int): The size of the list.

    Returns:
    list: A new list with n elements, all set to None.
    """
    return [None] * n


def Get(list, index):
    """
    Retrieve the element at the specified index in the list.

    Parameters:
    - list (list): The list to retrieve the element from.
    - index (int): The index of the element to retrieve.

    Returns:
    The element at the specified index in the list.
    """
    return list[index]


def Set(list, index, value):
    """
    Set the element at the specified index in the list to the given value.

    Parameters:
    - list (list): The list to modify.
    - index (int): The index at which to set the value.
    - value: The value to set at the specified index.

    Returns:
    None
    """
    list[index] = value


def Size(list):
    """
    Get the size of the list.

    Parameters:
    - list (list): The list to determine the size of.

    Returns:
    int: The size of the list.
    """
    size = 0
    for _ in list:
        size += 1
    return size


def NumberOfElements(list):
    """
    Get the number of elements in the list.

    Parameters:
    - list (list): The list to count elements in.

    Returns:
    int: The number of elements in the list.
    """
    number = 0
    for element in list:
        if element is None:
            return number
        else:
            number += 1
    return number


def IsEmpty(list):
    """
    Check if the list is empty.

    Parameters:
    - list (list): The list to check.

    Returns:
    bool: True if the list is empty, False otherwise.
    """
    return list[0] == None


def IsFull(list):
    """
    Check if the list is full.

    Parameters:
    - list (list): The list to check.

    Returns:
    bool: True if the list is full, False otherwise.
    """
    return list[Size(list) - 1] != None


def Insert(list, index, value):
    """
    Insert the given value at the specified index in the list, shifting existing elements to make room.

    Parameters:
    - list (list): The list to insert the value into.
    - index (int): The index at which to insert the value.
    - value: The value to insert into the list.

    Returns:
    str: A string indicating the result of the insertion.
        - "List is full" if the list is already full and no insertion is possible.
        - "Invalid Index" if the provided index is outside the valid range.
        - "Element inserted successfully" if the insertion is successful.
    """
    if IsFull(list):
        return "List is full"
    l = NumberOfElements(list)
    if index < 0 or index > l:
        return "Invalid Index"
    for j in range(l, index, -1):
        list[j] = list[j - 1]
    Set(list, index, value)
    return "Element inserted successfully"


def Remove(list, index):
    """
    Remove the element at the specified index in the list, shifting subsequent elements to fill the gap.

    Parameters:
    - list (list): The list from which to remove an element.
    - index (int): The index of the element to be removed.

    Returns:
    str: A string indicating the result of the removal.
         - "List is empty" if the list is empty, and no removal is possible.
         - "Invalid Index" if the provided index is outside the valid range.
         - "Element removed successfully" if the removal is successful.
    """
    if IsEmpty(list):
        return "List is empty"

    l = NumberOfElements(list)

    if index < 0 or index >= l:
        return "Invalid Index"

    # Shift subsequent elements to fill the gap left by the removed element
    for j in range(index, l - 1):
        list[j] = list[j + 1]

    # Set the last element to None to remove the duplicate value
    list[l - 1] = None

    return "Element removed successfully"


def InsertAtStart(list, element):
    """
    Insert the given element at the beginning of the list, shifting existing elements to make room.

    Parameters:
    - list (list): The list to insert the element into.
    - element: The element to insert at the start of the list.

    Returns:
    str: A string indicating the result of the insertion.
         - "List is full" if the list is already full and no insertion is possible.
         - "Element inserted successfully" if the insertion is successful.
    """
    return Insert(list, 0, element)


def RemoveFromStart(list):
    """
    Remove the element at the beginning of the list, shifting subsequent elements to fill the gap.

    Parameters:
    - list (list): The list from which to remove an element.

    Returns:
    str: A string indicating the result of the removal.
         - "List is empty" if the list is empty, and no removal is possible.
         - "Element removed successfully" if the removal is successful.
    """
    return Remove(list, 0)
