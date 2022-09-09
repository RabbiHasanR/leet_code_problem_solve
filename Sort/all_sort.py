# selection sort


from multiprocessing.sharedctypes import Value


def selection_sort_asc(L):
    n = len(L)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if L[j] < L[min]:
                min = j
        if min != i:
            L[i],L[min] = L[min],L[i]

S = [5,8,3,9,10,3,2,5,6,2]
selection_sort_asc(S)
print('Acending order selection sort:',S)

# bubble sort

def bubble_sort_asc(L):
    n = len(L)
    for i in range(n):
        for j in range(n-i-1):
            if L[j] > L[j+1]:
                L[j],L[j+1] = L[j+1], L[j]

B = [5,8,3,9,10,3,2,5,6,2]
bubble_sort_asc(B)
print('Acending order bubble sort:',B)


# insertion sort

def insertin_sort_asc(L):
    n = len(L)
    for i in range(1,n):
        item = L[i]
        j = i - 1
        while j >=0 and L[j] > item:
            L[j+1] = L[j]
            j = j - 1
            L[j+1] = item

I = [5,8,3,9,10,3,2,5,6,2]

insertin_sort_asc(I)
print("Acending order insertion sort:", I)

# merge sort

def merge(a,b):
    sort_list = []
    len_a, len_b = len(a), len(b)
    index_a, index_b = 0,0

    while index_a < len_a and index_b < len_b:
        if a[index_a] < b[index_b]:
            sort_list.append(a[index_a])
            index_a += 1
        else:
            sort_list.append(b[index_b])
            index_b += 1
    if index_a < len_a:
        sort_list.extend(a[index_a:])
    if index_b < len_b:
        sort_list.extend(b[index_b:])
    return sort_list

def merge_sort_asc(L):
    n = len(L)
    if  n <= 1:
        return L
    mid = n // 2
    left = merge_sort_asc(L[:mid])
    right = merge_sort_asc(L[mid:])

    return merge(left, right)

M = [5,8,3,9,10,3,2,5,6,2]
print('Acending order merge sort:', merge_sort_asc(M))

# quick sort

def partition(L,low,high):
    pivot = L[high]
    i = low - 1

    for j in range(low,high):
        if L[j] < pivot:
            i += 1
            L[i], L[j] = L[j], L[i]
    
    L[i+1], L[high] = L[high], L[i+1]
    return i + 1

def quick_sort_asc(L,low,high):
    if low >= high:
        return
    p = partition(L,low,high)
    quick_sort_asc(L,low, p-1)
    quick_sort_asc(L,p+1,high)

Q = [5,8,3,9,10,3,2,5,6,2]
quick_sort_asc(Q,0, len(Q)-1)
print("Acending order quick sort:",Q)

    


# counting sort

def counting_sort_asc(L):
    max_number = max(L)
    count = [0] * (max_number+1)
    # print(count)
    for l in L:
        count[l] = count[l] + 1
    # print(count)
    sorted_list = []
    for index, value in enumerate(count):
        if index > 0:
            sorted_list.extend([index]*value)
    return sorted_list

C = [5,8,3,9,10,3,2,5,6,2]
print('Ascending order counting sort:', counting_sort_asc(C))