# quick sort 

# Quicksort is a sorting algorithm based on the divide and conquer approach where

# An array is divided into subarrays by selecting a pivot element (element selected from the array).here picot is list last element.

# While dividing the array, the pivot element should be positioned in such a way that elements less than pivot are kept on the left side and elements greater than pivot are on the right side of the pivot.

# The left and right subarrays are also divided using the same approach. This process continues until each subarray contains a single element.

# At this point, elements are already sorted. Finally, elements are combined to form a sorted array.

# quick sort visualization

# L = [8,7,6,1,0,9,2]

# step 1: [8,7,6,1,0,9,2] here 2 is pivot
# step 2: after pivot place in right position and partitioning list [1,0,2,8,7,9,6]
# step 3: now quick sort in left partition [1,0]. here pivot is 0 .after pivot place in right position anr partitioning
#         list is [0,1] .pivot left partition is empty and pivot right partition has only one item [1]
#         now quick sot in right partition [1].since here is only one value so its already sort.
#         after quick sort left partition [1,0] main list is [0,1,2,8,7,9,6] 

# step 4: now quick sort in right partiion [8,7,9,6]. here pivot is 6. after pivot place in right position and 
#         partiioning list is [6,7,9,8] and so main list is now [0,1,2,6,7,9,8]. pivot left partition is empty and pivot right partion is [7,9,8].
#         right partition pivot is 8.after pivot place in right position and partitioning list is [7,8,9] so main
#         list is [0,1,2,6,7,8,9].
#         now left partion is [7] and since here is only one value sot its already sort and right partion is [9].
#         and since here also is only one value so its already sort and main list also sort
# step 5: so sorted list is [0,1,2,6,7,8,9]

# quick sort algorithm

# input: input list L and first index low = 0 and last index high = n-1
# step 1: if L.length <= 1 then return L
# step 2: now partition list based on pivot and place pivot in right position. assume pivot position = p
# step 3: now quicksort list low index from p-1 index subarray
# step 4: now quicksort list p+1 from list high index subarray


# time: avg:O(nlogn) worst O(n^2)
# space: O(logn)

# acending order sort

def partition_asc(L,low,high):
    pivot = L[high]
    i = low - 1

    for j in range(low, high):
        if L[j] < pivot:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[high] = L[high], L[i + 1]
    return i + 1

def quick_sort_asc(L,low,high):
    if low >= high:
        return L
    p = partition_asc(L, low, high)
    quick_sort_asc(L,low,p-1)
    quick_sort_asc(L,p+1,high)

L = [8,7,6,1,0,9,2]
quick_sort_asc(L, 0, len(L)-1)
print(L)

# decending order sort

def partition_dsc(L,low,high):
    pivot = L[high]
    i = low - 1

    for j in range(low, high):
        if L[j] > pivot:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[high] = L[high], L[i + 1]
    return i + 1

def quick_sort_dsc(L,low,high):
    if low >= high:
        return
    p = partition_dsc(L, low, high)
    quick_sort_dsc(L,low,p-1)
    quick_sort_dsc(L,p+1,high)

K = [8,7,6,1,0,9,2]
quick_sort_dsc(K, 0, len(K)-1)
print(K)