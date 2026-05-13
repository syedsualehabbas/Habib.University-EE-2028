# This file contains helper functions for:
# 1. ListADT
# 2. Stacks
# 3. Queues
# 4. GraphADT

# -------------------------ListADT-------------------------
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

# -------------------------Stacks-------------------------
def push(lst, item):
    Insert(lst, NumberOfElements(lst), item)

def pop(lst):
    last_index = NumberOfElements(lst) - 1 
    x = Get(lst, last_index)
    Remove(lst, last_index)
    return x

def top(lst):
    return Get(lst, NumberOfElements(lst)-1)

def is_empty(lst):
    return IsEmpty(lst)

# -------------------------Queues-------------------------
def enQueue(lst, item):
    Insert(lst, NumberOfElements(lst), item)

def deQueue(lst):
    x = front(lst)
    RemoveFromStart(lst)
    return x

def front(lst):
    return Get(lst, 0)

def is_empty(lst):
    return IsEmpty(lst)

# -------------------------GraphADT-------------------------
def addNodes(G, nodes):
    for i in nodes:
        G[i] = []

def addEdges(G, edges, directed=False):
    for i, j, k in edges:
        G[i].append((j, k))
        if directed==False:
            G[j].append((i, k))

def displayGraph(G):
    print(G)

def listOfNodes(G):
    return list(G.keys())

def listOfEdges(G, directed=False):
    edges_lst = []
    for key, value in G.items():
        for v, w in value:
            if directed == False:
                if (key, v, w) not in edges_lst and (v, key, w) not in edges_lst:
                    edges_lst.append((key, v, w))
            else:
                if (key, v, w) not in edges_lst:
                    edges_lst.append((key, v, w))
    return edges_lst

def getNeighbors(G, nodes):
    lst = []
    for i in G[nodes]:
        lst.append(i[0])
    return lst

def removeNode(G, node):
    del G[node]
    for a in G.values():
        for i, j in a:
            if i == node:
                a.remove((i, j))  

def removeNodes(G, nodes):
    for i in nodes:
        removeNode(G, i)


import math
def getNearestNeighbor(G, node):
    low = (math.inf, math.inf)
    if G[node]==[]:
        return None
    for i, j in G[node]:
        if j < low[1]:
            low = (i, j)
    return low[0]