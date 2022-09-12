# Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?

# first solution with recursivly
# time: O(n)
# space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def pre_order(self,node,res):
#         res.append(node.val)
#         if node.left:
#             self.pre_order(node.left,res)
#         if node.right:
#             self.pre_order(node.right,res)
            
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         if root:
#             self.pre_order(root,res)
#         return res

# second solution with iteratively
# time: O(n)
# space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        nStack = []
        curr = root
        while True:
            if curr:
                res.append(curr.val)
                nStack.append(curr)
                curr = curr.left
            elif nStack:
                curr = nStack.pop()
                curr = curr.right
            else:
                break
        return res
            
        