def stack_initialize(size):
    return {
        'size': size,
        'data':[None]*size,
        'top': -1
    }
stack=stack_initialize(4)
def is_empty(stack):
    if stack['top']==-1:
        return True
    return False

def is_full(stack):
    if stack['top']==stack['size']-1:
        return True
    return False

print(is_empty(stack))

def pust(e, stack):
    if is_full(stack):
        return "Stack is full."
    stack['data'][stack['top']+1]=e
    stack['top']+=1
    return stack

print(pust('hello',stack))
print(pust("bye",stack))


def pop(stack):
    if is_empty(stack):
        return "stack is empty"
    a=stack["data"][stack["top"]]
    stack["data"][stack["top"]]=None
    stack["top"]-=1
    return stack,a

print(pop(stack))
print(pust("bye",stack))
print(pust("bye",stack))
print(pust("bye",stack))
# import listadt

def create_stack(size):
    return stack_initialize(size)

print(create_stack(4))


