# merge sort algorithm
# Merge Sort is one of the most popular sorting algorithms that is based on the principle of Divide and Conquer Algorithm.

# Divide and Conquer Strategy
# Using the Divide and Conquer technique, we divide a problem into subproblems. When the solution to each subproblem is ready, we 'combine' the results from the subproblems to solve the main problem.

# Suppose we had to sort an array A. A subproblem would be to sort a sub-section of this array starting at index p and ending at index r, denoted as A[p..r].

# Divide

# If q is the half-way point between p and r, then we can split the subarray A[p..r] into two arrays A[p..q] and A[q+1, r].

# Conquer

# In the conquer step, we try to sort both the subarrays A[p..q] and A[q+1, r]. If we haven't yet reached the base case, we again divide both these subarrays and try to sort them.

# Combine

# When the conquer step reaches the base step and we get two sorted subarrays A[p..q] and A[q+1, r] for array A[p..r], we combine the results by creating a sorted array A[p..r] from two sorted subarrays A[p..q] and A[q+1, r].


# merge sort hosse list ke 2 vaghe vagh kore sort kore pore dui vag k merge kora

# L =[1,5,6,3,8,4,7,2]

# [1,5,6,3]        [8,4,7,2]
# [1,5]   [6,3]    [8.4]   [7.2]
# [1] [5] [6] [3]  [8] [4] [7] [2]
# [1,5]   [3,6]    [4,8]   [2,7]
# [1,3,5,6]        [2,4,7,8]
# [1,2,3,4,5,6,7,8] 


# step 1: split list L [1,5,6,3]        [8,4,7,2]
# step 2: split list [1,5,6,3] = [1,5] , [6,3]  and [8,4,7,2] = [8.4] , [7.2]
# step 3: split [1,5] = [1] , [5] and [6,3] = [6] , [3]  and [8,4] = [8],[4] and [7,2] = [7] [2]
# step 4: now comapre and sort acending order and merge [1],[5= [1,5]. 
# comapre and sort acending order and merge [6],[3] = [3,6].
# comapre and sort acending order and merge [8],[4] = [4,8].
# comapre and sort acending order and merge [7] [2] = [2,7]
# step 5: now compare and sort acending order and merge [1,5],[3,6] = [1,3,5,6].
# compare and sort acending order and merge [4,8],[2,7] = [2,4,7,8]
# step 6: now compare and sort acending order and merge [1,3,5,6],[2,4,7,8] = [1,2,3,4,5,6,7,8] 
# step 7: finally get acending order sorted list [1,2,3,4,5,6,7,8] 


# merge sort algorithm

# input: List L = [1,5,6,3,8,4,7,2]
# step 1: if list length n <=1 then list already be sorted . so return the list
# step 2: divide L list and merge_sort first half and assign left variable
# step 3: merge_sort second half and assign right variable
# step 4: merge List left and right 


# tiem: O(nlogn)
# space: O(n)

# meger sort implementation acending order
#acending order
def merge_asc(a,b):
    merge_list = []
    len_a, len_b = len(a), len(b)
    index_a, index_b = 0,0
    while index_a < len_a and index_b < len_b:
        if a[index_a] < b[index_b]:
            merge_list.append(a[index_a])
            index_a += 1
        else:
            merge_list.append(b[index_b])
            index_b += 1
    if index_a < len_a:
        merge_list.extend(a[index_a:])
    if index_b < len_b:
        merge_list.extend(b[index_b:])
    return merge_list

def merge_sort_asc(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = merge_sort_asc(L[:mid])
    right = merge_sort_asc(L[mid:])
    return merge_asc(left, right)


#decending order
def merge_dsc(a,b):
    merge_list = []
    len_a, len_b = len(a), len(b)
    index_a, index_b = 0,0
    while index_a < len_a and index_b < len_b:
        if a[index_a] > b[index_b]:
            merge_list.append(a[index_a])
            index_a += 1
        else:
            merge_list.append(b[index_b])
            index_b += 1
    if index_a < len_a:
        merge_list.extend(a[index_a:])
    if index_b < len_b:
        merge_list.extend(b[index_b:])
    return merge_list

def merge_sort_dsc(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = merge_sort_dsc(L[:mid])
    right = merge_sort_dsc(L[mid:])
    return merge_dsc(left, right)

L = [1,5,6,3,8,4,7,2]
print(merge_sort_asc(L))
print(merge_sort_dsc(L))


