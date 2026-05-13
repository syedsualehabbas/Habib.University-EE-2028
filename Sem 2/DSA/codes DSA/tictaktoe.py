lst=["A","B","B","A","S"]
target="A"
def binary_search(lst,target):
    l,r=0,len(lst)-1
    while l<=r:
        mid=(l+r)//2
        if lst[mid]==target:
            return mid
        else:
            l=l+1
    return -1

print(binary_search(lst,target))