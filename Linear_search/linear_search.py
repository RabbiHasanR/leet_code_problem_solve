def linear_search(L,x):
    for i in range(len(L)):
        if L[i] == x:
            return i
    return -1

L = [8,2,5,8,0,1,4]
print(linear_search(L,10))
