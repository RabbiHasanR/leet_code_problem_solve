# selection sort algorithm
# L = [10,5,2,8,7] sort acending order using selection sort

# step 1: here smallest number is 2.and first number is 10.so swap index with number 2 and number 10
# then list look like is:
# [10,5,2,8,7] -> [2,5,10,8,7]

# step 2: now we know list first item is smallest number . so find smallest number from the rest numbers [5,10,8,7]
# and smallest number is 5.since 5 already in first item so no need to swap.
# now list look like is:
# [2,5,10,8,7] -> [2,5,10,8,7] 

# step 3: now we know list first two number is already sort in acending order. so find smallest number from then rest of 
# number [10,8,7] and smallest number is 7. and first number is 10. swap index with number 7 and number 10
# then list look like is:
# [2,5,10,8,7] -> [2,5,7,8,10]

# step 4: now rest of numbers [8,10] smallest number is 8. since 8 alreay in first position so no need to swap index between 8 and 10
# now list look like is:
# [2,5,7,810] -> [2,5,7,8,10]
# and now list sort in acending order


# here L is list of numbers and n is list length
# step 1: i = 0
# step 2: if i >= n-1 go to step 11 else go to step 3
# step 3: index_min = i
# step 4: j = i + 1
# step 5: if j >= n go to step 9 else go to step 6
# step 6: if L[j] < L[index_min] go to step 7 else go to step 4
# step 7: index_min = j
# step 8: increase j = j + 1 go to step 5
# step 9: if index_min not equal i then L[i] and L[index_min] value swap
# step 10: increase i = i + 1 go to step 2
# step 11: L array value sort in acending order


# selection sort implementation for acending order:

def selection_sort_asc(L):
    n = len(L)
    for i in range(0, n-1):
        index_min = i
        for j in range(i+1, n):
            if L[j] < L[index_min]:
                index_min = j
        if index_min != i:
            L[i],L[index_min] = L[index_min], L[i]
    return L

def selection_sort_dsc(L):
    n = len(L)
    for i in range(0, n-1):
        index_max = i
        for j in range(i+1,n):
            if L[j] > L[index_max]:
                index_max = j
        if index_max != i:
            L[i], L[index_max] = L[index_max], L[i]

    return L

L = [2,5,7,8,10]

print(selection_sort_asc(L))
print(selection_sort_dsc(L))
