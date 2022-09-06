# bubble sort acending order explanation

# let , L = [3,1,7,6,2]

# step 1: compare first two number 3 and 1. if first number is greater then 1 then swap two number.
# after swap :
# [3,1,7,6,2] -> [1,3,7,6,2]

# step 2: compare 3 and 7 . if first number is greater then 7 then swap two number or not swap
# after swap:
# [1,3,7,6,2] -> [1,3,7,6,2]

# step 3: compare 7 and 6. if first number is greate then 6 then swap two numbers or not swap
# after swap:
# [1,3,7,6,2] -> [1,3,6,7,2]

# step 4: compare 7 and 2 .if first number is greater then 2 then swap two numbers or not swap
# after swap:
# [1,3,6,7,2] -> [1,3,6,2,7]

# step 5: after step 4 we know last number is greater then every number. so now sorting rest of numbers with out last number 7.
# compare 1 and 3. if firest number is greater then 3 then swap two number or not swap
# after swap:
# [1,3,6,2,7] -> [1,3,6,2,7]

# step 6: compare 3 and 6 .if first number is greater then 6 then swap two numbers or not swap
# after swap:
# [1,3,6,2,7] -> [1,3,6,2,7]

# step 7: compare 6 and 2.if first number is greater then 2 then swap two numbers or not swap
# after swap:
# [1,3,6,2,7] -> [1,3,2,6,7]
# after then we confirm it greatest 2 numbers 6,7 is last two number.now sorting rest of number without 6 and 7

# step 8: compare 1 and 3.if first number is greater then 3 then swap two numbers or not swap
# after swap:
# [1,3,2,6,7] -> [1,3,2,6,7]

# step 9: compare 3 and 2. if first number is greater then 2 then swap two numbers or not swap
# after swap:
# [1,3,2,6,7] -> [1,2,3,6,7]
# after then we confirm it greatest 3 numbers 3,6,7 is last three numbers.now sorting rest of number without3, 6 and 7

# step 10: compare 1 and 2. if first number is greater then 2 then swap two numbers or not swap
# after swap:
# [1,2,3,6,7] -> [1,2,3,6,7]
# after then we confirm it greatest 4 numbers 2,3,6,7 is last four numbers.now sorting rest of number without 2,3, 6 and 7

# step 11: now here only one number 1 is left.so we confirm it our list is sorted



# bubble sort algorithm for acending order

# step1: increase i value 0 to n(length of list) and go to step 2.if i >=n then go to step 4
# step2: increase j value 0 to n-i-1 ang go to step 3.if j >= n-i-1 then go to step 1
# step3: check L[j] > L[j+1]. if true then swap else go to step 2
# step4: now list L is sorted acending order

# time: O(n^2)
# space: O(1)


def bubble_sort_asc(L):
    n = len(L)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
            # print(L) // print list after finish every step
    return L

def bubble_sort_dsc(L):
    n = len(L)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if L[j] < L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
            # print(L) // print list after finish every step
    return L

L = [3,1,7,6,2]
print(bubble_sort_asc(L))
print(bubble_sort_dsc(L))



