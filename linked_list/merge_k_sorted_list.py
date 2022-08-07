# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.



#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# first_solution
#  time: O(n2)
#  space: O(1)  

      
# class Solution:
#     def merge(self, list1, list2):
#         dummy = ListNode()
#         tail = dummy
#         while list1 and list2:
#             if list1.val < list2.val:
#                 tail.next = list1
#                 list1 = list1.next
#             else:
#                 tail.next = list2
#                 list2 = list2.next
#             tail = tail.next
#         if list1:
#             tail.next = list1
#         else:
#             tail.next = list2
#         return dummy.next
    
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         merge_list = ListNode()
#         if len(lists):
#             merge_list.next = lists[0]
#             index = 1

#             while index < len(lists):
#                 temp_list = lists[index]
#                 merge_list.next = self.merge(merge_list.next, temp_list)
#                 index += 1
#             return merge_list.next
#         return merge_list.next


# second solution
# time: O(nlogn)
# space: O(logn)

class Solution:
    
    def merge(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            merge_lists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i+1) < len(lists) else None
                merge_lists.append(self.merge(list1, list2))
            lists = merge_lists
        return lists[0]