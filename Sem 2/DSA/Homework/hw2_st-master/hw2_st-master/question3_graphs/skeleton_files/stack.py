from listADT import *


def is_empty(lst):
    return IsEmpty(lst)


def push(lst, item):
    if not IsFull(lst):
        Insert(lst, NumberOfElements(lst), item)
    else:
        print("Stack is full")


def pop(lst):
    if IsFull(lst):
        print("Stack is full")
    else:
        x = top(lst)
        Remove(lst, NumberOfElements(lst)-1)
        return x


def top(lst):
    return Get(lst, NumberOfElements(lst)-1)
