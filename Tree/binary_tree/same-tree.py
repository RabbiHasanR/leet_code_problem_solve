# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

# Example 1:


# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:


# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:


# Input: p = [1,2,1], q = [1,1,2]
# Output: false
 

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104

# first solution
# time: O(n)
# space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pre_order(self,node, tree_list):
        if node:
            tree_list.append(node.val)
            self.pre_order(node.left,tree_list)
            self.pre_order(node.right,tree_list)
        else:
            tree_list.append(None)
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_list = []
        q_list = []
        self.pre_order(p,p_list)
        self.pre_order(q,q_list)
        # print(p_list,q_list)
        if p_list == q_list:
            return True
        return False