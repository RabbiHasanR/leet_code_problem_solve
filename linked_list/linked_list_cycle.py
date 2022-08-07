# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

 

# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:


# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:


# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
 

# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.
 

# Follow up: Can you solve it using O(1) (i.e. constant) memory?

# first solution
# time: O(n)
# space: O(n)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         next_data = []
#         current_node = head
#         hasC = False
#         while current_node:
#             if current_node.next in next_data:
#                 hasC = True
#                 break
#             next_data.append(current_node.next)
#             current_node = current_node.next
#         return hasC

# Second Solution using floyd's tortoise and hare algorithm
# time: O(n)
# space: O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, first = head, head
        while first and first.next:
            slow = slow.next
            first = first.next.next
            if slow == first:
                return True
        return False