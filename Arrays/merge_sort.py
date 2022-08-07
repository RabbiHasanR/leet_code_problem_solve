# merge two sorted list
# time: O(n)
# space: O(n)
def merge(list1, list2):
    merge_list = []
    index_list1, index_list2 = 0, 0

    while index_list1 < len(list1) and index_list2 < len(list2):
        if list1[index_list1] < list2[index_list2]:
            merge_list.append(list1[index_list1])
            index_list1 += 1
        else:
            merge_list.append(list2[index_list2])
            index_list2 += 1
    if index_list1 < len(list1):
        merge_list.extend(list1[index_list1:])
    elif index_list2 < len(list2):
        merge_list.extend(list2[index_list2:])
    
    return merge_list

# merge sort
# time: O(nlogn)
# space: O(n)
def merge_sort(list):
    if len(list) <=1:
        return list
    middle = len(list) // 2

    left_list = merge_sort(list[:middle])
    right_list = merge_sort(list[middle:])

    return merge(left_list, right_list)


# list1 = [1,2,3,4,5,6]
# list2 = [1,2,3,4,7,8,9]

# print(merge(list1, list2))

list = [[4,7,2,3], [10], [10,9,8,7,6], [2,3,1], [1,2], [2,1]]
index = 1
list_1 = merge_sort(list[0])
list_2 = []
while index < len(list):
    list_2 = merge_sort(list[index])
    list_1 = merge(list_1, list_2)
    index += 1
print(list_1)