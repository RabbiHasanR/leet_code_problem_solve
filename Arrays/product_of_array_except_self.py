# problem

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# first solution
# time complexity for this solution O(n)
# space complexity for this solution O(1)
# class Solution:
#     def productExceptSelf(self, nums):
#         pre, post = 1,1
#         prefix = [1]*len(nums)
#         postfix = [1]*len(nums)
#         result = [1]*len(nums)
        
#         for n in range(len(nums)):
#             pre *= nums[n]
#             prefix[n] = pre
#         for n in range(len(nums)-1,-1,-1):
#             post *= nums[n]
#             postfix[n]=post

#         for n in range(len(nums)):
#             if n == 0:
#                 result[n]=1*postfix[n+1]
#             elif n < len(nums)-1:
#                 result[n]=prefix[n-1]*postfix[n+1]
#             else:
#                 result[n]=prefix[n-1]*1

#         return result

# second solution
# time complexity for this solution O(n)
# space complexity for this solution O(1)

class Solution:
    def productExceptSelf(self, nums):
        result = [1]*(len(nums))
        prefix = 1
        for n in range(len(nums)):
            result[n] = prefix
            prefix *= nums[n]
        
        postfix = 1
        for n in range(len(nums)-1, -1, -1):
            result[n] *= postfix
            postfix *= nums[n]
        return result

s = Solution()
nums = [1,2,3,4]
print(s.productExceptSelf(nums))