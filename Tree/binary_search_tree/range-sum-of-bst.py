# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

# Example 1:


# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
# Example 2:


# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 2 * 104].
# 1 <= Node.val <= 105
# 1 <= low <= high <= 105
# All Node.val are unique.

# first solution using in order
# time: O(n)
# space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def in_order(self,node,sort_list):
        if node.left:
            self.in_order(node.left,sort_list)
        sort_list.append(node.val)
        if node.right:
            self.in_order(node.right,sort_list)
            
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sort_list = []
        if root:
            self.in_order(root,sort_list)
            low_index = sort_list.index(low)
            high_index = sort_list.index(high)
            return sum(sort_list[low_index:high_index+1])
        return 0