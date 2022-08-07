# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

# first solution
# time O(n^2)
# space O(1)

# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         total_good_pair = 0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] == nums[j]:
#                     total_good_pair += 1
#         return total_good_pair

# second solution
# time O(n)
# space O(n)

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        repeate_num = {}
        num = 0
        for n in nums:
            if n in repeate_num:
                num += repeate_num[n]
                repeate_num[n] += 1
            else:
                repeate_num[n] = 1
        return num

sol = Solution()
nums = [1,2,3,1,1,3]
print(sol.numIdenticalPairs(nums))