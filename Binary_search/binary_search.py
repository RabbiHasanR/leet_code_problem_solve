def binary_search(L,x):
    n = len(L)
    left = 0
    right = n-1
    while left <= right:
        mid = (left + right) // 2
        if L[mid] == x:
            return mid
        elif x > L[mid]:
            left = mid + 1
        else:
            right = mid -1
    return -1


# binary search with recursive function

def binary_recursive_search(l,left,right,x):
    if left > right:
        return -1
    mid = (left + right) // 2
    if l[mid] == x:
        return mid
    
    if l[mid] < x:
        return binary_recursive_search(l,mid+1,right,x)
    else:
        return binary_recursive_search(l,left,mid-1,x)

L = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(L,11))
print(binary_recursive_search(L,0,len(L)-1,5))


