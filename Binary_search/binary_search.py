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


L = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(L,11))
